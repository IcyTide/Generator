from tqdm import tqdm

from kungfus import Kungfu, SUPPORT_KUNGFUS
from parser.buff import parse_buff
from parser.dot import parse_dot
from parser.skill import parse_skill
from tools.classes.buff import Buff
from tools.classes.dot import Dot
from tools.classes.recipe import Recipe
from tools.classes.skill import Skill
from tools.classes.talent import Talent
from tools.parser.recipe import parse_recipe
from tools.parser.talent import parse_talent
from tools.utils import save_code


class Builder:
    @property
    def attributes(self):
        return self.all_attributes[self.kungfu.name]

    @property
    def buffs(self):
        return self.all_buffs[self.kungfu.name]

    @property
    def dots(self):
        return self.all_dots[self.kungfu.name]

    @property
    def skills(self):
        return self.all_skills[self.kungfu.name]

    @property
    def talents(self):
        return self.all_talents[self.kungfu.name]

    @property
    def recipes(self):
        return self.all_recipes[self.kungfu.name]

    def __init__(self):
        self.all_attributes = {}
        self.all_buffs = {}
        self.all_dots = {}
        self.all_skills = {}
        self.all_talents = {}
        self.all_recipes = {}
        for kungfu in SUPPORT_KUNGFUS:
            self.kungfu: Kungfu = kungfu
            print(f"Start parsing {kungfu.name}")
            self.init_all()
            self.build_all()
            self.parse_all()

    def init_all(self):
        self.all_attributes[self.kungfu.name] = {}
        self.all_buffs[self.kungfu.name] = {}
        self.all_dots[self.kungfu.name] = {}
        self.all_skills[self.kungfu.name] = {}
        self.all_talents[self.kungfu.name] = {}
        self.all_recipes[self.kungfu.name] = {}

    def build_all(self):
        self.build_attribute(self.kungfu.attribute)
        self.build_buffs(self.kungfu.buffs)
        self.build_dots(self.kungfu.dots)
        self.build_recipes(self.kungfu.recipes)
        self.build_skills(self.kungfu.skills)
        self.build_talents(self.kungfu.talents)

    def build_attribute(self, attribute_id):
        self.attributes[attribute_id] = Talent(attribute_id)

    def build_buffs(self, buffs: dict[str, list[int]]):
        for category, buff_ids in buffs.items():
            for buff_id in buff_ids:
                self.buffs[buff_id] = Buff(buff_id)

    def build_dots(self, dots: dict[str, dict[int, list]]):
        for category, dot_ids in dots.items():
            for dot_id, skill_ids in dot_ids.items():
                skills = {skill_id: Skill(skill_id) for skill_id in skill_ids}
                if dot_id in self.dots:
                    dot = self.dots[dot_id]
                    dot.skills.update(skills)
                else:
                    dot = self.dots[dot_id] = Dot(dot_id)
                    dot.skills = skills

    def build_skills(self, skills: dict[str, list[int]]):
        for category, skill_ids in skills.items():
            for skill_id in skill_ids:
                self.skills[skill_id] = Skill(skill_id)

    def build_talents(self, talents: list[dict[int, dict]]):
        for talent_items in talents:
            for talent_id, params in talent_items.items():
                talent = self.talents[talent_id] = Talent(talent_id, **params)
                self.build_buffs(dict(talents=talent.buffs))
                self.build_dots(dict(talents=talent.dots))
                self.build_skills(dict(talents=talent.skills))

    def build_recipes(self, recipes: dict[str, list[int]]):
        for category, recipe_ids in recipes.items():
            for recipe_id in recipe_ids:
                self.recipes[recipe_id] = Recipe(recipe_id)

    def parse_all(self):
        self.parse_attribute()
        self.parse_buffs()
        self.parse_dots()
        self.parse_skills()
        self.parse_talents()
        self.parse_recipes()

    def parse_attribute(self):
        for attribute_id, attribute in tqdm(self.attributes.items()):
            attribute = self.attributes[attribute_id] = parse_talent(attribute)
            self.build_recipes(dict(attribute=[recipe_id for recipe_id, _ in attribute.recipes]))

    def parse_buffs(self):
        for buff_id, buff in tqdm(self.buffs.items()):
            buffs = self.buffs[buff_id] = parse_buff(buff)
            for buff_level, item in buffs.items():
                self.build_recipes(dict(buffs=[recipe_id for recipe_id, _ in item.recipes]))

    def parse_dots(self):
        for dot_id, dot in tqdm(self.dots.items()):
            self.dots[dot_id] = parse_dot(dot)

    def parse_skills(self):
        for skill_id, skill in tqdm(self.skills.items()):
            self.skills[skill_id] = parse_skill(skill)

    def parse_talents(self):
        for talent_id, talent in tqdm(self.talents.items()):
            talent = self.talents[talent_id] = parse_talent(talent)
            self.build_recipes(dict(talent=[recipe_id for recipe_id, _ in talent.recipes]))

    def parse_recipes(self):
        for recipe_id, recipe in tqdm(self.recipes.items()):
            self.recipes[recipe_id] = parse_recipe(recipe, self.skills, self.dots)

    def save(self):
        save_code("attributes", {k: v for attribute in self.all_attributes.values() for k, v in attribute.items()})
        save_code("buffs", {k: v for buff in self.all_buffs.values() for k, v in buff.items()})
        save_code("dots", {k: v for dot in self.all_dots.values() for k, v in dot.items()})
        save_code("skills", {k: v for skill in self.all_skills.values() for k, v in skill.items()})
        save_code("talents", {k: v for talent in self.all_talents.values() for k, v in talent.items()})
        save_code("recipes", {k: v for recipe in self.all_recipes.values() for k, v in recipe.items()})


if __name__ == '__main__':
    builder = Builder()
    builder.save()
