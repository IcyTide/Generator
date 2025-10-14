from enum import StrEnum

from assets.raw.buffs import BUFFS


class BuffType(StrEnum):
    Both = "Both"
    Current = "Current"
    Snapshot = "Snapshot"


class Buff:
    belong: str
    buff_id: int
    buff_level: int
    stack: int
    buff_type: str

    name: str = ""
    comment: str = ""
    attributes: dict[str, int] = {}
    recipes: list[str] = []
    buff_key: str = ""
    max_stack: int = 1
    max_tick: int = 1

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

    def to_dict(self):
        return dict(
            belong=self.belong,
            buff_id=self.buff_id,
            buff_level=self.buff_level,
            buff_type=self.buff_type,
            stack=self.stack
        )

    @classmethod
    def from_dict(cls, kungfu_id: int, json: dict, **kwargs):
        if not kwargs:
            kwargs = BUFFS[kungfu_id][json["buff_id"]][json["buff_level"]]
        return cls(
            belong=json["belong"],
            buff_id=json["buff_id"],
            buff_level=json["buff_level"],
            buff_type=json["buff_type"],
            stack=json["stack"],
            **kwargs
        )
