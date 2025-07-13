import os

import lupa.lua51 as lupa

from tools.lua.enums import ENV_VARIABLES
from tools.utils import BASE_DIR

class Engine:
    include_packages: list

    def __init__(self):
        self.engine = lupa.LuaRuntime(encoding="gbk")
        self.include_packages = []
        for enum_class in ENV_VARIABLES:
            setattr(self.engine.globals(), enum_class.__name__, enum_class)
        self.engine.globals().GetEditorString = self.get_editor_string
        self.engine.globals().IsClient = self.is_client
        self.engine.globals().Include = self.include
        self.execute("scripts/include/skill.lh")
        self.execute("scripts/include/newskill.lh")

    @staticmethod
    def get_editor_string(*params):
        return "\t".join(str(e) for e in params)

    @staticmethod
    def is_client():
        return True

    def include(self, script_path):
        if script_path in self.include_packages:
            return
        # self.engine.execute(script_path)
        self.include_packages.append(script_path)

    def execute(self, script_file):
        try:
            with open(os.path.join(BASE_DIR, script_file), encoding="utf-8") as f:
                lua_code = f.read()
            self.engine.execute(lua_code)
        except:
            with open(os.path.join(BASE_DIR, script_file), "rb") as f:
                lua_code = f.read()
            self.engine.execute(lua_code)

    def run(self, func, *args):
        return self.engine.globals()[func](*args)