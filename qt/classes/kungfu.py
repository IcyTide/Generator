from assets.raw.attributes import ATTRIBUTES
from assets.raw.buffs import BUFFS
from assets.raw.dots import DOTS
from assets.raw.skills import SKILLS
from assets.raw.talents import TALENTS
from kungfus import Kungfu
from qt.classes.attribute import Attribute, Target


class DisplayKungfu:
    source: Attribute
    target: Target

    gear_attributes: dict[str, int]
    gear_recipes: list[str]
    gear_gains: list[str]

    def __init__(self, kungfu: Kungfu):
        self.kungfu_id = kungfu.attribute
        self.attribute = ATTRIBUTES[self.kungfu_id]
        self.name = self.attribute["name"]
        self.kind = kungfu.kind
        self.major = kungfu.major
        self.school = kungfu.school
        buffs, dots, skills = kungfu.buffs, kungfu.dots, kungfu.skills
        self.talents = {}
        for talents in kungfu.talents:
            for talent_id, params in talents.items():
                talent = self.talents[talent_id] = TALENTS[self.kungfu_id][talent_id]
                talent_name = talent["name"]
                if talent_buffs := talent.get("buffs"):
                    buffs[talent_name] = talent_buffs
                if talent_dots := talent.get("dots"):
                    dots[talent_name] = talent_dots
                if talent_skills := talent.get("skills"):
                    skills[talent_name] = talent_skills
        self.buffs = {
            belong: {buff_id: BUFFS[self.kungfu_id][buff_id] for buff_id in buff_ids}
            for belong, buff_ids in buffs.items()
        }
        self.skills = {
            belong: {skill_id: SKILLS[self.kungfu_id][skill_id] for skill_id in skill_ids}
            for belong, skill_ids in skills.items()
        }
        self.dots = {
            belong: {dot_id: DOTS[self.kungfu_id][dot_id] for dot_id in dot_ids}
            for belong, dot_ids in dots.items()
        }

        self.gear_attributes = {}
        self.gear_recipes = []

    def create_attribute(self) -> Attribute:
        attribute = Attribute(self.major)
        for k, v in self.attributes.items():
            attribute[k] += v
        attribute.recipes += self.recipes
        return attribute

    @property
    def attributes(self):
        ret = {}
        for k, v in self.attribute.get("attributes", {}).items():
            if k not in ret:
                ret[k] = 0
            ret[k] += v
        for k, v in self.gear_attributes.items():
            if k not in ret:
                ret[k] = 0
            ret[k] += v
        return ret

    @property
    def recipes(self):
        return self.attribute.get("recipes", []) + self.gear_recipes

    @property
    def gains(self):
        return self.gear_gains