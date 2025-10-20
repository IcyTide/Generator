from base.constant import OVERCOME_SCALE, SHIELD_BASE_MAP, SHIELD_CONSTANT_MAP, STRAIN_SCALE

base_neutral_attack_power = 52863
neutral_attack_power_gain = 0
extra_neutral_attack_power = 19746
magical_damage_addition = 0
recipe_1520_1 =  recipe_4467_1 = recipe_4468_1 = recipe_4469_1 = recipe_4470_1 = recipe_4471_1 = 0
skill_damage_final_cof = 0
neutral_overcome = 47984 / OVERCOME_SCALE
level = 134
neutral_shield_base = SHIELD_BASE_MAP[level]
neutral_shield_gain = all_shield_ignore = 0
shield_constant = SHIELD_CONSTANT_MAP[level]
strain = 104686 / STRAIN_SCALE
pve_addition_base = 553
neutral_damage_cof = 0
min_ret = int(int(int(int(int(int(int(int(int(int(180 + 0 * 20) + int((int(base_neutral_attack_power * (1 + neutral_attack_power_gain / 1024)) + extra_neutral_attack_power) * 2.75)) * (1 + (magical_damage_addition + 51 * recipe_1520_1 + 51 * recipe_4467_1 + 102 * recipe_4468_1 + 153 * recipe_4469_1 + 204 * recipe_4470_1 + 255 * recipe_4471_1) / 1024))) * (1 + skill_damage_final_cof / 1024)) * (1 + (int(neutral_overcome * 1024) - int(int(int(int(neutral_shield_base * (1 + neutral_shield_gain / 1024)) * (1 - all_shield_ignore / 1024)) / (int(int(neutral_shield_base * (1 + neutral_shield_gain / 1024)) * (1 - all_shield_ignore / 1024)) + shield_constant) * 1024) * (1 + int(neutral_overcome * 1024) / 1024))) / 1024)) * (1 - (level - 130) * 0.05)) * (1 + int(strain * 1024) / 1024)) * (1 + pve_addition_base / 1024)) * (1 + neutral_damage_cof / 1024))
max_ret = int(int(int(int(int(int(int(int(int(int(180 + 1 * 20) + int((int(base_neutral_attack_power * (1 + neutral_attack_power_gain / 1024)) + extra_neutral_attack_power) * 2.75)) * (1 + (magical_damage_addition + 51 * recipe_1520_1 + 51 * recipe_4467_1 + 102 * recipe_4468_1 + 153 * recipe_4469_1 + 204 * recipe_4470_1 + 255 * recipe_4471_1) / 1024))) * (1 + skill_damage_final_cof / 1024)) * (1 + (int(neutral_overcome * 1024) - int(int(int(int(neutral_shield_base * (1 + neutral_shield_gain / 1024)) * (1 - all_shield_ignore / 1024)) / (int(int(neutral_shield_base * (1 + neutral_shield_gain / 1024)) * (1 - all_shield_ignore / 1024)) + shield_constant) * 1024) * (1 + int(neutral_overcome * 1024) / 1024))) / 1024)) * (1 - (level - 130) * 0.05)) * (1 + int(strain * 1024) / 1024)) * (1 + pve_addition_base / 1024)) * (1 + neutral_damage_cof / 1024))
print(f"{min_ret} - {max_ret}")