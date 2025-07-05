from dataclasses import dataclass
from typing import List

from base.buff import Buff
from base.dot import Dot
from base.skill import Skill


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