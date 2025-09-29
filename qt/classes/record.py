from dataclasses import dataclass
from typing import List

from qt.classes.buff import Buff
from qt.classes.dot import Dot
from qt.classes.skill import Skill


@dataclass
class Record:
    name: str = "New Record"
    count: int = 1

    buffs: List[Buff] = None
    skills: List[Skill] = None
    dots: List[Dot] = None

    def __post_init__(self):
        if not self.buffs:
            self.buffs = []
        if not self.skills:
            self.skills = []
        if not self.dots:
            self.dots = []

    def __iter__(self):
        for attr in ("name", "count"):
            yield str(getattr(self, attr))

    def to_dict(self):
        return dict(
            name=self.name, count=self.count,
            buffs=[buff.to_dict() for buff in self.buffs],
            skills=[skill.to_dict() for skill in self.skills],
            dots=[dot.to_dict() for dot in self.dots]
        )

    @classmethod
    def from_dict(cls, json):
        record = cls(
            json["name"], json["count"],
            [Buff.from_dict(buff) for buff in json["buffs"]],
            [Skill.from_dict(skill) for skill in json["skills"]],
            [Dot.from_dict(dot) for dot in json["dots"]]
        )
        return record