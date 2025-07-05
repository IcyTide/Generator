from dataclasses import dataclass
from enum import StrEnum


class BuffType(StrEnum):
    Self = "Self"
    Target = "Target"
    Snapshot = "Snapshot"


@dataclass
class Buff:
    id: int
    level: int = 1
    stack: int = 1
    type: BuffType = BuffType.Self

    max_level: int = 1
    max_stack: int = 1

    def __iter__(self):
        for attr in ("type", "id", "level", "stack",):
            yield str(getattr(self, attr))