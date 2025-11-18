from assets.raw.enchants import ENCHANTS
from assets.raw.equipments import EQUIPMENTS
from base.constant import EMBED_COF, POSITIONS, ROUND, STRENGTH_COF
from qt.classes.gains.gear import GearGain


class Stone:
    name: str

    attributes: dict[str, int]
    level: int

    def __init__(self, detail):
        self.detail = detail
        for k, v in detail.items():
            setattr(self, k, v)

    def to_dict(self):
        return self.detail

    @classmethod
    def from_dict(cls, json):
        if not json:
            return None
        return cls(json)


class Enchant:
    id: int
    enchant: str

    attributes: dict[str, int]

    def __init__(self, enchant, detail: dict):
        self.enchant = enchant
        self.detail = detail
        for k, v in detail.items():
            setattr(self, k, v)

    def to_dict(self):
        return dict(id=self.id, enchant=self.enchant)

    @classmethod
    def from_dict(cls, position: str, json: dict):
        if not json:
            return None
        return cls(json["enchant"], ENCHANTS[POSITIONS[position]][json["enchant"]])


class Gear:
    id: int

    school: str
    kind: str
    equipment: str
    enchant: Enchant | None = None
    stone: Stone | None = None
    strength_level: int
    embed_levels: dict[int, int]

    level: int
    name: str
    base: dict[str, int] = {}
    magic: dict[str, int] = {}
    embed: dict[str, int] = {}

    max_strength: int

    special_enchant: str | None = None
    recipes: list[str]
    gains: list[str]
    set_id: int
    sets: dict[int, dict]

    def __init__(self, school, kind, equipment, detail: dict):
        self.school = school
        self.kind = kind
        self.equipment = equipment
        self.strength_level = 0
        self.embed_levels = {}
        self.detail = detail
        for k, v in detail.items():
            setattr(self, k, v)

    @property
    def strength_magic(self):
        if not self.magic or not self.strength_level:
            return {}
        return {k: ROUND(v * STRENGTH_COF(self.strength_level)) for k, v in self.magic.items()}

    @property
    def embeds(self):
        if not self.embed or not any(self.embed_levels.values()):
            return {}
        return {k: int(v * EMBED_COF(self.embed_levels[i])) for i, (k, v) in enumerate(self.embed.items())}

    @property
    def attributes(self):
        attributes = {}
        for k, v in self.base.items():
            if k not in attributes:
                attributes[k] = 0
            attributes[k] += v
        for k, v in self.magic.items():
            if k not in attributes:
                attributes[k] = 0
            attributes[k] += v
        for k, v in self.strength_magic.items():
            if k not in attributes:
                attributes[k] = 0
            attributes[k] += v
        for k, v in self.embeds.items():
            if k not in attributes:
                attributes[k] = 0
            attributes[k] += v
        if self.enchant:
            for k, v in self.enchant.attributes.items():
                if k not in attributes:
                    attributes[k] = 0
                attributes[k] += v
        if self.stone:
            for k, v in self.stone.attributes.items():
                if k not in attributes:
                    attributes[k] = 0
                attributes[k] += v
        return attributes

    def to_dict(self):
        return dict(
            school=self.school,
            kind=self.kind,
            equipment=self.equipment,
            id=self.id,
            strength_level=self.strength_level,
            embed_levels=self.embed_levels,
            enchant=self.enchant.to_dict() if self.enchant else None,
            special_enchant=self.special_enchant,
            stone=self.stone
        )

    @classmethod
    def from_dict(cls, position: str, json: dict):
        if not json:
            return None
        instance = cls(
            json["school"],
            json["kind"],
            json["equipment"],
            EQUIPMENTS[POSITIONS[position]][json["school"]][json["kind"]][json["equipment"]]
        )
        instance.strength_level = json["strength_level"]
        instance.embed_levels = {int(k): v for k, v in json["embed_levels"].items()}
        instance.enchant = Enchant.from_dict(position, json["enchant"])
        instance.special_enchant = json["special_enchant"]
        instance.stone = Stone.from_dict(json["stone"])
        return instance


class Gears:
    def __init__(self, gears: dict[str, Gear] = None):
        if not gears:
            self.gears = {}
        else:
            self.gears = gears

    def __setitem__(self, key, value):
        self.gears[key] = value

    def __getitem__(self, key):
        return self.gears[key]

    def get(self, key):
        if key not in self.gears:
            return None
        return self.gears[key]

    def pop(self, key):
        if key not in self.gears:
            return None
        return self.gears.pop(key)

    def __bool__(self):
        return bool(self.gears)

    @property
    def content(self):
        set_count, set_bonus = {}, {}
        attributes, recipes, gains = {}, [], {}
        for gear in self.gears.values():
            for k, v in gear.attributes.items():
                if k not in attributes:
                    attributes[k] = 0
                attributes[k] += v
            recipes += gear.recipes
            if gear.special_enchant:
                gains[gear.special_enchant] = GearGain(gear.special_enchant)
            for k in gear.gains:
                gains[k] = GearGain(k)
            if set_id := gear.set_id:
                if set_id not in set_count:
                    set_count[set_id] = 0
                    set_bonus[set_id] = gear.sets
                set_count[set_id] += 1
        for set_id, count in set_count.items():
            for need_count, bonus in set_bonus[set_id].items():
                if count >= need_count:
                    for k, v in bonus.get("attributes", {}).items():
                        if k not in attributes:
                            attributes[k] = 0
                        attributes[k] += v
                    recipes += bonus.get("recipes", [])
                    for k in bonus.get("gains", []):
                        gains[k] = GearGain(k)
        return attributes, recipes, gains

    def to_dict(self):
        if not self:
            return {}
        ret = {}
        for k, v in self.gears.items():
            ret[k] = v.to_dict()
        return ret

    @classmethod
    def from_dict(cls, json: dict):
        if not json:
            return cls()
        instance = cls({
            position: Gear.from_dict(position, gear)
            for position, gear in json.items()
        })
        return instance
