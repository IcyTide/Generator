from tools.classes.belong import Belong
from tools.classes.skill import Skill
from tools.lua.engine import Engine

def set_belong_to_skill(belong: Belong, skills: dict[int, dict[int, Skill]]):
    if not belong.dest_rollback_attributes:
        return
    for skill_id, skill_levels in skills.items():
        for skill_level, skill in skill_levels.items():
            if not belong.check_skill(skill):
                continue
            for attr, value in belong.dest_rollback_attributes:
                skill.dest_rollback_attributes.append((attr, value * belong.belong_key))


def parse_belong(belong: Belong, skills: dict[int, dict[int, Skill]]):
    engine = Engine(belong.script_path)
    engine.get_skill_level_data(belong)
    set_belong_to_skill(belong, skills)
    return belong
