import os.path

from tools.classes.talent import Talent
from tools.lua.engine import Engine


def parse_talent(talent_id):
    talent = Talent(talent_id)
    talent_data = talent.to_asset()
    engine = Engine()
    engine.execute(os.path.join("scripts", "skill", talent.script_file))
    talent.skill_level = talent.max_level
    engine.run("GetSkillLevelData", talent)
    for k, v in talent.to_asset().items():
        talent_data[k] = [v]
    return talent_data
