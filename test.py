from base.constant import BINARY_SCALE, LEVEL_VARIABLES, OVERCOME_SCALE, STRAIN_SCALE
from qt.classes.skill import Skill

level_variables = LEVEL_VARIABLES(54)
variables = dict(
    physical_attack_power=7290,
    weapon_damage=17,
    weapon_damage_rand=3,
    physical_overcome=2008 / OVERCOME_SCALE,
    strain=3701 / STRAIN_SCALE,
    pve_damage_addition=399 / BINARY_SCALE,
    recipe_369_1=1,
    recipe_370_1=1,
    physical_shield=level_variables["shield_base"] - 280
) | level_variables

skill = Skill.from_dict(
    kungfu_id=10026,
    json=dict(
        belong_id=6524,
        skill_id=6526,
        skill_level=19,
        count=1
    )
)

damage = sum(skill.damages)
min_hit_damage = damage.evaluate(variables)
print(f"min_hit_damage: {int(min_hit_damage)}")
max_hit_damage = damage.evaluate(variables | dict(rand=1))
print(f"max_hit_damage: {int(max_hit_damage)}")
