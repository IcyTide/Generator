from tools.classes.skill import Skill
from tools.lua.enums import ATTRIBUTE_EFFECT_MODE, ATTRIBUTE_TYPE
from tools.settings import skill_txts


class Talent(Skill):
    buffs: list[int] = []
    skills: list[int] = []
    dots: dict[int, list[int]] = {}

    recipes: list[tuple[int, int]]

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.recipes = []
        for k, v in kwargs.items():
            setattr(self, k, v)

    def add_attribute(self, attr_effect_mode: ATTRIBUTE_EFFECT_MODE, attr_type: ATTRIBUTE_TYPE, param_1, param_2):
        if attr_type == ATTRIBUTE_TYPE.SET_TALENT_RECIPE:
            self.recipes.append((int(param_1), int(param_2)))
        else:
            super().add_attribute(attr_effect_mode, attr_type, param_1, param_2)

    def to_dict(self):
        if self.skill_level:
            return {
                "name": self.get_name(skill_txts, "SkillID", self.skill_id, self.skill_level),
                "attributes": [(attr, param_1 or param_2) for attr, param_1, param_2 in self.self_rollback_attributes],
                "recipes": self.recipes
            }
        else:
            return {}
