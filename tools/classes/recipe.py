from pathlib import Path

from tools.classes import AliasBase
from tools.classes.skill import Skill
from tools.settings import recipe_settings
from tools.utils import path_to_function


class Recipe(AliasBase):
    recipe_id: int
    recipe_level: int = 0
    recipe_name: str

    skill_recipe_type: int
    skill_id: int
    skill_level: int

    prepare_frames_add: int
    damage_add_percent: int

    script_file: str = ""

    def __init__(self, recipe_id):
        self.recipe_id = recipe_id
        self.setting_rows = recipe_settings[recipe_settings['RecipeID'] == self.recipe_id]
        self.max_level = self.setting_rows["RecipeLevel"].max()

    def check_skill(self, skill: Skill):
        if skill.recipe_type == self.skill_recipe_type:
            return True
        if skill.skill_id == self.skill_id:
            if not self.skill_level:
                return True
            return self.skill_level == skill.skill_level
        return False

    def to_asset(self):
        if self.recipe_level:
            setting_row = self.setting_rows[self.setting_rows["RecipeLevel"] == self.recipe_level].iloc[0]
            for k, v in setting_row.items():
                setattr(self, k, v)
            return {
                "recipe_name": self.recipe_name,
                "skill_recipe_type": int(self.skill_recipe_type),
                "skill_id": int(self.skill_id),
                "skill_level": int(self.skill_level),
                "script": path_to_function(self.script_file)
            }
        else:
            return {
                "recipe_id": self.recipe_id,
                "max_level": int(self.max_level),
            }
