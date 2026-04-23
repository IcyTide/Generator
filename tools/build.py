import logging

from tqdm import tqdm

from gains import GAIN
from kungfus import Kungfu, SUPPORT_KUNGFUS
from tools.classes.belong import Belong
from tools.classes.buff import Buff
from tools.classes.dot import Dot
from tools.classes.recipe import Recipe
from tools.classes.skill import Skill
from tools.parser.belong import parse_belong
from tools.parser.buff import parse_buff
from tools.parser.dot import parse_dot
from tools.parser.recipe import parse_recipe
from tools.parser.skill import parse_skill
from tools.utils import save_code, save_json

logging.basicConfig(level=logging.INFO)


class Builder:
    @property
    def buffs(self):
        return self.all_buffs[self.kungfu.kungfu_id]

    @property
    def dots(self):
        return self.all_dots[self.kungfu.kungfu_id]

    @property
    def skills(self):
        return self.all_skills[self.kungfu.kungfu_id]

    @property
    def belongs(self):
        return self.all_belongs[self.kungfu.kungfu_id]

    @property
    def recipes(self):
        return self.all_recipes[self.kungfu.kungfu_id]

    @property
    def skill_recipes(self):
        return self.all_skill_recipes[self.kungfu.kungfu_id]

    def __init__(self):
        self.all_buffs = {}
        self.all_dots = {}
        self.all_skills = {}
        self.all_belongs = {}
        self.all_recipes = {}
        self.all_skill_recipes = {}
        for kungfu in SUPPORT_KUNGFUS + [GAIN]:
            self.kungfu: Kungfu = kungfu
            logging.info(f"Start parsing {kungfu.kungfu_id}")
            self.init_all()
            self.build_all()
            self.parse_all()

    def init_all(self):
        self.all_buffs[self.kungfu.kungfu_id] = {}
        self.all_dots[self.kungfu.kungfu_id] = {}
        self.all_skills[self.kungfu.kungfu_id] = {}
        self.all_belongs[self.kungfu.kungfu_id] = {}
        self.all_recipes[self.kungfu.kungfu_id] = {}
        self.all_skill_recipes[self.kungfu.kungfu_id] = {}

    def build_all(self):
        if self.kungfu.kungfu_id:
            self.belongs[self.kungfu.kungfu_id] = Belong(self.kungfu.kungfu_id)
        self.build_buffs(self.kungfu.buffs)
        self.build_dots(self.kungfu.dots)
        self.build_skills(self.kungfu.skills)
        self.build_talents(self.kungfu.talents)
        self.build_recipes(self.kungfu.recipes)

    def build_buffs(self, buffs: dict[int, dict[int, dict]], build_skill_recipes: bool = True):
        for category, buff_ids in buffs.items():
            if category not in self.belongs:
                self.belongs[category] = Belong(category)
            if category not in self.buffs:
                self.buffs[category] = {}
            if build_skill_recipes:
                self.skill_recipes[category] = self.belongs[category]
            for buff_id, patches in buff_ids.items():
                self.buffs[category][buff_id] = Buff(buff_id, patches=patches)

    def build_dots(self, dots: dict[int, dict[int, dict]], build_skill_recipes: bool = True):
        for category, dot_ids in dots.items():
            if category not in self.belongs:
                self.belongs[category] = Belong(category)
            if category not in self.dots:
                self.dots[category] = {}
            if build_skill_recipes:
                self.skill_recipes[category] = self.belongs[category]
            for dot_id, patches in dot_ids.items():
                self.dots[category][dot_id] = Dot(dot_id, patches=patches)

    def build_skills(self, skills: dict[int, dict[int, dict]], build_skill_recipes: bool = True):
        for category, skill_ids in skills.items():
            if category not in self.belongs:
                self.belongs[category] = Belong(category)
            if category not in self.skills:
                self.skills[category] = {}
            if build_skill_recipes:
                self.skill_recipes[category] = self.belongs[category]
            for skill_id, patches in skill_ids.items():
                self.skills[category][skill_id] = Skill(skill_id, patches=patches)

    def build_talents(self, talents: list[dict[int, dict]]):
        for talent_items in talents:
            for talent_id, params in talent_items.items():
                if buffs := params.pop("buffs", {}):
                    self.build_buffs({talent_id: buffs}, False)
                if skills := params.pop("skills", {}):
                    self.build_skills({talent_id: skills}, False)
                if dots := params.pop("dots", {}):
                    self.build_dots({talent_id: dots}, False)
                self.belongs[talent_id] = Belong(talent_id, patches=params)

    def build_recipes(self, recipes: list[tuple[int, int]]):
        for recipe_key in recipes:
            self.recipes[recipe_key] = Recipe(*recipe_key)

    def parse_all(self):
        self.parse_dots()
        self.parse_skills()
        self.parse_buffs()
        self.parse_belongs()
        self.parse_recipes()
        self.parse_skill_recipes()

    def parse_buffs(self):
        for category, buff_ids in tqdm(self.buffs.items()):
            for buff_id, buff in tqdm(buff_ids.items()):
                buffs = self.buffs[category][buff_id] = parse_buff(buff, self.skills)
                for sub_buff in buffs.values():
                    self.build_recipes(sub_buff.recipes)

    def parse_dots(self):
        for category, dot_ids in tqdm(self.dots.items()):
            for dot_id, dot in tqdm(dot_ids.items()):
                self.dots[category][dot_id] = parse_dot(dot)

    def parse_skills(self):
        for category, skill_ids in tqdm(self.skills.items()):
            for skill_id, skill in tqdm(skill_ids.items()):
                self.skills[category][skill_id] = parse_skill(skill)

    def parse_belongs(self):
        for belong_id, belong in tqdm(self.belongs.items()):
            belong = self.belongs[belong_id] = parse_belong(belong, self.skills)
            self.build_recipes(belong.recipes)

    def parse_recipes(self):
        for recipe in tqdm(self.recipes.values()):
            parse_recipe(recipe, self.skills, self.dots)

    def parse_skill_recipes(self):
        pop_skills = [self.kungfu.kungfu_id]
        for skill_id, belong in tqdm(self.skill_recipes.items()):
            if belong.recipes:
                self.skill_recipes[skill_id] = [self.recipes[recipe_key] for recipe_key in belong.recipes]
            else:
                pop_skills.append(skill_id)
        for skill_id in pop_skills:
            self.skill_recipes.pop(skill_id, None)

    @staticmethod
    def build_skill_code(skill_ids: dict[int, dict[int, Skill]]):
        code = {}
        for skill_id, skill_levels in skill_ids.items():
            code[skill_id] = {}
            for skill_level, item in skill_levels.items():
                content = code[skill_id][skill_level] = item.to_dict()
                if damages := content.pop('damages', []):
                    content['damages'] = [damage['damage'] for damage in damages]
                if critical := content.pop('critical', {}):
                    content['critical_strike'] = critical['critical_strike']
                    content['critical_power'] = critical['critical_power']
                content.pop('skill_attribute', None)
        return code

    @property
    def dot_code(self):
        code = {}
        for kungfu_id, dots in self.all_dots.items():
            code[kungfu_id] = {}
            for category, dot_ids in dots.items():
                code[kungfu_id][category] = {}
                for dot_id, dot_levels in dot_ids.items():
                    code[kungfu_id][category][dot_id] = {}
                    for dot_level, item in dot_levels.items():
                        content = code[kungfu_id][category][dot_id][dot_level] = item.to_dict()
                        content['skills'] = self.build_skill_code(item.skills)
        return code

    @property
    def skill_code(self):
        code = {}
        for kungfu_id, skills in self.all_skills.items():
            code[kungfu_id] = {}
            for category, skill_ids in skills.items():
                code[kungfu_id][category] = self.build_skill_code(skill_ids)
        return code

    def save(self):
        save_code("buffs", self.all_buffs),
        save_json("buffs", self.all_buffs)
        save_code("dots", self.dot_code),
        save_json("dots", self.all_dots)
        save_code("skills", self.skill_code),
        save_json("skills", self.all_skills)
        save_code("belongs", self.all_belongs),
        save_json("belongs", self.all_belongs)
        save_code("recipes", self.all_skill_recipes)
        save_json("recipes", self.all_skill_recipes)


if __name__ == '__main__':
    builder = Builder()
    builder.save()
