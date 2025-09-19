from base.skill import Skill


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
        for attr in ("dot_id", "dot_level", "source", "tick", "count"):
            if value := getattr(self, attr):
                yield str(value)
            else:
                yield ""

    def __str__(self):
        if self.name and self.comment:
            return f"{self.name}({self.comment})"
        elif self.name:
            return self.name
        elif self.comment:
            return self.comment
        return f"{self.dot_id}-{self.dot_level}"