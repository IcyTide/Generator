from assets.raw.skills import SKILLS
from base.expression import Expression, parse_expr


class Skill:
    belong: str
    skill_id: int
    skill_level: int
    count: int

    name: str = ""
    comment: str = ""
    damage: str | Expression
    critical_damage: str | Expression
    critical_strike: str | Expression
    attributes: dict[str, int] = {}

    def __init__(self, belong: str, skill_id: int, skill_level: int, count: int = 1, **kwargs):
        self.belong = belong
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.count = count
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.damage = parse_expr(self.damage)
        self.critical_damage = parse_expr(self.critical_damage)
        self.critical_strike = parse_expr(self.critical_strike)

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

    def to_dict(self):
        return dict(
            belong=self.belong,
            skill_id=self.skill_id,
            skill_level=self.skill_level,
            count=self.count
        )

    @classmethod
    def from_dict(cls, kungfu_id: int, json: dict, **kwargs):
        if not kwargs:
            kwargs = SKILLS[kungfu_id][json["skill_id"]][json["skill_level"]]
        return cls(
            belong=json["belong"],
            skill_id=json["skill_id"],
            skill_level=json["skill_level"],
            count=json["count"],
            **kwargs
        )
