from dataclasses import dataclass
from typing import List

from base.buff import Buff
from base.dot import Dot
from base.record import Record
from base.skill import Skill


@dataclass
class Section:
    name: str = "New Section"
    count: int = 1

    records: List[Record] = None

    def __post_init__(self):
        if not self.records:
            self.records = [Record()]

    def __iter__(self):
        for attr in ("name", "count"):
            yield str(getattr(self, attr))