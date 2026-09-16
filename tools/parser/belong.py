from base.expression import Ceil
from tools.classes.belong import Belong
from tools.classes.skill import Skill
from tools.lua.engine import Engine


def set_belong_to_skill(belong: Belong, skills: dict[int, dict[int, dict[int, Skill]]]):
    if not belong.skill_damage_cof and belong.coming_damage_cof:
        return
    belong.skill_damage_cof = Ceil(belong.skill_damage_cof)
    belong.coming_damage_cof = Ceil(belong.coming_damage_cof)
    for category, skill_ids in skills.items():
        for skill_id, skill_levels in skill_ids.items():
            for skill_level, skill in skill_levels.items():
                if not belong.check_skill(skill):
                    continue
                skill.skill_damage_cof += belong.skill_damage_cof * belong.belong_key
                skill.coming_damage_cof += belong.coming_damage_cof * belong.belong_key


def parse_belong(belong: Belong, skills: dict[int, dict[int, dict[int, Skill]]]):
    engine = Engine(belong.script_path)
    engine.get_skill_level_data(belong)
    set_belong_to_skill(belong, skills)
    return belong
