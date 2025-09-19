from tools.classes.buff import Buff


class Dot(Buff):
    skills: dict
    attributes_prefix = "active"

    active_coefficient = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
                "name": self.get_name(self.buff_id, self.buff_level),
                "comment": self.comment,
                "interval": int(self.interval),
                "max_stack": int(self.max_stack),
                "max_tick": int(self.max_tick),
                "skills": self.sources
            }
        else:
            return {}
