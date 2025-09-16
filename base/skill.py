from assets.raw.skills import SKILLS


class Skill:
    belong: str
    skill_id: int
    skill_level: int
    count: int

    name: str
    comment: str

    def __init__(self, belong: str, skill_id: int, skill_level: int, **kwargs):
        self.belong = belong
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.count = 0
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __iter__(self):
        for attr in ("skill_id", "skill_level", "count"):
            yield str(getattr(self, attr))