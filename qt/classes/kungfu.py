from assets.raw.belongs import BELONGS
from assets.raw.buffs import BUFFS
from assets.raw.dots import DOTS
from assets.raw.recipes import RECIPES
from assets.raw.skills import SKILLS
from base.constant import MAJOR_TYPES
from gains import GAIN
from qt.classes.attribute import Attribute, Target
from qt.classes.gain import Gain


class Kungfu:
    source: Attribute
    target: Target

    gear_attributes: dict[str, int] = {}
    gear_recipes: list[str] = []
    gains: dict[str, Gain] = {}

    build_attributes: dict[str, int] = {}
    build_recipes: list[str] = []
    talents: dict[str, str] = {}

    set_gain_attribute: bool = True

    def __init__(self, kungfu):
        self.kungfu_id = kungfu.attribute
        self.attribute = BELONGS[self.kungfu_id][self.kungfu_id]
        self.name = self.attribute["name"]
        self.kind = kungfu.kind
        self.major = kungfu.major
        self.school = kungfu.school
        self.id2belong = {belong_id: belong["name"] for belong_id, belong in BELONGS[self.kungfu_id].items()}
        self.belong2id = {v: k for k, v in self.id2belong.items()}

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

        self.talent_choices = []
        self.talent_buffs, self.talent_skills, self.talent_dots = {}, {}, {}
        for talents in kungfu.talents:
            self.talent_choices.append({})
            for talent_id, params in talents.items():
                self.talent_choices[-1][self.id2belong[talent_id]] = BELONGS[self.kungfu_id][talent_id]
                belong = self.id2belong[talent_id]
                if buffs := params.get("buffs"):
                    self.talent_buffs[belong] = {buff_id: BUFFS[self.kungfu_id][buff_id] for buff_id in buffs}
                if skills := params.get("skills"):
                    self.talent_skills[belong] = {skill_id: SKILLS[self.kungfu_id][skill_id] for skill_id in skills}
                if dots := params.get("dots"):
                    self.talent_dots[belong] = {dot_id: DOTS[self.kungfu_id][dot_id] for dot_id in dots}

        self.recipe_choices = {
            self.id2belong[belong_id]: recipes for belong_id, recipes in RECIPES[self.kungfu_id].items()
        }

    def create_attribute(self, require_grad: bool = True) -> Attribute:
        attributes = self.attributes
        attribute = Attribute(MAJOR_TYPES[self.major], self.attribute["damage_type"], self.attribute["critical_type"])
        for k, v in attributes.items():
            attribute[k] += v
        if self.set_gain_attribute:
            for gain in self.gains.values():
                gain.set_attribute(attribute)
        attribute.recipes += self.recipes
        attribute.belongs += list(self.talents.values())
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
        return attributes

    @property
    def recipes(self):
        return self.attribute.get("recipes", []) + self.gear_recipes + self.build_recipes

    @property
    def buffs(self):
        return {
            **self.kungfu_buffs,
            **{k: v for k, v in self.talent_buffs.items() if k in self.talents},
            "装备": {buff_id: BUFFS[0][buff_id] for gain in self.gains.values() for buff_id in gain.buffs}
        }

    @property
    def skills(self):
        return {
            **self.kungfu_skills,
            **{k: v for k, v in self.talent_skills.items() if k in self.talents},
            "装备": {skill_id: SKILLS[0][skill_id] for gain in self.gains.values() for skill_id in gain.skills}
        }

    @property
    def dots(self):
        return {
            **self.kungfu_dots,
            **{k: v for k, v in self.talent_dots.items() if k in self.talents},
            "装备": {dot_id: DOTS[0][dot_id] for gain in self.gains.values() for dot_id in gain.dots}
        }
