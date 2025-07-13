import os.path

from kungfus import SUPPORT_KUNGFUS
from tools.classes.skill import Skill
from tools.lua.engine import Engine
from tools.utils import save_code


def get_all_skills():
    skills = []
    for kungfu in SUPPORT_KUNGFUS.values():
        for skill_id in kungfu.skills:
            if skill_id in skills:
                continue
            skills.append(skill_id)
    return skills


def parse_skill(skill_id):
    skill = Skill(skill_id)
    skill_data = {**skill.to_asset()}
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

def parse_skills():
    data = {}
    for skill_id in get_all_skills():
        data[skill_id] = {}
        for k, v in parse_skill(skill_id).items():
            if not isinstance(v, list):
                data[skill_id][k] = v
                continue
            if not any(v):
                continue
            if all(e == v[0] for e in v):
                data[skill_id][k] = v[0]
            else:
                data[skill_id][k] = v
    save_code("skills", data)


if __name__ == '__main__':
    parse_skills()