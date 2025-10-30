from assets.raw.buffs import BUFFS
from assets.raw.enchants import ENCHANTS
from base.translate import get_translates


def parse_content(content: dict):
    if "attributes" not in content:
        return None, None
    name = content["name"]
    attributes = content["attributes"]
    translates, _ = get_translates(attributes)
    desc = "/".join(f"{v}{translates[k]}" for k, v in attributes.items())
    return f"{name}({desc})", attributes


def create_consumable(buff_ids: int | list):
    result = {}
    if isinstance(buff_ids, int):
        buff_ids = [buff_ids]
    for buff_id in buff_ids:
        for buff_level, content in BUFFS[0][buff_id].items():
            name, attributes = parse_content(content)
            if not name:
                continue
            result[name] = attributes
    return result


MAJOR_FOODS = create_consumable(29274)
MINOR_FOODS = create_consumable(29276)
MAJOR_POTIONS = create_consumable(29288)
MINOR_POTIONS = create_consumable(29289)
SPREADS = {
    **create_consumable(29284),
    **create_consumable(29285)
}
SNACKS = {
    **create_consumable(17365),
    **{k: v for buff_id in [27784, 27785, 27786, 27787, 27788, 27792] for k, v in create_consumable(buff_id).items()}
}
WINES = {
    k: v for buff_id in [17349, 17352, 17355, 17358, 17361] for k, v in create_consumable(buff_id).items()
}
BOILED_FISHES = create_consumable(10100)
GUILD_FOODS = create_consumable(2563)
GUILD_SPREADS = create_consumable(18428)

WEAPON_ENCHANTS = ENCHANTS["consumable"]

CONSUMABLES = {
    **MAJOR_FOODS,
    **MINOR_FOODS,
    **MAJOR_POTIONS,
    **MINOR_POTIONS,
    **SPREADS,
    **SNACKS,
    **WINES,
    **BOILED_FISHES,
    **GUILD_FOODS,
    **GUILD_SPREADS,
    **WEAPON_ENCHANTS
}


class Consumable:
    def __init__(self, name: str):
        self.name = name
        self.attributes = CONSUMABLES[name]

    def to_dict(self):
        return self.name

    @classmethod
    def from_dict(cls, name: str):
        return cls(name)


class Consumables:
    def __init__(self, consumables: dict[str, Consumable] = None):
        if not consumables:
            self.consumables = {}
        else:
            self.consumables = consumables

    def __setitem__(self, key, value):
        self.consumables[key] = Consumable(value)

    def __getitem__(self, key):
        return self.consumables[key]

    def __iter__(self):
        for consumable in self.consumables.values():
            yield consumable

    def get(self, key):
        if key not in self.consumables:
            return ""
        return self.consumables[key]

    def pop(self, key):
        if key not in self.consumables:
            return None
        return self.consumables.pop(key)

    @property
    def content(self):
        attributes = {}
        for consumable in self:
            for k, v in consumable.attributes.items():
                if k not in attributes:
                    attributes[k] = 0
                attributes[k] += v
        return attributes

    def to_dict(self):
        return {k: v.to_dict() for k, v in self.consumables.items()}

    @classmethod
    def from_dict(cls, consumables: dict[str, str]):
        return Consumables({k: Consumable.from_dict(v) for k, v in consumables.items()})
