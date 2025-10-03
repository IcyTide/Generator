from dataclasses import dataclass
from typing import List

from qt.classes.record import Record


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

    def to_dict(self):
        return dict(
            name=self.name,
            count=self.count,
            records=[record.to_dict() for record in self.records]
        )

    @classmethod
    def from_dict(cls, kungfu_id: int, json: dict):
        section = cls(
            json["name"],
            json["count"],
            [Record.from_dict(kungfu_id, record) for record in json["records"]]
        )
        return section
