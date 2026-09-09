from base.expression import Expression
from tools.classes.buff import Buff
from tools.classes.dot import Dot
from tools.classes.skill import Skill


def set_buff_to_skills(
        buff: Buff, skills: dict[int, dict[int, dict[int, Skill]]], dots: dict[int, dict[int, dict[int, Dot]]]
):
    if not buff.skills and not buff.dots:
        return
    for category, skill_ids in skills.items():
        for skill_id, skill_levels in skill_ids.items():
            for skill_level, skill in skill_levels.items():
                if not buff.check_skill(skill):
                    continue
                skill.coming_damage_cof += buff.coming_damage_cof * buff.buff_key
    for category, dot_ids in dots.items():
        for dot_id, dot_levels in dot_ids.items():
            for dot_level, dot in dot_levels.items():
                if not buff.check_dot(dot):
                    continue
                for skill_id, skill_levels in dot.skills.items():
                    for skill_level, skill in skill_levels.items():
                        skill.damage_cof += buff.damage_cof * buff.buff_key


def parse_buff(
        buff: Buff, skills: dict[int, dict[int, dict[int, Skill]]], dots: dict[int, dict[int, dict[int, Dot]]]
) -> dict[int, Buff]:
    result = {}
    for buff_level in buff.levels:
        buff = Buff(buff.buff_id, buff_level, patches=buff.patches)
        set_buff_to_skills(buff, skills, dots)
        result[buff_level] = buff
    return result
