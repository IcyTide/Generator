from base.constant import DOT_DAMAGE_SCALE
from base.skill import Skill
from tools.classes.dot import Dot
from tools.parser.skill import parse_skill


def parse_dot(dot: Dot):
    result = {}
    skill_ids: dict[int, Skill] = dot.skills
    for buff_level in range(1, int(dot.max_level) + 1):
        dot, dot.skills = Dot(dot.buff_id, buff_level), {}
        for skill_id in skill_ids:
            dot.skills[skill_id] = skill_levels = parse_skill(skill_ids[skill_id])
            for skill_level, skill in skill_levels.items():
                skill.dest_rollback_attributes, skill.dest_attributes = [], dot.attributes
                skill.interval, skill.tick = int(dot.interval * dot.max_tick / DOT_DAMAGE_SCALE), dot.max_tick
        result[buff_level] = dot
    return result
