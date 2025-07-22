from assets.raw.skills import SKILLS


class Skill:
    skill_id: int
    skill_level: int
    count: int
    max_count: int

    max_level: int = 1

    kind_type: int
    weapon_request: int = 0
    use_skill_coefficient: int = 0

    skill_event_mask_1: int = 0
    skill_event_mask_2: int = 0

    recipe_type: int = 0

    _attributes: list[list[tuple[str, int, int]]] = []
    _prepare_frames: list[int] = []
    _channel_interval: list[float] = []
    _weapon_damage_percent: list[int] = []

    damage_add_percent: int = 0

    def __init__(self, skill_id: int, skill_level: int = 1, count: int = 1):
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.count = count
        for k, v in SKILLS[self.skill_id].items():
            setattr(self, k, v)

    @property
    def attributes(self):
        if self.skill_level > len(self._attributes):
            return self._attributes[-1]
        else:
            return self._attributes[self.skill_level - 1]

    @attributes.setter
    def attributes(self, value):
        self._attributes = value

    @property
    def prepare_frames(self):
        if self.skill_level > len(self._prepare_frames):
            return self._prepare_frames[-1]
        else:
            return self._prepare_frames[self.skill_level - 1]

    @prepare_frames.setter
    def prepare_frames(self, value):
        self._prepare_frames = value

    @property
    def channel_interval(self):
        if self.skill_level > len(self._attributes):
            return self._attributes[-1]
        else:
            return self._attributes[self.skill_level - 1]

    @channel_interval.setter
    def channel_interval(self, value):
        self._channel_interval = value

    @property
    def weapon_damage_percent(self):
        if self.skill_level > len(self._attributes):
            return self._attributes[-1]
        else:
            return self._attributes[self.skill_level - 1]

    @weapon_damage_percent.setter
    def weapon_damage_percent(self, value):
        self._weapon_damage_percent = value

    def __iter__(self):
        for attr in ("skill_id", "skill_level", "count",):
            yield str(getattr(self, attr))

    def __str__(self):
        return "-".join(iter(self))

    @classmethod
    def from_str(cls, value: str):
        return cls(*(int(e) for e in value.split("-")))
