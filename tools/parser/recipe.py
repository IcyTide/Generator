from tools.classes.dot import Dot
from tools.classes.recipe import BuffRecipe, Recipe
from tools.classes.skill import Skill
from tools.lua.engine import Engine


def set_recipe_to_skill(engine: Engine, recipe, skills: dict[int, dict[int, Skill]]):
    buff_recipes = set()
    for skill_id, skill_levels in skills.items():
        for skill_level, skill in skill_levels.items():
            if not recipe.check_skill(skill):
                continue
            skill.recipe_key = recipe.recipe_key
            skill.damage_gain += int(recipe.damage_add_percent) * skill.recipe_key
            if skill.prepare_frames:
                skill.prepare_frames += int(recipe.prepare_frames_add) * skill.recipe_key
            engine.get_skill_recipe_data(skill, recipe.recipe_id, recipe.recipe_level)
            buff_recipes = buff_recipes.union(skill.buff_recipes)
            skill.buff_recipes = set()
    return buff_recipes


def set_recipe_to_buffs(buff_recipe: BuffRecipe, dots: dict[int, dict[int, Dot]]):
    for dot_id, dot_levels in dots.items():
        if dot_id != buff_recipe.buff_id:
            continue
        for dot_level, dot in dot_levels.items():
            if buff_recipe.buff_level and buff_recipe.buff_level != dot_level:
                continue
            dot.interval += int(buff_recipe.interval_frame_add) * buff_recipe.recipe_key


def parse_recipe(recipe: Recipe, skills: dict[int, dict[int, Skill]], dots: dict[int, dict[int, Dot]]):
    engine = Engine(recipe.script_path)
    buff_recipes = set_recipe_to_skill(engine, recipe, skills)
    for dot_id, dot_levels in dots.items():
        for dot_level, dot in dot_levels.items():
            buff_recipes |= set_recipe_to_skill(engine, recipe, dot.skills)
    for buff_recipe_id, buff_recipe_level in buff_recipes:
        buff_recipe = BuffRecipe(recipe.recipe_key, buff_recipe_id, buff_recipe_level)
        set_recipe_to_buffs(buff_recipe, dots)
