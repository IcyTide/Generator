from enum import StrEnum


class BuffType(StrEnum):
    Self = "Self"
    Target = "Target"
    Snapshot = "Snapshot"


class Buff:
    belong: str
    buff_id: int
    buff_level: int
    stack: int
    buff_type: str

    name: str = ""
    comment: str = ""
    max_stack: int
    max_tick: int

    def __init__(self, belong: str, buff_id: int, buff_level: int, buff_type: str, stack: int = 1, **kwargs):
        self.belong = belong
        self.buff_id = buff_id
        self.buff_level = buff_level
        self.stack = stack
        self.buff_type = buff_type
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __iter__(self):
        yield str(self)
        for attr in ("buff_id", "buff_level", "stack", "buff_type"):
            yield str(getattr(self, attr))

    def __str__(self):
        if self.name and self.comment:
            return f"{self.name}({self.comment})"
        elif self.name:
            return self.name
        elif self.comment:
            return self.comment
        return f"{self.buff_id}-{self.buff_level}"