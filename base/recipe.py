from base.skill import Skill


class Recipe:
    recipe_id: int
    recipe_level: int

    recipe_name: str
    name: str

    skill_recipe_type: int
    skill_id: int
    skill_level: int

    prepare_frames_add: int
    damage_add_percent: int

    clone_id: int
    sub_check_list: list[int] = []

    def script_check(self, skill: Skill):
        if skill.skill_id in self.sub_check_list:
            return True
        return False

    def setting_check(self, skill: Skill):
        if skill.recipe_type == self.skill_recipe_type:
            return True
        if skill.skill_id in (self.skill_id, self.clone_id):
            if not self.skill_level:
                return True
            return self.skill_level == skill.skill_level
        return False

    def check_effect(self, skill: Skill):
        if self.prepare_frames_add + self.damage_add_percent:
            return self.setting_check(skill)
        else:
            return self.setting_check(skill) and self.script_check(skill)

    def apply(self, skill: Skill):
        skill.prepare_frames += self.prepare_frames_add
        skill.damage_add_percent += self.damage_add_percent
        if self.script_check(skill):
            self.apply_script(skill)

    def apply_script(self, skill: Skill):
        pass

    def unapply(self, skill: Skill):
        skill.prepare_frames -= self.prepare_frames_add
        skill.damage_add_percent -= self.damage_add_percent
        if self.script_check(skill):
            self.unapply_script(skill)

    def unapply_script(self, skill: Skill):
        pass
