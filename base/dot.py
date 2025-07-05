from dataclasses import dataclass

from base.skill import Skill


@dataclass
class Dot:
    id: int
    level: int = 1
    count: int = 1

    source: Skill = None
    consume: Skill = None

    max_level: int = 1
    max_stack: int = 1
    max_tick: int = 1

    @property
    def stack(self):
        return self.source.count

    @property
    def tick(self):
        return self.consume.count if self.consume else 1

    def __iter__(self):
        for attr in ("id", "level", "source", "consume", "count"):
            if value := getattr(self, attr):
                yield str(value)
            else:
                yield ""