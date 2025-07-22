from enum import StrEnum

from assets.raw.buffs import BUFFS


class BuffType(StrEnum):
    Self = "Self"
    Target = "Target"
    Snapshot = "Snapshot"


class Buff:
    buff_type: BuffType = BuffType.Self
    buff_id: int
    buff_level: int = 1
    stack: int = 1

    max_level: int = 1
    max_stack: int = 1

    _attributes: list[list[tuple[str, int, int]]] = []
    _recipes: list[list[tuple[int, int]]] = []

    def __init__(self, buff_id, buff_type, buff_level: int = 1, stack: int = 1):
        self.buff_id = buff_id
        self.buff_type = buff_type
        self.buff_level = buff_level
        self.stack = stack
        for k, v in BUFFS[self.buff_id].items():
            setattr(self, k, v)

    @property
    def attributes(self):
        if self.buff_level > len(self._attributes):
            return self._attributes[-1]
        else:
            return self._attributes[self.buff_level - 1]

    @attributes.setter
    def attributes(self, value):
        self._attributes = value

    @property
    def recipes(self):
        if self.buff_level > len(self._recipes):
            return self._recipes[-1]
        else:
            return self._recipes[self.buff_level - 1]

    @recipes.setter
    def recipes(self, value):
        self._recipes = value

    def __iter__(self):
        for attr in ("buff_type", "buff_id", "buff_level", "stack",):
            yield str(getattr(self, attr))