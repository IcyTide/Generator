from assets.raw.skills import SKILLS
from base.expression import Expression
from base.utils import parse_expr


class Skill:
    belong: str
    skill_id: int
    skill_level: int
    count: float

    name: str = ""
    comment: str = ""
    damages: list[str | Expression] = []
    critical_strike: str | Expression = ""
    critical_power: str | Expression = ""
    attributes: dict[str, int] = {}

    def __init__(self, belong: str, skill_id: int, skill_level: int, count: float = 1., **kwargs):
        self.belong = belong
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.count = count
        self.kwargs = kwargs
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.damages = [parse_expr(damage) for damage in self.damages]
        self.critical_strike = parse_expr(self.critical_strike)
        self.critical_power = parse_expr(self.critical_power)

    def __iter__(self):
        yield str(self)
        yield str(self.skill_id)
        yield str(self.skill_level)
        yield str(self.count)

    def __str__(self):
        if self.name and self.comment:
            return f"{self.name}({self.comment})"
        elif self.name:
            return self.name
        elif self.comment:
            return self.comment
        return f"{self.skill_id}-{self.skill_level}"

    def copy(self):
        return Skill(self.belong, self.skill_id, self.skill_level, self.count, **self.kwargs)

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
            if json["skill_id"] in SKILLS[kungfu_id]:
                kwargs = SKILLS[kungfu_id][json["skill_id"]][json["skill_level"]]
            else:
                kwargs = SKILLS[0][json["skill_id"]][json["skill_level"]]
        return cls(
            belong=json["belong"],
            skill_id=json["skill_id"],
            skill_level=json["skill_level"],
            count=json["count"],
            **kwargs
        )
