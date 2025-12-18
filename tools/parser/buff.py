from ....base.expression import Expression
from tools.classes.buff import Buff
from tools.classes.skill import Skill


def set_buff_to_skill(buff: Buff, skills: dict[int, dict[int, Skill]]):
    if not buff.skills:
        return
    for skill_id, skill_levels in skills.items():
        for skill_level, skill in skill_levels.items():
            if not buff.check_skill(skill):
                continue
            for attr, value in buff.attributes:
                if isinstance(value, Expression):
                    value = value.evaluate(dict(buff_key=buff.buff_key))
                else:
                    value = value * buff.buff_key
                skill.dest_rollback_attributes.append((attr, value))


def parse_buff(buff: Buff, skills: dict[int, dict[int, Skill]]) -> dict[int, Buff]:
    result = {}
    for buff_level in buff.levels:
        buff = Buff(buff.buff_id, buff_level, patches=buff.patches)
        set_buff_to_skill(buff, skills)
        result[buff_level] = buff
    return result
