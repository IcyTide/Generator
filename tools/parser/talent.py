from tools.classes.talent import Talent
from tools.lua.engine import Engine


def parse_talent(talent: Talent):
    engine = Engine(talent.script_path)
    talent = Talent(talent.skill_id, talent.max_level, **talent.kwargs)
    engine.get_skill_level_data(talent)
    return talent
