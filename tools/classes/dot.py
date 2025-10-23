from tools.classes.buff import Buff
from tools.classes.skill import Skill


class Dot(Buff):
    skills: dict
    attributes_prefix = "active"

    active_coefficient = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = {}

    @property
    def sources(self):
        sources = {}
        for skill_id, skill_levels in self.skills.items():
            sources[skill_id] = {}
            for skill_level, skill in skill_levels.items():
                sources[skill_id][skill_level] = skill.to_dict()
        return sources

    def to_dict(self):
        if self.buff_level:
            return {
                "name": f"{self.get_name(self.buff_id, self.buff_level)}(DOT)",
                "comment": self.comment,
                "interval": str(self.interval),
                "max_stack": int(self.max_stack),
                "max_tick": int(self.max_tick),
                "skills": self.sources
            }
        else:
            return {}
