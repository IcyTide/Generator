from base.constant import BINARY_SCALE
from base.expression import Ceil, Expression
from tools.classes.buff import Buff
from tools.classes.dot import Dot
from tools.classes.skill import Skill

def is_int(value: float | int):
    return int(value) == value

def set_buff_to_skills(
        buff: Buff, skills: dict[int, dict[int, dict[int, Skill]]], dots: dict[int, dict[int, dict[int, Dot]]]
):
    if not buff.skill_damage_cof and not buff.coming_damage_cof:
        return
    if buff.max_stack == 1:
        buff.skill_damage_cof = Ceil(buff.skill_damage_cof)
        buff.coming_damage_cof = Ceil(buff.coming_damage_cof)
    for category, skill_ids in skills.items():
        for skill_id, skill_levels in skill_ids.items():
            for skill_level, skill in skill_levels.items():
                if not buff.check_skill(skill):
                    continue
                if is_int(buff.skill_damage_cof):
                    skill.skill_damage_cof += buff.skill_damage_cof * buff.buff_key
                else:
                    skill.skill_damage_cof += Ceil(buff.skill_damage_cof * buff.buff_key)
                if is_int(buff.coming_damage_cof):
                    skill.coming_damage_cof += buff.coming_damage_cof * buff.buff_key
                else:
                    skill.coming_damage_cof += Ceil(buff.coming_damage_cof * buff.buff_key)
    for category, dot_ids in dots.items():
        for dot_id, dot_levels in dot_ids.items():
            for dot_level, dot in dot_levels.items():
                if not buff.check_dot(dot):
                    continue
                for skill_id, skill_levels in dot.skills.items():
                    for skill_level, skill in skill_levels.items():
                        if is_int(buff.dot_damage_cof):
                            skill.dot_damage_cof += buff.dot_damage_cof * buff.buff_key
                        else:
                            skill.dot_damage_cof += Ceil(buff.dot_damage_cof * buff.buff_key)


def parse_buff(
        buff: Buff, skills: dict[int, dict[int, dict[int, Skill]]], dots: dict[int, dict[int, dict[int, Dot]]]
) -> dict[int, Buff]:
    result = {}
    for buff_level in buff.levels:
        buff = Buff(buff.buff_id, buff_level, patches=buff.patches)
        set_buff_to_skills(buff, skills, dots)
        result[buff_level] = buff
    return result
