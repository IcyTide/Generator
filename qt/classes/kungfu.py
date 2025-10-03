from assets.raw.buffs import BUFFS
from assets.raw.dots import DOTS
from assets.raw.skills import SKILLS
from assets.raw.belongs import BELONGS
from qt.classes.attribute import Attribute, Target


class Kungfu:
    source: Attribute
    target: Target

    gear_attributes: dict[str, int]
    gear_recipes: list[str]
    gear_gains: list[str]

    def __init__(self, kungfu):
        self.kungfu_id = kungfu.attribute
        self.attribute = BELONGS[self.kungfu_id][self.kungfu_id]
        self.name = self.attribute["name"]
        self.kind = kungfu.kind
        self.major = kungfu.major
        self.school = kungfu.school
        buffs, dots, skills = kungfu.buffs, kungfu.dots, kungfu.skills
        self.talents = []
        for talents in kungfu.talents:
            self.talents.append({})
            for talent_id, params in talents.items():
                self.talents[-1][talent_id] = BELONGS[self.kungfu_id][talent_id]
                if talent_buffs := params.get("buffs"):
                    buffs[talent_id] = talent_buffs
                if talent_dots := params.get("dots"):
                    dots[talent_id] = talent_dots
                if talent_skills := params.get("skills"):
                    skills[talent_id] = talent_skills

        self.buffs = {
            BELONGS[self.kungfu_id][belong]["name"]: {
                buff_id: BUFFS[self.kungfu_id][buff_id] for buff_id in buff_ids
            } for belong, buff_ids in buffs.items()
        }
        self.skills = {
            BELONGS[self.kungfu_id][belong]["name"]: {
                skill_id: SKILLS[self.kungfu_id][skill_id] for skill_id in skill_ids
            } for belong, skill_ids in skills.items()
        }
        self.dots = {
            BELONGS[self.kungfu_id][belong]["name"]: {
                dot_id: DOTS[self.kungfu_id][dot_id] for dot_id in dot_ids
            }
            for belong, dot_ids in dots.items()
        }

        self.gear_attributes = {}
        self.gear_recipes = []
        self.gear_gains = []

    def create_attribute(self) -> Attribute:
        attributes, recipes, gains = self.attributes
        attribute = Attribute(self.major)
        for k, v in attributes.items():
            attribute[k] += v
        attribute.recipes += recipes
        return attribute

    @property
    def attributes(self):
        attributes = {}
        for k, v in self.attribute.get("attributes", {}).items():
            if k not in attributes:
                attributes[k] = 0
            attributes[k] += v
        for k, v in self.gear_attributes.items():
            if k not in attributes:
                attributes[k] = 0
            attributes[k] += v
        recipes = self.attribute.get("recipes", []) + self.gear_recipes
        gains = self.gear_gains
        return attributes, recipes, gains
