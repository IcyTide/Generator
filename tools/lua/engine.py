from pathlib import Path

import lupa.lua51 as lupa

from tools.classes.skill import Skill
from tools.lua.enums import ENV_VARIABLES
from tools.utils import BASE_DIR


class BaseEngine:
    base_path = Path(BASE_DIR)

    def __init__(self, lua_path: str | Path = None):
        self.engine = lupa.LuaRuntime(unpack_returned_tuples=True, encoding="gbk")
        self.prepare_engine()
        if lua_path:
            self.lua_path = str(lua_path)
            if not self.lua_path.startswith("scripts"):
                self.lua_path = Path("scripts") / self.lua_path
            self.execute(self.lua_path)

    def prepare_engine(self):
        self.engine.globals().GetEditorString = self.get_editor_string
        self.engine.globals().IsClient = self.is_client
        self.engine.globals().Include = self.include

        for enum_class in ENV_VARIABLES:
            setattr(self.engine.globals(), enum_class.__name__, enum_class)

    def include(self, file):
        self.execute(file)

    def get_editor_string(self, *params):
        return "\t".join(str(e) for e in params)

    def is_client(self):
        return True

    def execute(self, lua_path):
        lua_path = self.base_path / lua_path
        if not lua_path.exists():
            return
        try:
            with open(lua_path, encoding="gbk") as f:
                lua_code = f.read()
            self.engine.execute(lua_code)
        except:
            with open(lua_path, "rb") as f:
                lua_code = f.read()
            self.engine.execute(lua_code)


class Engine(BaseEngine):
    def get_skill_level_data(self, skill: Skill):
        if func := self.engine.globals().GetSkillLevelData:
            return func(skill)
        return None

    def get_skill_recipe_data(self, skill: Skill, recipe_id: int, recipe_level: int):
        if func := self.engine.globals().GetSkillRecipeData:
            return func(skill, recipe_id, recipe_level)
        return None
