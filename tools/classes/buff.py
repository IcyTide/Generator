from kungfus import BUFF_PATCHES
from tools.classes import AliasBase
from tools.lua.enums import ATTRIBUTE_TYPE
from tools.settings import buff_settings, buff_txts
from tools.utils import camel_to_capital, get_variable, set_patches


class Buff(AliasBase):
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

    max_stack: int
    max_tick: int
    interval: int

    attributes: list[tuple[ATTRIBUTE_TYPE, int, int]] = []
    recipes: list[tuple[int, int]] = []

    attributes_prefix: str = "begin"

    levels: list[int]
    skills: list[int]
    name: str = ""
    comments: dict[int, str] = None
    comment: str = ""

    @property
    def level(self):
        return self.buff_level

    def __init__(self, buff_id: int, buff_level: int = 0):
        self.buff_id = buff_id
        self.setting_rows = buff_settings[buff_settings['ID'] == self.buff_id]
        self.max_level = self.setting_rows["Level"].max()
        self.attributes = []
        self.recipes = []
        self.skills = []
        if buff_level:
            self.buff_level = buff_level
            setting_row = self.setting_rows[self.setting_rows["Level"] == self.buff_level].iloc[0]
            for k, v in setting_row.items():
                setattr(self, k, v)
            self.get_attributes(self.attributes_prefix)

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
            param_1 = 0 if not param_1 else int(param_1)
            param_2 = 0 if not param_2 else int(param_2)
            if attr_type == ATTRIBUTE_TYPE.SET_TALENT_RECIPE:
                self.recipes.append((param_1, param_2))
            else:
                self.attributes.append((attr_type, param_1, param_2))

    def to_dict(self):
        if self.buff_level:
            return {
                "name": self.name or self.get_name(buff_txts, "BuffID", self.buff_id, self.buff_level),
                "comment": self.comment,
                "skills": self.skills,
                "interval": int(self.interval),
                "max_stack": int(self.max_stack),
                "max_tick": int(self.max_tick),
                "attributes": {attr: param_1 or param_2 for attr, param_1, param_2 in self.attributes},
                "recipes": [get_variable(recipe_id, recipe_level) for recipe_id, recipe_level in self.recipes]
            }
        else:
            return {}
