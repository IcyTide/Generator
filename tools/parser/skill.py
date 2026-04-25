from tools.classes.skill import Skill
from tools.lua.engine import Engine


def parse_skill(skill: Skill) -> dict[int, Skill]:
    result = {}
    if skill.custom_damage_source:
        engine = Engine()
        for skill_level in skill.levels:
            skill = Skill(skill.skill_id, skill_level, patches=skill.patches)
            skill.custom_damage_base = engine.get_custom_damages(skill.custom_damage_source)[skill_level - 1]
            result[skill_level] = skill
    else:
        engine = Engine(skill.script_path)
        for skill_level in skill.levels:
            skill = Skill(skill.skill_id, skill_level, patches=skill.patches)
            engine.get_skill_level_data(skill)
            result[skill_level] = skill
    return result
