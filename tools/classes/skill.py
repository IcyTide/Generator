from tools.classes import AliasBase
from tools.lua.enums import ATTRIBUTE_EFFECT_MODE, ATTRIBUTE_TYPE
from tools.settings import skill_settings, skill_txts


class Skill(AliasBase):
    _aliases = {
        "dwSkillID": "skill_id",
        "dwLevel": "skill_level"
    }
    skill_id: int
    skill_level: int = 0
    skill_name: str

    max_level: int
    kind_type: int
    weapon_request: int
    use_skill_coefficient: int

    skill_event_mask_1: int
    skill_event_mask_2: int

    recipe_type: int

    script_file: str

    self_rollback_attributes: list[tuple[str, int, int]]
    self_attributes: list[tuple[str, int, int]]
    dest_rollback_attributes: list[tuple[str, int, int]]
    dest_attributes: list[tuple[str, int, int]]

    channel_interval: float = 0.
    prepare_frames: int = 0
    weapon_damage_percent: int = 0

    @staticmethod
    def empty_func(*args):
        return

    def __init__(self, skill_id):
        self.skill_id = skill_id
        setting_row = skill_settings[skill_settings['SkillID'] == self.skill_id].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)
        self.self_rollback_attributes = []
        self.self_attributes = []
        self.dest_rollback_attributes = []
        self.dest_attributes = []

    def add_attribute(self, attr_effect_mode: ATTRIBUTE_EFFECT_MODE, attr_type: ATTRIBUTE_TYPE, param_1, param_2):
        if not attr_type:
            return
        attribute = (ATTRIBUTE_TYPE(attr_type).name, param_1, param_2)
        if attr_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_SELF_AND_ROLLBACK:
            self.self_rollback_attributes.append(attribute)
        elif attr_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_SELF_NOT_ROLLBACK:
            self.self_attributes.append(attribute)
        elif attr_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_DEST_AND_ROLLBACK:
            self.dest_rollback_attributes.append(attribute)
        elif attr_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_DEST_NOT_ROLLBACK:
            self.dest_attributes.append(attribute)

    def to_asset(self):
        if self.skill_level:
            return {
                "name": self.get_name(skill_txts, "SkillID", self.skill_id, self.skill_level),
                "channel_interval": self.channel_interval,
                "prepare_frames": self.prepare_frames,
                "weapon_damage_percent": self.weapon_damage_percent,
                "self_rollback_attributes": self.self_rollback_attributes,
                "self_attributes": self.self_attributes,
                "dest_rollback_attributes": self.dest_rollback_attributes,
                "dest_attributes": self.dest_attributes
            }
        else:
            return {
                "skill_name": self.skill_name,
                "max_level": int(self.max_level),
                "kind_type": self.kind_type,
                "skill_event_mask1": int(self.skill_event_mask1),
                "skill_event_mask2": int(self.skill_event_mask2),
                "recipe_type": int(self.recipe_type),
                "weapon_request": int(self.weapon_request),
                "use_skill_coefficient": int(self.use_skill_coefficient)
            }
