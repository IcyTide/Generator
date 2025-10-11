from assets.raw.dots import DOTS
from qt.classes.skill import Skill


class Dot:
    dot_id: int
    dot_level: int
    count: int
    source: Skill = None
    tick: int

    name: str
    comment: str = ""
    skills: dict
    max_stack: int
    max_tick: int

    @property
    def stack(self):
        return self.source.count

    def __init__(self, belong: str, dot_id: int, dot_level: int, tick: int = 1, count: int = 1, **kwargs):
        self.belong = belong
        self.dot_id = dot_id
        self.dot_level = dot_level
        self.tick = tick
        self.count = count
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __iter__(self):
        yield str(self)
        for attr in ("dot_id", "dot_level", "stack", "tick", "count"):
            yield str(getattr(self, attr))

    def __str__(self):
        if self.name and self.comment:
            return f"{self.name}({self.comment})"
        elif self.name:
            return self.name
        elif self.comment:
            return self.comment
        return f"{self.dot_id}-{self.dot_level}"

    def to_dict(self):
        return dict(
            belong=self.belong,
            dot_id=self.dot_id,
            dot_level=self.dot_level,
            source=self.source.to_dict(),
            tick=self.tick,
            count=self.count
        )

    @classmethod
    def from_dict(cls, kungfu_id: int, json: dict, **kwargs):
        if not kwargs:
            kwargs = DOTS[kungfu_id][json["dot_id"]][json["dot_level"]]
        dot = cls(
            belong=json["belong"],
            dot_id=json["dot_id"],
            dot_level=json["dot_level"],
            tick=json["tick"],
            count=json["count"],
            **kwargs
        )
        source = json["source"]
        skill_kwargs = dot.skills[source["skill_id"]][source["skill_level"]]
        dot.source = Skill.from_dict(
            kungfu_id,
            source,
            **skill_kwargs
        )
        return dot