class Skill:
    belong: str
    skill_id: int
    skill_level: int
    count: int

    name: str = ""
    comment: str = ""

    def __init__(self, belong: str, skill_id: int, skill_level: int, count: int = 1, **kwargs):
        self.belong = belong
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.count = count
        self.kwargs = kwargs
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __iter__(self):
        yield str(self)
        for attr in ("skill_id", "skill_level", "count"):
            yield str(getattr(self, attr))

    def __str__(self):
        if self.name and self.comment:
            return f"{self.name}({self.comment})"
        elif self.name:
            return self.name
        elif self.comment:
            return self.comment
        return f"{self.skill_id}-{self.skill_level}"
