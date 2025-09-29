from base.expression import Variable
from kungfus import BUFF_PATCHES
from tools.classes import AliasBase
from tools.classes.skill import Skill
from tools.lua.enums import ATTRIBUTE_TYPE
from tools.settings import buff_settings, buff_txts
from tools.utils import camel_to_capital, get_variable, process_attr_param, set_patches


class Buff(AliasBase):
    txt = buff_txts
    id_column = "BuffID"
    _aliases = {
        "Name": "buff_name",
        "Level": "buff_level",
        "MaxStackNum": "max_stack",
        "Count": "max_tick"
    }
    buff_id: int
    buff_level: int = 0

    max_level: int

    is_stackable: bool
    is_countable: bool

    max_stack: int = 1
    max_tick: int = 0
    interval: int = 0

    attributes_prefix: str = "begin"

    levels: list[int]

    attributes: list[tuple[ATTRIBUTE_TYPE, int]]
    recipes: list[tuple[int, int]]
    coming_damage_cof: int = 0
    skills: list[int]
    name: str = ""
    comments: dict[int, str] = None
    comment: str = ""

    @property
    def level(self):
        return self.buff_level

    def __init__(self, buff_id: int, buff_level: int = 0):
        self.buff_id = buff_id
        self.attributes, self.recipes, self.skills = [], [], []
        setting_rows = buff_settings[buff_settings['ID'] == self.buff_id]
        self.max_level = setting_rows["Level"].max()
        if buff_level:
            self.buff_level = buff_level
            setting_row = setting_rows[setting_rows["Level"] == self.buff_level].iloc[0]
            for k, v in setting_row.items():
                setattr(self, k, v)
            self.get_attributes(self.attributes_prefix)
            self.buff_key = Variable(get_variable("buff", self.buff_id, self.buff_level))

        set_patches(self, BUFF_PATCHES, buff_id, buff_level)

    def get_attributes(self, prefix):
        i = 0
        while hasattr(self, f'{prefix}_attrib{i + 1}'):
            i += 1
            attr = getattr(self, f'{prefix}_attrib{i}')
            if not attr or attr == self.empty_func:
                break
            attr = camel_to_capital(attr[2:])
            attr_type = ATTRIBUTE_TYPE[attr]  # noqa
            if not attr_type:
                continue
            param_1, param_2 = getattr(self, f'{prefix}_value{i}_a'), getattr(self, f'{prefix}_value{i}_b')
            if attr_type == ATTRIBUTE_TYPE.SKILL_EVENT_HANDLER:
                pass
            elif attr_type == ATTRIBUTE_TYPE.SET_TALENT_RECIPE:
                self.recipes.append((int(param_1), int(param_2)))
            elif param := process_attr_param(attr_type, param_1, param_2):
                self.attributes.append((attr_type, param))

    def check_skill(self, skill: Skill):
        return skill.skill_id in self.skills

    def to_dict(self):
        if self.buff_level:
            return {
                "name": self.name or self.get_name(self.buff_id, self.buff_level),
                "comment": self.comment,
                "interval": int(self.interval),
                "max_stack": int(self.max_stack),
                "max_tick": int(self.max_tick),
                "attributes": {attr: param for attr, param in self.attributes},
                "recipes": [get_variable("recipe", *keys) for keys in self.recipes],
                "skills": self.skills,
                "buff_key": str(self.buff_key)
            }
        else:
            return {}
