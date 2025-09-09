from tqdm import tqdm

from kungfus import SUPPORT_KUNGFUS
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
    def __init__(self):
        self.attributes = {}
        self.buffs = {}
        self.dots = {}
        self.skills = {}
        self.talents = {}
        self.recipes = {}
        for kungfu in SUPPORT_KUNGFUS:
            self.build_attribute(kungfu.attribute)
            self.build_buffs(kungfu.buffs)
            self.build_dots(kungfu.dots)
            self.build_recipes(kungfu.recipes)
            self.build_skills(kungfu.skills)
            self.build_talents(kungfu.talents)

    def build_attribute(self, attribute_id):
        self.attributes[attribute_id] = Talent(attribute_id)

    def build_buffs(self, buffs: dict[str, list[int]]):
        for category, buff_ids in buffs.items():
            for buff_id in buff_ids:
                self.buffs[buff_id] = Buff(buff_id)

    def build_dots(self, dots: dict[str, dict[int, list]]):
        for category, dot_ids in dots.items():
            for dot_id, skill_ids in dot_ids.items():
                dot = self.dots[dot_id] = Dot(dot_id)
                dot.skills = {skill_id: Skill(skill_id) for skill_id in skill_ids}

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

    # def build_recipes(self):
    #     for attribute in self.attributes.values():
    #         for recipe_id, _ in attribute.recipes:
    #             self.recipes[recipe_id] = Recipe(recipe_id)
    #     for buff_id, buffs in self.buffs.items():
    #         for buff_level, buff in buffs.items():
    #             for recipe_id, _ in buff.recipes:
    #                 self.recipes[recipe_id] = Recipe(recipe_id)
    #     for talent in self.talents.values():
    #         for recipe_id, _ in talent.recipes:
    #             self.recipes[recipe_id] = Recipe(recipe_id)
    #     for recipe in self.recipes.values():
    #         recipe.parse_attribute()

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
        for recipe_id, params in tqdm(self.recipes.items()):
            self.recipes[recipe_id] = parse_recipe(recipe_id, self.skills, self.dots)

    def __call__(self):
        self.parse_attribute()
        self.parse_buffs()
        self.parse_dots()
        self.parse_skills()
        self.parse_talents()
        self.parse_recipes()
        save_code("attributes", self.attributes)
        save_code("buffs", self.buffs)
        save_code("dots", self.dots)
        save_code("skills", self.skills)
        save_code("talents", self.talents)
        save_code("recipes", self.recipes)
        return


if __name__ == '__main__':
    builder = Builder()
    builder()
