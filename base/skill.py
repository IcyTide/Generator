from assets.raw.skills import SKILLS


class Skill:
    skill_id: int
    skill_level: int

    max_level: int = 1

    kind_type: int
    weapon_request: int = 0

    skill_event_mask_1: int = 0
    skill_event_mask_2: int = 0

    recipe_type: int = 0

    _attributes: list[list[tuple[str, int, int]]] = []
    _prepare_frames: list[int] = []
    _min_prepare_frames: list[float] = []
    _weapon_damage_percent: list[int] = []

    damage_add_percent: int = 0

    def __init__(self, skill_id: int, skill_level: int = 1, ):
        self.skill_id = skill_id
        self.skill_level = skill_level
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
    def weapon_damage_percent(self):
        if self.skill_level > len(self._attributes):
            return self._attributes[-1]
        else:
            return self._attributes[self.skill_level - 1]

    @weapon_damage_percent.setter
    def weapon_damage_percent(self, value):
        self._weapon_damage_percent = value
