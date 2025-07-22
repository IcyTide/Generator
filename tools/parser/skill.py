import os.path

from tools.classes.skill import Skill
from tools.lua.engine import Engine

def parse_skill(skill_id):
    skill = Skill(skill_id)
    skill_data = skill.to_asset()
    engine = Engine()
    engine.execute(os.path.join("scripts", "skill", skill.script_file))
    for skill_level in range(int(skill.max_level)):
        skill, skill.skill_level = Skill(skill_id), skill_level + 1
        engine.run("GetSkillLevelData", skill)
        for k, v in skill.to_asset().items():
            if k not in skill_data:
                skill_data[k] = [type(v)()] * skill_level
            skill_data[k].append(v)
    return skill_data
