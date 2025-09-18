from tools.classes.buff import Buff
from tools.settings import buff_txts


class Dot(Buff):
    skills: dict

    attributes_prefix = "active"

    active_coefficient = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def formulas(self):
        formulas = {}
        for skill_id, skill_levels in self.skills.items():
            formulas[skill_id] = {}
            for skill_level, skill in skill_levels.items():
                formulas[skill_id][skill_level] = skill.to_dict()
        return formulas

    def to_dict(self):
        if self.buff_level:
            return {
                "name": self.get_name(self.buff_id, self.buff_level),
                "comment": self.comment,
                "interval": int(self.interval),
                "max_stack": int(self.max_stack),
                "max_tick": int(self.max_tick),
                "formulas": self.formulas
            }
        else:
            return {}
