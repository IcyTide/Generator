from base.expression import Variable
from tools.classes.skill import Skill
from tools.lua.enums import ATTRIBUTE_EFFECT_MODE, ATTRIBUTE_TYPE
from tools.settings import recipe_txts
from tools.utils import get_variable, process_attr_param


class Belong(Skill):
    buffs: list[int] = []
    dots: dict[int, list[int]] = {}
    skills: list[int] = []

    recipes: list[tuple[int, int]]

    dest_rollback_skills: list[int] = []

    critical_type: str = ""
    damage_type: str = ""

    def __init__(self, *args, **kwargs):
        self.dest_rollback_skills = []
        super().__init__(*args, **kwargs)
        self.recipes = []
        self.buffs, self.skills, self.dots = [], [], {}
        self.belong_key = Variable(get_variable("belong", self.skill_id))
        txt_rows = recipe_txts[recipe_txts.SkillID == self.skill_id]
        for row in txt_rows.itertuples():
            self.recipes.append((row.ID, row.Level))
        self.skill_level = self.max_level

    def check_skill(self, skill: Skill):
        return skill.skill_id in self.dest_rollback_skills

    def add_attribute(self, attr_effect_mode: ATTRIBUTE_EFFECT_MODE, attr_type: ATTRIBUTE_TYPE, param_1, param_2):
        if not attr_type:
            return
        if attr_type == ATTRIBUTE_TYPE.SKILL_EVENT_HANDLER:
            pass
        elif attr_type == ATTRIBUTE_TYPE.SET_ADAPTIVE_SKILL_TYPE:
            self.critical_type = param_1
            self.damage_type = param_2
        elif attr_type == ATTRIBUTE_TYPE.SET_TALENT_RECIPE:
            self.recipes.append((int(param_1), int(param_2)))
        elif attr_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_SELF_AND_ROLLBACK:
            param = process_attr_param(attr_type, param_1, param_2)
            self.self_rollback_attributes.append((attr_type, param))

    def to_dict(self):
        if self.skill_level:
            return {
                "name": self.name or self.get_name(self.skill_id, self.skill_level) or self.skill_name,
                "attributes": {attr: param for attr, param in self.self_rollback_attributes},
                "recipes": [get_variable("recipe", *keys) for keys in self.recipes],
                "buffs": self.buffs,
                "dots": self.dots,
                "skills": self.skills,
                "desc": self.get_desc(self.skill_id, self.skill_level),
                "critical_type": self.critical_type,
                "damage_type": self.damage_type,
                "belong_key": str(self.belong_key)
            }
        else:
            return {}
