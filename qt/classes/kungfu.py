from assets.raw.belongs import BELONGS
from assets.raw.buffs import BUFFS
from assets.raw.dots import DOTS
from assets.raw.recipes import RECIPES
from assets.raw.skills import SKILLS
from base.constant import MAJOR_TYPES
from qt.classes.attribute import Attribute, Target


class Kungfu:
    source: Attribute
    target: Target

    gear_attributes: dict[str, int] = {}
    gear_recipes: list[str] = []
    gear_gains: list[str] = []

    build_attributes: dict[str, int] = {}
    build_recipes: list[str] = []
    build_gains: list[str] = []

    select_talents: list[str] = []

    def __init__(self, kungfu):
        self.kungfu_id = kungfu.attribute
        self.attribute = BELONGS[self.kungfu_id][self.kungfu_id]
        self.name = self.attribute["name"]
        self.kind = kungfu.kind
        self.major = kungfu.major
        self.school = kungfu.school
        self.id2belong = {belong_id: belong["name"] for belong_id, belong in BELONGS[self.kungfu_id].items()}
        self.belong2id = {v: k for k, v in self.id2belong.items()}
        self.talents = []
        self.talent_buffs, self.talent_skills, self.talent_dots = {}, {}, {}
        for talents in kungfu.talents:
            self.talents.append({})
            for talent_id, params in talents.items():
                self.talents[-1][self.id2belong[talent_id]] = BELONGS[self.kungfu_id][talent_id]
                belong = self.id2belong[talent_id]
                if buffs := params.get("buffs"):
                    self.talent_buffs[belong] = {buff_id: BUFFS[self.kungfu_id][buff_id] for buff_id in buffs}
                if skills := params.get("skills"):
                    self.talent_skills[belong] = {skill_id: SKILLS[self.kungfu_id][skill_id] for skill_id in skills}
                if dots := params.get("dots"):
                    self.talent_dots[belong] = {dot_id: DOTS[self.kungfu_id][dot_id] for dot_id in dots}
        self.kungfu_buffs = {
            self.id2belong[belong_id]: {buff_id: BUFFS[self.kungfu_id][buff_id] for buff_id in buff_ids}
            for belong_id, buff_ids in kungfu.buffs.items()
        }
        self.kungfu_skills = {
            self.id2belong[belong_id]: {skill_id: SKILLS[self.kungfu_id][skill_id] for skill_id in skill_ids}
            for belong_id, skill_ids in kungfu.skills.items()
        }
        self.kungfu_dots = {
            self.id2belong[belong_id]: {dot_id: DOTS[self.kungfu_id][dot_id] for dot_id in dot_ids}
            for belong_id, dot_ids in kungfu.dots.items()
        }
        self.recipes = {
            self.id2belong[belong_id]: recipes for belong_id, recipes in RECIPES[self.kungfu_id].items()
        }

    def create_attribute(self, require_grad: bool = True) -> Attribute:
        attributes, recipes, gains = self.attributes
        attribute = Attribute(MAJOR_TYPES[self.major], self.attribute["damage_type"], self.attribute["critical_type"])
        for k, v in attributes.items():
            attribute[k] += v
        attribute.recipes += recipes
        if require_grad:
            attribute.require_grad()
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
        for k, v in self.build_attributes.items():
            if k not in attributes:
                attributes[k] = 0
            attributes[k] += v
        recipes = self.attribute.get("recipes", []) + self.gear_recipes + self.build_recipes
        gains = self.gear_gains + self.build_gains
        return attributes, recipes, gains

    @property
    def buffs(self):
        return {**self.kungfu_buffs, **{k: v for k, v in self.talent_buffs.items() if k in self.select_talents}}

    @property
    def skills(self):
        return {**self.kungfu_skills, **{k: v for k, v in self.talent_skills.items() if k in self.select_talents}}

    @property
    def dots(self):
        return {**self.kungfu_dots, **{k: v for k, v in self.talent_dots.items() if k in self.select_talents}}
