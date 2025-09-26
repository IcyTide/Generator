from collections import defaultdict

from base.constant import EMBED_COF, ROUND, STRENGTH_COF


class Stone:
    name: str
    attributes: dict[str, int]

    def __init__(self, detail):
        for k, v in detail.items():
            setattr(self, k, v)


class Enchant:
    enchant: str

    attributes: dict[str, int]

    def __init__(self, enchant, detail: dict):
        self.enchant = enchant
        for k, v in detail.items():
            setattr(self, k, v)


class Gear:
    school: str
    kind: str
    equipment: str
    enchant: Enchant | None = None
    strength_level: int
    embed_levels: dict[int, int]

    name: str
    base: dict[str, int] = {}
    magic: dict[str, int] = {}
    embed: dict[str, int] = {}

    max_strength: int

    def __init__(self, school, kind, equipment, detail: dict):
        self.school = school
        self.kind = kind
        self.equipment = equipment
        self.strength_level = 0
        self.embed_levels = {}
        for k, v in detail.items():
            setattr(self, k, v)

    @property
    def strength_magic(self):
        if not self.magic or not self.strength_level:
            return {}
        return {k: ROUND(v * STRENGTH_COF(self.strength_level)) for k, v in self.magic.items()}

    @property
    def embeds(self):
        if not self.embed or not all(self.embed_levels.values()):
            return {}
        return {k: int(v * EMBED_COF(self.embed_levels[i])) for i, (k, v) in enumerate(self.embed.items())}

    @property
    def attributes(self):
        attributes = defaultdict(int)
        for k, v in self.base.items():
            attributes[k] += v
        for k, v in self.magic.items():
            attributes[k] += v
        for k, v in self.strength_magic.items():
            attributes[k] += v
        for k, v in self.embeds.items():
            attributes[k] += v
        for k, v in self.enchant.attributes.items():
            attributes[k] += v
        return attributes
