from base.expression import Variable
from tools.classes.dot import Dot
from tools.classes.recipe import Recipe
from tools.classes.skill import Skill
from tools.lua.engine import Engine


def set_recipe_to_skill(engine: Engine, recipe, skills: dict[int, dict[int, Skill]]):
    for skill_id, skill_levels in skills.items():
        for skill_level, skill in skill_levels.items():
            if not recipe.check_skill(skill):
                continue
            skill.recipe_key = Variable(recipe.recipe_key)
            if not skill.interval:
                skill.damage_addition += int(recipe.damage_add_percent) * skill.recipe_key
            skill.prepare_frames += int(recipe.prepare_frames_add) * skill.recipe_key
            engine.get_skill_recipe_data(skill, recipe.recipe_id, recipe.recipe_level)


def parse_recipe(recipe: Recipe, skills: dict[int, dict[int, Skill]], dots: dict[int, dict[int, Dot]]):
    result = {}
    for recipe_level in recipe.levels:
        recipe = result[recipe_level] = Recipe(recipe.recipe_id, recipe_level)
        engine = Engine(recipe.script_path)
        set_recipe_to_skill(engine, recipe, skills)
        for dot_id, dot_levels in dots.items():
            for dot_level, dot in dot_levels.items():
                set_recipe_to_skill(engine, recipe, dot.skills)
    return result
