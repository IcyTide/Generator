from base.expression import Variable
from tools.classes.skill import Skill
from tools.classes.dot import Dot
from tools.parser.skill import parse_skill


def parse_dot(dot: Dot):
    result = {}
    for buff_level in dot.levels:
        dot = Dot(dot.buff_id, buff_level, dot.patches)
        skill_ids: dict[int, Skill] = {
            skill_id: Skill(skill_id, patches=patches) for skill_id, patches in dot.skills.items()
        }
        for skill_id in skill_ids:
            dot.skills[skill_id] = skill_levels = parse_skill(skill_ids[skill_id])
            for skill_level, skill in skill_levels.items():
                skill.dest_rollback_attributes, skill.dest_attributes = [], dot.attributes
                skill.interval, skill.tick = dot.interval, dot.max_tick
                skill.tick_cof = dot.active_coefficient ** (Variable("tick") - 1)
        result[buff_level] = dot
    return result
