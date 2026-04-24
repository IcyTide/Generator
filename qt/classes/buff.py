from enum import StrEnum

from assets.raw.buffs import BUFFS


class BuffType(StrEnum):
    Both = "Both"
    Current = "Current"
    Snapshot = "Snapshot"


class Buff:
    belong_id: int
    buff_id: int
    buff_level: int
    stack: float
    buff_type: str

    name: str = ""
    comment: str = ""
    on_target: int = 0
    attributes: dict[str, int] = {}
    recipes: list[str] = []
    buff_key: str = ""
    max_stack: int = 1
    max_tick: int = 1

    def __init__(self, belong_id: int, buff_id: int, buff_level: int, buff_type: str, stack: float = 1, **kwargs):
        self.belong_id = belong_id
        self.buff_id = buff_id
        self.buff_level = buff_level
        self.stack = stack
        self.buff_type = buff_type
        self.kwargs = kwargs
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __iter__(self):
        yield str(self)
        yield str(self.buff_id)
        yield str(self.buff_level)
        yield str(self.stack)
        yield str(self.buff_type)

    def __str__(self):
        if self.name and self.comment:
            return f"{self.name}({self.comment})"
        elif self.name:
            return self.name
        elif self.comment:
            return self.comment
        return f"{self.buff_id}-{self.buff_level}"

    def copy(self):
        return Buff(self.belong_id, self.buff_id, self.buff_level, self.buff_type, self.stack, **self.kwargs)

    def to_dict(self):
        return dict(
            belong_id=self.belong_id,
            buff_id=self.buff_id,
            buff_level=self.buff_level,
            buff_type=self.buff_type,
            stack=self.stack
        )

    @classmethod
    def from_dict(cls, kungfu_id: int, json: dict):
        kungfu_buffs = BUFFS[kungfu_id] | BUFFS[0]
        if json["belong_id"] not in kungfu_buffs:
            return None
        belong_buffs = kungfu_buffs[json["belong_id"]]
        if json["buff_id"] not in belong_buffs:
            return None
        buffs = belong_buffs[json["buff_id"]]
        if json["buff_level"] not in buffs:
            return None
        kwargs = buffs[json["buff_level"]]
        return cls(
            belong_id=json["belong_id"],
            buff_id=json["buff_id"],
            buff_level=json["buff_level"],
            buff_type=json["buff_type"],
            stack=json["stack"],
            **kwargs
        )
