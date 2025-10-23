from tools.classes.belong import Belong
from tools.lua.engine import Engine


def parse_belong(belong: Belong):
    engine = Engine(belong.script_path)
    belong = Belong(belong.skill_id, belong.max_level, patches=belong.patches)
    engine.get_skill_level_data(belong)
    return belong
