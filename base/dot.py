from assets.raw.buffs import BUFFS
from base.skill import Skill


class Dot:
    dot_id: int
    dot_level: int = 1
    count: int = 1

    source: Skill = None
    consume: Skill = None

    source_list: list[int] = None
    consume_list: list[int] = None

    max_level: int = 1
    max_stack: int = 1
    max_tick: int = 1

    @property
    def stack(self):
        return self.source.count

    @property
    def tick(self):
        return self.consume.count if self.consume else 1

    def __init__(self, dot_id, dot_level: int = 1, count: int = 1):
        self.dot_id = dot_id
        self.dot_level = dot_level
        self.count = count
        for k, v in BUFFS[self.dot_id].items():
            setattr(self, k, v)
    def __iter__(self):
        for attr in ("dot_id", "dot_level", "source", "consume", "count"):
            if value := getattr(self, attr):
                yield str(value)
            else:
                yield ""