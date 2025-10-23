from tools.classes.skill import Skill
from tools.lua.engine import Engine


def parse_skill(skill: Skill) -> dict[int, Skill]:
    result = {}
    engine = Engine(skill.script_path)
    for skill_level in skill.levels:
        skill = Skill(skill.skill_id, skill_level, patches=skill.patches)
        engine.get_skill_level_data(skill)
        result[skill_level] = skill
    return result
