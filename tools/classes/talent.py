from tools.classes.skill import Skill
from tools.lua.enums import ATTRIBUTE_TYPE
from tools.settings import skill_txts


class Talent(Skill):
    def to_asset(self):
        if self.skill_level:
            return {
                "name": self.get_name(skill_txts, "SkillID", self.skill_id, self.skill_level),
                "recipes": [
                    (param_1, param_2) for attr, param_1, param_2 in self.self_rollback_attributes
                    if attr == ATTRIBUTE_TYPE.SET_TALENT_RECIPE.name
                ]
            }
        else:
            return {
                "skill_name": self.skill_name,
            }
