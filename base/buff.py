from enum import StrEnum


class BuffType(StrEnum):
    Self = "Self"
    Target = "Target"
    Snapshot = "Snapshot"


class Buff:
    belong: str
    buff_id: int
    buff_level: int
    buff_stack: int
    buff_type: str

    name: str
    comment: str
    max_stack: int
    max_tick: int

    def __init__(self, belong: str, buff_id: int, buff_level: int, buff_type: str, **kwargs):
        self.belong = belong
        self.buff_id = buff_id
        self.buff_level = buff_level
        self.buff_stack = 0
        self.buff_type = buff_type
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __iter__(self):
        for attr in ("buff_id", "buff_level", "buff_stack", "buff_type"):
            yield str(getattr(self, attr))
