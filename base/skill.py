from dataclasses import dataclass


@dataclass
class Skill:
    id: int
    level: int = 1
    count: int = 1

    max_level: int = 1
    max_count: int = 0

    def __iter__(self):
        for attr in ("id", "level", "count",):
            yield str(getattr(self, attr))

    def __str__(self):
        return "-".join(iter(self))

    def _set_asset(self):
        pass

    @classmethod
    def from_str(cls, value: str):
        return cls(*(int(e) for e in value.split("-")))