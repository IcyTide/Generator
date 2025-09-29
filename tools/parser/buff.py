from tools.classes.buff import Buff
from tools.classes.skill import Skill
from tools.lua.enums import ATTRIBUTE_EFFECT_MODE


def set_buff_to_skill(buff: Buff, skills: dict[int, dict[int, Skill]]):
    if not buff.skills:
        return
    for skill_id, skill_levels in skills.items():
        for skill_level, skill in skill_levels.items():
            if not buff.check_skill(skill):
                continue
            for attr, value in buff.attributes:
                skill.dest_rollback_attributes.append((attr, value * buff.buff_key))


def parse_buff(buff: Buff, skills: dict[int, dict[int, Skill]]) -> dict[int, Buff]:
    result = {}
    for buff_level in buff.levels:
        buff = Buff(buff.buff_id, buff_level)
        set_buff_to_skill(buff, skills)
        result[buff_level] = buff
    return result
