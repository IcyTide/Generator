from typing import Dict

from base.skill import Skill
from kungfus import first

class Kungfu:
    skills: Dict[int, Skill]

    def __init__(self, kungfu_id, name, kungfu):
        self.kungfu_id = kungfu_id
        self.name = name

        self.build_skills(kungfu)

    def build_skills(self, kungfu):
        self.skills = {}
        for category, params in kungfu.SKILLS.items():
            for param in params:
                if isinstance(param, tuple):
                    skill_id, attrs = param
                else:
                    skill_id = param
                self.skills[skill_id] = skill = Skill(skill_id)


SUPPORT_KUNGFUS = {
    1: Kungfu(1, "first", first),
}