from assets.raw.dots import DOTS
from qt.classes.skill import Skill


class Dot:
    belong_id: int
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

    def __init__(self, belong_id: int, dot_id: int, dot_level: int, count: float = 1., **kwargs):
        self.belong_id = belong_id
        self.dot_id = dot_id
        self.dot_level = dot_level
        self.count = count
        self.kwargs = kwargs
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.belong2id = {self.name: self.belong_id}
        self.id2belong = {v: k for k, v in self.belong2id.items()}
        self.skills = {self.name: self.skills}

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
        dot = Dot(self.belong_id, self.dot_id, self.dot_level, self.count, **self.kwargs)
        dot.source = self.source.copy()
        dot.consume_tick = self.consume_tick
        dot.current_tick = self.current_tick
        return dot

    def to_dict(self):
        return dict(
            belong_id=self.belong_id,
            dot_id=self.dot_id,
            dot_level=self.dot_level,
            source=self.source.to_dict(),
            consume_tick=self.consume_tick,
            current_tick=self.current_tick,
            count=self.count
        )

    @classmethod
    def from_dict(cls, kungfu_id: int, json: dict):
        kungfu_dots = DOTS.get(kungfu_id, {})
        if json["belong_id"] not in kungfu_dots:
            return None
        belong_dots = kungfu_dots[json["belong_id"]]
        if json["dot_id"] not in belong_dots:
            return None
        dots = belong_dots[json["dot_id"]]
        if json["dot_level"] not in dots:
            return None
        kwargs = dots[json["dot_level"]]
        dot = cls(
            belong_id=json["belong_id"],
            dot_id=json["dot_id"],
            dot_level=json["dot_level"],
            count=json["count"],
            **kwargs
        )
        source_json = json["source"]
        source_skills = dot.skills[dot.name]
        if source_json["skill_id"] not in source_skills:
            return None
        skills = source_skills[source_json["skill_id"]]
        if source_json["skill_level"] not in skills:
            return None
        source_kwargs = skills[source_json["skill_level"]]
        dot.source = Skill(
            belong_id=source_json["belong_id"],
            skill_id=source_json["skill_id"],
            skill_level=source_json["skill_level"],
            count=source_json["count"],
            **source_kwargs
        )
        dot.consume_tick = json["consume_tick"]
        dot.current_tick = json["current_tick"]
        return dot
