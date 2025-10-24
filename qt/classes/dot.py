from assets.raw.dots import DOTS
from qt.classes.skill import Skill


class Dot:
    dot_id: int
    dot_level: int
    count: float
    source: Skill = None
    consume_tick: int = 1
    current_tick: int = 1

    name: str
    comment: str = ""
    skills: dict
    max_stack: int
    max_tick: int

    @property
    def stack(self):
        return self.source.count

    @property
    def total(self):
        return f"{self.stack}/{self.consume_tick}"

    def __init__(self, belong: str, dot_id: int, dot_level: int, count: float = 1., **kwargs):
        self.belong = belong
        self.dot_id = dot_id
        self.dot_level = dot_level
        self.count = count
        self.kwargs = kwargs
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __iter__(self):
        yield str(self)
        for attr in ("dot_id", "dot_level", "total", "count"):
            yield str(getattr(self, attr))

    def __str__(self):
        if self.name and self.comment:
            return f"{self.name}({self.comment})"
        elif self.name:
            return self.name
        elif self.comment:
            return self.comment
        return f"{self.dot_id}-{self.dot_level}"

    def copy(self):
        dot = Dot(self.belong, self.dot_id,  self.dot_level, self.count, **self.kwargs)
        dot.source = self.source.copy()
        dot.consume_tick = self.consume_tick
        dot.current_tick = self.current_tick
        return dot

    def to_dict(self):
        return dict(
            belong=self.belong,
            dot_id=self.dot_id,
            dot_level=self.dot_level,
            source=self.source.to_dict(),
            consume_tick=self.consume_tick,
            current_tick=self.current_tick,
            count=self.count
        )

    @classmethod
    def from_dict(cls, kungfu_id: int, json: dict, **kwargs):
        if not kwargs:
            if json["dot_id"] in DOTS[kungfu_id]:
                kwargs = DOTS[kungfu_id][json["dot_id"]][json["dot_level"]]
            else:
                kwargs = DOTS[0][json["dot_id"]][json["dot_level"]]
        dot = cls(
            belong=json["belong"],
            dot_id=json["dot_id"],
            dot_level=json["dot_level"],
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
        dot.consume_tick = json["consume_tick"]
        dot.current_tick = json["current_tick"]
        return dot
