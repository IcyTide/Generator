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

    script_file: str
    path: str
    script_path: Path = None

    def __init__(self, recipe_id: int, recipe_level: int = 0):
        self.recipe_id = recipe_id
        self.setting_rows = recipe_settings[recipe_settings['RecipeID'] == self.recipe_id]
        self.max_level = self.setting_rows["RecipeLevel"].max()
        if recipe_level:
            self.recipe_level = recipe_level
            setting_row = self.setting_rows[self.setting_rows["RecipeLevel"] == self.recipe_level].iloc[0]
            for k, v in setting_row.items():
                setattr(self, k, v)
            if self.script_file:
                self.script_path = Path(self.path) / self.script_file

    @property
    def recipe_key(self):
        return f"_{self.recipe_id}_{self.recipe_level}"

    def check_skill(self, skill: Skill):
        if self.skill_recipe_type and skill.recipe_type == self.skill_recipe_type:
            return True
        if self.skill_id and skill.skill_id == self.skill_id:
            if not self.skill_level:
                return True
            return self.skill_level == skill.skill_level
        return False

    def to_dict(self):
        if self.recipe_level:
            return {
                "recipe_name": self.recipe_name,
            }
        else:
            return {}
