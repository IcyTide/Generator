from typing import List, Tuple

from tools.lua.enums import ATTRIBUTE_EFFECT_MODE, ATTRIBUTE_TYPE
from tools.settings import skill_settings, skill_txts
from tools.utils import camel_to_snake


class Skill:
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

    attributes: List[Tuple[str, str, int, int]]
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
        self.attributes = []

    def __getattr__(self, item):
        if item in self._aliases:
            item = self._aliases[item]
        elif item.lower() != item:
            item = camel_to_snake(item)
        if item in dir(self):
            return getattr(self, item)
        else:
            return self.empty_func

    def __getitem__(self, item):
        return getattr(self, item)

    def __setattr__(self, key, value):
        if key in self._aliases:
            key = self._aliases[key]
        elif key.lower() != key:
            key = camel_to_snake(key)
        super().__setattr__(key, value)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def add_attribute(self, attr_effect_mode: ATTRIBUTE_EFFECT_MODE, attr_type: ATTRIBUTE_TYPE, param_1, param_2):
        if not attr_type:
            return
        self.attributes.append(
            (ATTRIBUTE_EFFECT_MODE(attr_effect_mode).name, ATTRIBUTE_TYPE(attr_type).name, param_1, param_2)
        )

    def to_asset(self):
        if self.skill_level:
            txt_rows = skill_txts[(skill_txts['SkillID'] == self.skill_id)]
            default_row = txt_rows[txt_rows['Level'] == 0]
            default_name = default_row.iloc[0]['Name'] if not default_row.empty else ""
            txt_row = txt_rows[txt_rows['Level'] == self.skill_level]
            name = txt_row.iloc[0]['Name'] if not txt_row.empty else default_name
            return {
                "name": name,
                "channel_interval": self.channel_interval,
                "prepare_frames": self.prepare_frames,
                "weapon_damage_percent": self.weapon_damage_percent,
                "attributes": self.attributes
            }
        else:
            return {
                "skill_id": int(self.skill_id),
                "skill_name": self.skill_name,
                "max_level": int(self.max_level),
                "kind_type": self.kind_type,
                "skill_event_mask1": int(self.skill_event_mask1),
                "skill_event_mask2": int(self.skill_event_mask2),
                "recipe_type": int(self.recipe_type),
                "weapon_request": int(self.weapon_request),
                "use_skill_coefficient": int(self.use_skill_coefficient)
            }
