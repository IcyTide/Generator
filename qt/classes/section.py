from dataclasses import dataclass
from typing import List

from qt.classes.record import Record


@dataclass
class Section:
    name: str = "New Section"
    count: int = 1
    duration: float = 0.

    records: List[Record] = None

    def __post_init__(self):
        if not self.records:
            self.records = [Record()]

    def __iter__(self):
        for attr in ("name", "count", "duration"):
            yield str(getattr(self, attr))

    @property
    def is_empty(self):
        if not self.count:
            return True
        for record in self.records:
            if not record.is_empty:
                return False
        return True

    def copy(self):
        return Section(
            self.name,
            self.count,
            self.duration,
            [record.copy() for record in self.records]
        )

    def to_dict(self):
        return dict(
            name=self.name,
            count=self.count,
            duration=self.duration,
            records=[record.to_dict() for record in self.records]
        )

    @classmethod
    def from_dict(cls, kungfu_id: int, json: dict):
        section = cls(
            json["name"],
            json["count"],
            json["duration"],
            [Record.from_dict(kungfu_id, record) for record in json["records"]]
        )
        return section


class Sections:
    def __init__(self, sections: list[Section] = None):
        if not sections:
            self.sections = []
        else:
            self.sections = sections

    def __setitem__(self, key, value):
        self.sections[key] = value

    def __getitem__(self, key):
        return self.sections[key]

    def __iter__(self):
        for section in self.sections:
            yield section

    def __len__(self):
        return len(self.sections)

    def append(self, item):
        self.sections.append(item)

    def remove(self, item):
        self.sections.remove(item)

    @property
    def is_empty(self):
        for section in self.sections:
            if not section.is_empty:
                return False
        return True

    @property
    def duration(self):
        return sum(section.duration * section.count for section in self.sections)

    def copy(self):
        return Sections([section.copy() for section in self.sections])

    def to_dict(self):
        return [section.to_dict() for section in self.sections]

    @classmethod
    def from_dict(cls, kungfu_id: int, json: list):
        return cls([
            Section.from_dict(kungfu_id, section) for section in json
        ])
