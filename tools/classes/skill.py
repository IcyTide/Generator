from pathlib import Path

from base.constant import BINARY_SCALE, DEFAULT_SURPLUS_COF, DOT_DAMAGE_SCALE, FRAME_PER_SECOND, MAGICAL_DAMAGE_SCALE, \
    PHYSICAL_DAMAGE_SCALE
from base.expression import Expression, Int
from kungfus import SKILL_PATCHES
from tools.classes import AliasBase
from tools.classes.attribute import Attribute, Target
from tools.classes.damage import DamageChain
from tools.lua.enums import ATTRIBUTE_EFFECT_MODE, ATTRIBUTE_TYPE, SKILL_KIND_TYPE
from tools.settings import skill_settings, skill_txts
from tools.utils import camel_to_capital, process_attr_param, set_patches


class Skill(AliasBase):
    txt = skill_txts
    id_column = "SkillID"
    _aliases = {
        "dwSkillID": "skill_id",
        "dwLevel": "skill_level",
        "nHeight": "zero",
        "nAreaRadius": "zero",
        "nBeatBackRate": "zero",
        "nTargetCountLimit": "zero",
        "nChannelFrame": "zero"
    }
    skill_id: int
    skill_level: int = 0
    skill_name: str

    max_level: int
    kind_type: str | SKILL_KIND_TYPE
    weapon_request: int

    recipe_type: int

    self_rollback_attributes: list[tuple[ATTRIBUTE_TYPE, tuple[int, int] | int]]
    dest_rollback_attributes: list[tuple[ATTRIBUTE_TYPE, tuple[int, int] | int]]
    self_attributes: list[tuple[ATTRIBUTE_TYPE, tuple[int, int] | int]]
    dest_attributes: list[tuple[ATTRIBUTE_TYPE, tuple[int, int] | int]]
    buff_recipes: set[tuple[int, int]]

    prepare_frames: int = 0
    channel_interval: int = FRAME_PER_SECOND
    weapon_damage_percent: int = BINARY_SCALE
    weapon_request: bool
    use_skill_coefficient: bool

    damage_addition: int = 0

    skill_coefficient: int = 0
    dot_coefficient: int = 0
    surplus_coefficient: int = 0

    script_file: str
    path: str
    script_path: Path = None

    interval: int = 0
    tick: int = 1
    tick_cof: float = 1.

    levels: list[int] = None
    recipe_key: Expression = None
    comment: str = ""

    @property
    def level(self):
        return self.skill_level

    def __init__(self, skill_id: int, skill_level: int = 0):
        self.skill_id = skill_id
        self.skill_level = skill_level
        setting_row = skill_settings[skill_settings['SkillID'] == self.skill_id].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)
        self.max_level = max(1, self.max_level)
        self.kind_type = SKILL_KIND_TYPE[camel_to_capital(self.kind_type)] if self.kind_type else None  # noqa
        self.self_rollback_attributes, self.dest_rollback_attributes = [], []
        self.self_attributes, self.dest_attributes = [], []
        self.buff_recipes = set()
        if self.script_file:
            self.script_path = Path(self.path) / self.script_file

        set_patches(self, SKILL_PATCHES, skill_id, skill_level)

    def __getattr__(self, item):
        if self.recipe_key and item == "nChannelInterval":
            return 1
        else:
            return super().__getattr__(item)

    def __setattr__(self, key, value):
        if self.recipe_key and key == "nChannelInterval":
            if value < FRAME_PER_SECOND:
                self.channel_interval *= 1 + (value - 1) * self.recipe_key
            else:
                self.channel_interval = self.channel_interval * (1 - self.recipe_key) + value * self.recipe_key
        else:
            super().__setattr__(key, value)

    def add_attribute(self, attr_effect_mode: ATTRIBUTE_EFFECT_MODE, attr_type: ATTRIBUTE_TYPE, param_1, param_2):
        if not attr_type:
            return
        param = process_attr_param(attr_type, param_1, param_2)
        if not param:
            return
        if self.recipe_key:
            param *= self.recipe_key
        if attr_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_SELF_AND_ROLLBACK:
            self.self_rollback_attributes.append((attr_type, param))
        elif attr_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_DEST_AND_ROLLBACK:
            self.dest_rollback_attributes.append((attr_type, param))
        elif attr_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_SELF_NOT_ROLLBACK:
            self.self_attributes.append((attr_type, param))
        elif attr_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_DEST_NOT_ROLLBACK:
            self.dest_attributes.append((attr_type, param))

    def set_buff_recipe(self, index, recipe_id, recipe_level):
        self.buff_recipes.add((recipe_id, recipe_level))

    @property
    def physical_attack_power_cof(self):
        if not self.use_skill_coefficient:
            return 0
        if self.skill_coefficient:
            frames = self.skill_coefficient
        else:
            frames = Int(self.prepare_frames + self.channel_interval * self.tick_cof)
        interval = int(self.interval * self.tick / DOT_DAMAGE_SCALE)
        interval = interval if interval > FRAME_PER_SECOND else FRAME_PER_SECOND
        scale = interval / FRAME_PER_SECOND / self.tick / FRAME_PER_SECOND / PHYSICAL_DAMAGE_SCALE
        return frames * scale

    @property
    def magical_attack_power_cof(self):
        if not self.use_skill_coefficient:
            return 0
        if self.skill_coefficient:
            frames = self.skill_coefficient
        else:
            frames = Int(self.prepare_frames + self.channel_interval * self.tick_cof)
        interval = int(self.interval * self.tick / DOT_DAMAGE_SCALE)
        interval = interval if interval > FRAME_PER_SECOND else FRAME_PER_SECOND
        scale = interval / FRAME_PER_SECOND / self.tick / FRAME_PER_SECOND / MAGICAL_DAMAGE_SCALE
        return frames * scale

    @property
    def weapon_damage_cof(self):
        if not self.use_skill_coefficient:
            return 0
        if not self.weapon_request:
            return 0
        return Int(self.weapon_damage_percent) / BINARY_SCALE

    @property
    def surplus_cof(self):
        if self.surplus_coefficient:
            return self.surplus_coefficient / BINARY_SCALE
        else:
            return DEFAULT_SURPLUS_COF

    @property
    def formula(self):
        source, target = Attribute(), Target()
        damage_chain = target.damage_chain = DamageChain(source, target, self)
        source.need_int = target.need_int = damage_chain.need_int
        for attr, param in self.self_rollback_attributes:
            source[attr] += param
        for attr, param in self.dest_rollback_attributes:
            target[attr] += param
        # self not rollback attributes no meaning
        for attr, param in self.dest_attributes:
            if callable(target[attr]):
                target[attr](*param)
            else:
                target[attr] += param
        return damage_chain.to_dict()

    def to_dict(self):
        if self.skill_level:
            return {
                "name": self.get_name(self.skill_id, self.skill_level),
                "comment": self.comment,
                **self.formula
            }
        else:
            return {}
