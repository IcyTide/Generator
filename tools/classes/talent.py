from tools.classes.skill import Skill
from tools.lua.enums import ATTRIBUTE_EFFECT_MODE, ATTRIBUTE_TYPE
from tools.utils import get_variable


class Talent(Skill):
    buffs: list[int] = []
    dots: dict[int, list[int]] = {}
    skills: list[int] = []

    recipes: list[tuple[int, int]]

    critical_type: str = ""
    damage_type: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.recipes = []
        self.kwargs = kwargs
        for k, v in kwargs.items():
            setattr(self, k, v)

    def add_attribute(self, attr_effect_mode: ATTRIBUTE_EFFECT_MODE, attr_type: ATTRIBUTE_TYPE, param_1, param_2):
        if attr_type == ATTRIBUTE_TYPE.SKILL_EVENT_HANDLER:
            pass
        elif attr_type == ATTRIBUTE_TYPE.SET_ADAPTIVE_SKILL_TYPE:
            self.critical_type = param_1
            self.damage_type = param_2
        elif attr_type == ATTRIBUTE_TYPE.SET_TALENT_RECIPE:
            self.recipes.append((int(param_1), int(param_2)))
        else:
            super().add_attribute(attr_effect_mode, attr_type, param_1, param_2)

    def to_dict(self):
        if self.skill_level:
            return {
                "name": self.get_name(self.skill_id, self.skill_level),
                "attributes": {attr: param for attr, param in self.self_rollback_attributes},
                "recipes": [get_variable(recipe_id, recipe_level) for recipe_id, recipe_level in self.recipes],
                "buffs": self.buffs,
                "dots": self.dots,
                "skills": self.skills,
                "desc": self.get_desc(self.skill_id, self.skill_level),
                "critical_type": self.critical_type,
                "damage_type": self.damage_type
            }
        else:
            return {}
