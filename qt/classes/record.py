from dataclasses import dataclass
from typing import List

from qt.classes.buff import Buff
from qt.classes.dot import Dot
from qt.classes.skill import Skill


@dataclass
class Record:
    name: str = "New Record"
    count: int = 1
    duration: float = 0.

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
        for attr in ("name", "count", "duration"):
            yield str(getattr(self, attr))

    @property
    def is_empty(self):
        if not self.count:
            return True
        if self.skills or self.dots:
            return False
        return True

    def copy(self):
        return Record(
            self.name, self.count, self.duration,
            [buff.copy() for buff in self.buffs],
            [skill.copy() for skill in self.skills],
            [dot.copy() for dot in self.dots]
        )

    def to_dict(self):
        return dict(
            name=self.name, count=self.count, duration=self.duration,
            buffs=[buff.to_dict() for buff in self.buffs],
            skills=[skill.to_dict() for skill in self.skills],
            dots=[dot.to_dict() for dot in self.dots]
        )

    @classmethod
    def from_dict(cls, kungfu_id: int, json: dict):
        record = cls(
            json["name"], json["count"], json["duration"],
            [Buff.from_dict(kungfu_id, buff) for buff in json["buffs"]],
            [Skill.from_dict(kungfu_id, skill) for skill in json["skills"]],
            [Dot.from_dict(kungfu_id, dot) for dot in json["dots"]]
        )
        return record
