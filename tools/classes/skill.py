from pathlib import Path

from base.constant import BINARY_SCALE, FRAME_PER_SECOND, MAGICAL_DAMAGE_SCALE, PHYSICAL_DAMAGE_SCALE
from base.damage import DamageChain
from base.expression import Expression
from tools.classes import AliasBase
from tools.classes.attribute import Attribute, Target
from tools.lua.enums import ATTRIBUTE_EFFECT_MODE, ATTRIBUTE_TYPE, SKILL_KIND_TYPE
from tools.settings import skill_settings, skill_txts
from tools.utils import camel_to_capital


class Skill(AliasBase):
    _aliases = {
        "dwSkillID": "skill_id",
        "dwLevel": "skill_level"
    }
    skill_id: int
    skill_level: int = 0
    skill_name: str

    max_level: int
    kind_type: str | SKILL_KIND_TYPE
    weapon_request: int

    recipe_type: int

    self_rollback_attributes: list[tuple[ATTRIBUTE_TYPE, int, int]]
    dest_rollback_attributes: list[tuple[ATTRIBUTE_TYPE, int, int]]
    self_attributes: list[tuple[ATTRIBUTE_TYPE, int, int]]
    dest_attributes: list[tuple[ATTRIBUTE_TYPE, int, int]]

    prepare_frames: int = 0
    channel_interval: int = FRAME_PER_SECOND
    weapon_damage_percent: int = BINARY_SCALE
    weapon_request: bool
    use_skill_coefficient: bool

    damage_addition: int = 0

    script_file: str
    path: str
    script_path: Path = None

    interval: int = 0
    tick: int = 1

    recipe_key: Expression = None

    def __init__(self, skill_id: int, skill_level: int = 0):
        self.skill_id = skill_id
        self.skill_level = skill_level
        setting_row = skill_settings[skill_settings['SkillID'] == self.skill_id].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)
        self.kind_type = SKILL_KIND_TYPE[camel_to_capital(self.kind_type)] if self.kind_type else None  # noqa
        self.self_rollback_attributes, self.dest_rollback_attributes = [], []
        self.self_attributes, self.dest_attributes = [], []
        if self.script_file:
            self.script_path = Path(self.path) / self.script_file

    def __setattr__(self, key, value):
        if self.recipe_key and key in ("channel_interval",):
            super().__setattr__(key, value * self.recipe_key + getattr(self, key) * (1 - self.recipe_key))
        else:
            super().__setattr__(key, value)

    def add_attribute(self, attr_effect_mode: ATTRIBUTE_EFFECT_MODE, attr_type: ATTRIBUTE_TYPE, param_1, param_2):
        if not attr_type:
            return
        param_1 = 0 if not param_1 else int(param_1)
        param_2 = 0 if not param_2 else int(param_2)
        if self.recipe_key:
            param_1 *= self.recipe_key
            param_2 *= self.recipe_key
        if attr_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_SELF_AND_ROLLBACK:
            self.self_rollback_attributes.append((attr_type, param_1, param_2))
        elif attr_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_DEST_AND_ROLLBACK:
            self.dest_rollback_attributes.append((attr_type, param_1, param_2))
        elif attr_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_SELF_NOT_ROLLBACK:
            self.self_attributes.append((attr_type, param_1, param_2))
        elif attr_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_DEST_NOT_ROLLBACK:
            self.dest_attributes.append((attr_type, param_1, param_2))

    @property
    def physical_attack_power_cof(self):
        if not self.use_skill_coefficient:
            return 0
        frames = self.prepare_frames + self.channel_interval
        interval = self.interval if self.interval > FRAME_PER_SECOND else FRAME_PER_SECOND
        return frames * interval / FRAME_PER_SECOND / self.tick / FRAME_PER_SECOND / PHYSICAL_DAMAGE_SCALE

    @property
    def magical_attack_power_cof(self):
        if not self.use_skill_coefficient:
            return 0
        frames = self.prepare_frames + self.channel_interval
        interval = self.interval if self.interval > FRAME_PER_SECOND else FRAME_PER_SECOND
        return frames * interval / FRAME_PER_SECOND / self.tick / FRAME_PER_SECOND / MAGICAL_DAMAGE_SCALE

    @property
    def weapon_damage_cof(self):
        if not self.use_skill_coefficient:
            return 0
        if not self.weapon_request:
            return 0
        return self.weapon_damage_percent

    @property
    def formula(self):
        source, target = Attribute(), Target()
        damage_chain = target.damage_chain = DamageChain(source, target, self)
        for attr, param_1, param_2 in self.self_rollback_attributes:
            source[attr] += param_2 if param_2 else param_1
        for attr, param_1, param_2 in self.dest_rollback_attributes:
            target[attr] += param_2 if param_2 else param_1
        # self not rollback attributes no meaning
        for attr, param_1, param_2 in self.dest_attributes:
            if callable(target[attr]):
                target[attr](param_1, param_2)
            else:
                target[attr] += param_2 if param_2 else param_1
        return damage_chain.to_dict()

    def to_dict(self):
        if self.skill_level:
            return {
                "name": self.get_name(skill_txts, "SkillID", self.skill_id, self.skill_level),
                **self.formula
            }
        else:
            return {}
