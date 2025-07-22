from parser.buff import parse_buff
from parser.skill import parse_skill
from parser.dot import parse_dot
from parser.talent import parse_talent
from parser.recipe import parse_recipe


from assets.annotate.buffs import BUFFS
from assets.annotate.skills import SKILLS
from assets.annotate.recipes import RECIPES
from kungfus import SUPPORT_KUNGFUS
from tools.settings import recipe_txts
from tools.utils import save_code


class Builder:
    def __init__(self):
        self.buffs = {}
        self.skills = {}
        self.dots = {}
        self.talents = {}
        self.recipes = {}
        for kungfu_id, kungfu in SUPPORT_KUNGFUS.items():
            self.build_buffs(kungfu.buffs)
            self.build_skills(kungfu.skills)
            self.build_dots(kungfu.dots)
            self.build_talents(kungfu.talents)

    def build_buffs(self, buffs: dict[str, list[int]]):
        for category, buff_ids in buffs.items():
            for buff_id in buff_ids:
                self.buffs[buff_id] = BUFFS.get(buff_id, {})

    def build_dots(self, dots: dict[str, dict[int, tuple[list[int], list[int]]]]):
        for category, params in dots.items():
            for dot_id, (source_list, consume_list) in params.items():
                self.dots[dot_id] = dict(
                    source_list=source_list,
                    consume_list=consume_list,
                    **BUFFS.get(dot_id, {})
                )
                for skill_id in source_list + consume_list:
                    self.skills[skill_id] = SKILLS.get(skill_id, {})

    def build_skills(self, skills: dict[str, list[int]]):
        for category, skill_ids in skills.items():
            for skill_id in skill_ids:
                self.skills[skill_id] = SKILLS.get(skill_id, {})

    def build_talents(self, talents: list[dict[int, dict]]):
        for talent_items in talents:
            for talent_id, param in talent_items.items():
                self.talents[talent_id] = SKILLS.get(talent_id, {})
                self.build_dots({"talents": param.get("dots", {})})
                self.build_buffs({"talents": param.get("buffs", [])})
                self.build_skills({"talents": param.get("skills", [])})

    @staticmethod
    def parse_items(items, parse_func, *args):
        for item_id, params in items.items():
            items[item_id] = {}
            for k, v in parse_func(item_id, *args).items():
                if not v:
                    continue
                if not isinstance(v, list):
                    items[item_id][k] = v
                    continue
                if not any(v):
                    continue
                if all(e == v[0] for e in v):
                    items[item_id][k] = [v[0]]
                else:
                    items[item_id][k] = v
            for k, v in params.items():
                items[item_id][k] = v


    def build_recipes(self):
        for buff in self.buffs.values():
            for recipe in buff.get("recipes", []):
                for recipe_id, recipe_level in recipe:
                    if recipe_id not in self.recipes:
                        self.recipes[recipe_id] = {}
                    self.recipes[recipe_id][recipe_level] = RECIPES.get(recipe_id, {}).get(recipe_level, {})
        for talent in self.talents.values():
            for recipe in talent.get("recipes", []):
                for recipe_id, recipe_level in recipe:
                    if recipe_id not in self.recipes:
                        self.recipes[recipe_id] = {}
                    self.recipes[recipe_id][recipe_level] = RECIPES.get(recipe_id, {}).get(recipe_level, {})


    def __call__(self):
        self.parse_items(self.buffs, parse_buff)
        self.parse_items(self.skills, parse_skill)
        self.parse_items(self.dots, parse_dot)
        self.parse_items(self.talents, parse_talent)
        self.build_recipes()
        save_code("buffs", {**self.buffs, **self.dots})
        save_code("skills", {**self.skills, **self.talents})
        self.parse_items(self.recipes, parse_recipe, self.recipes)
        save_code("recipes", self.recipes)



if __name__ == '__main__':
    builder = Builder()
    builder()
