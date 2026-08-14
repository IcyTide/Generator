from typing import TYPE_CHECKING

from base.constant import *
from base.expression import Ceil, Expression, Max, Min, Variable
from tools.lua.enums import SKILL_KIND_TYPE

if TYPE_CHECKING:
    from tools.classes.attribute import Attribute  # noqa
    from tools.classes.skill import Skill  # noqa


class BaseChain:
    source: "Attribute"
    target: "Attribute"
    skill: "Skill"

    skill_attribute: dict[str, int | Expression]
    source_attribute: dict[str, int | Expression]
    target_attribute: dict[str, int | Expression]

    def __init__(self):
        self.rand = Variable("rand")

    def cal_custom_damage(self):
        custom_damage_base = self.skill[custom_damage_base_key := "custom_damage_base"]
        self.skill_attribute[custom_damage_base_key] = custom_damage_base
        return custom_damage_base

    def set_base_damage(self):
        damage_base = self.source[damage_base_key := f"{self.source.damage_type}_damage_base"]
        self.source_attribute[damage_base_key] = damage_base
        damage_rand = self.source[damage_rand_key := f"{self.source.damage_type}_damage_rand"]
        self.source_attribute[damage_rand_key] = damage_rand
        return damage_base, damage_rand

    def cal_base_damage(self):
        damage_base, damage_rand = self.set_base_damage()
        damage = damage_base + self.rand * damage_rand
        return damage

    def set_attack_damage(self):
        if attack_power_gain := self.source[attack_power_gain_key := f"{self.source.damage_type}_attack_power_gain"]:
            self.source_attribute[attack_power_gain_key] = attack_power_gain
            base_attack_power = Variable(f"base_{self.source.damage_type}_attack_power")
            attack_power = Variable(f"{self.source.damage_type}_attack_power")
            attack_power += base_attack_power * attack_power_gain / BINARY_SCALE
        else:
            attack_power = Variable(f"{self.source.damage_type}_attack_power")
        frames = self.skill[frames_key := "frames"]
        self.skill_attribute[frames_key] = frames
        attack_power_cof = self.skill[attack_power_cof_key := f"{self.source.kind_type}_attack_power_cof"]
        self.skill_attribute[attack_power_cof_key] = attack_power_cof
        return attack_power, attack_power_cof

    def cal_attack_damage(self):
        attack_power, attack_power_cof = self.set_attack_damage()
        damage = attack_power * attack_power_cof
        return damage

    def set_surplus_damage(self):
        surplus = Variable(surplus_key := "surplus")
        self.source_attribute[surplus_key] = self.source[surplus_key]
        surplus_cof = self.skill[surplus_cof_key := "surplus_cof"]
        self.skill_attribute[surplus_cof_key] = surplus_cof
        return surplus, surplus_cof

    def cal_surplus_damage(self):
        surplus, surplus_cof = self.set_surplus_damage()
        damage = surplus * surplus_cof
        return damage

    def set_weapon_damage(self):
        weapon_damage = Variable("weapon_damage")
        weapon_damage_rand = Variable("weapon_damage_rand")
        weapon_damage = weapon_damage + self.rand * weapon_damage_rand
        weapon_damage_cof = self.skill[weapon_damage_cof_key := "weapon_damage_cof"]
        self.skill_attribute[weapon_damage_cof_key] = weapon_damage_cof
        return weapon_damage, weapon_damage_cof

    def cal_weapon_damage(self):
        if self.source.damage_type != SKILL_KIND_TYPE.PHYSICS:
            return 0
        weapon_damage, weapon_damage_cof = self.set_weapon_damage()
        damage = weapon_damage * weapon_damage_cof
        return damage

    def set_global_damage_scale(self):
        global_damage_scale = self.target[global_damage_scale_key := "global_damage_scale"]
        if global_damage_scale != 1:
            self.target_attribute[global_damage_scale_key] = global_damage_scale
        global_damage_factor = self.target[global_damage_factor_key := "global_damage_factor"]
        self.target_attribute[global_damage_factor_key] = global_damage_factor
        return global_damage_scale

    def cal_global_damage_scale(self, damage):
        global_damage_scale = self.set_global_damage_scale()
        damage = damage * global_damage_scale
        return damage

    def set_damage_addition(self):
        damage_addition = Variable(damage_addition_key := f"{self.source.kind_type}_damage_addition")
        damage_addition += self.source[damage_addition_key]
        damage_gain = self.source[damage_gain_key := f"{self.source.kind_type}_damage_gain"]
        self.source_attribute[damage_gain_key] = damage_gain
        damage_addition += self.skill.damage_addition
        damage_gain = self.skill[damage_gain_key := "damage_gain"]
        self.skill_attribute[damage_gain_key] = damage_gain
        move_state_damage_addition = self.source.move_state_damage_addition
        move_state_damage_gain = self.source[move_state_damage_gain_key := "move_state_damage_gain"]
        self.source_attribute[move_state_damage_gain_key] = move_state_damage_gain
        return damage_addition, move_state_damage_addition

    def cal_damage_addition(self, damage: Expression):
        damage_addition, move_state_damage_addition = self.set_damage_addition()
        damage = damage * (1 + damage_addition)
        damage = damage * (1 + move_state_damage_addition)
        return damage

    def set_skill_damage_final_addition(self):
        ...

    def cal_skill_damage_final_addition(self, damage):
        skill_damage_final_addition = Variable("skill_damage_final_addition")
        damage = damage * (1 + skill_damage_final_addition)
        return damage

    def set_overcome(self):
        ...

    def cal_overcome(self, damage: Expression):
        overcome = Variable(f"{self.source.damage_type}_overcome")
        damage = damage * (1 + overcome)
        return damage

    def set_defense(self):
        if shield_gain := self.source[shield_gain_key := f"{self.target.damage_type}_shield_gain"]:
            self.target_attribute[shield_gain_key] = shield_gain
            base_shield = Variable(f"base_{self.target.damage_type}_shield")
            shield = Variable(f"{self.target.damage_type}_shield")
            shield += base_shield * shield_gain / BINARY_SCALE
            shield = Max(shield, 0)
        else:
            shield = Variable(f"{self.target.damage_type}_shield")
        all_shield_ignore = Variable("all_shield_ignore")
        shield = shield * (1 - all_shield_ignore / BINARY_SCALE)
        shield_constant = Variable("shield_constant")
        defense = shield / (shield + shield_constant)
        return defense

    def cal_defense(self, damage: Expression):
        defense = self.set_defense()
        damage = damage * (1 - defense)
        return damage

    def set_critical_strike(self):
        critical_strike = Variable(f"{self.source.critical_type}_critical_strike")
        critical_strike_rate_key = f"{self.source.critical_type}_critical_strike_rate"
        if critical_strike_rate := self.source[critical_strike_rate_key]:
            self.source_attribute[critical_strike_rate_key] = critical_strike_rate
            critical_strike += critical_strike_rate / DECIMAL_SCALE
        resist_critical_strike_rate_key = "resist_critical_strike_rate"
        if resist_critical_strike_rate := self.target[resist_critical_strike_rate_key]:
            self.target_attribute[resist_critical_strike_rate_key] = resist_critical_strike_rate
            critical_strike -= resist_critical_strike_rate / DECIMAL_SCALE
        return critical_strike

    def set_critical_power(self):
        critical_power_rate_key = f"{self.source.critical_type}_critical_power_rate"
        if critical_power_rate := self.source[critical_power_rate_key]:
            self.source[critical_power_rate_key] = critical_power_rate
            critical_power = Variable(f"{self.source.critical_type}_critical_power_percent")
            critical_power_rate += Variable(f"{self.source.critical_type}_critical_power_rate")
            critical_power += critical_power_rate / BINARY_SCALE
            critical_power = Min(MAX_CRITICAL_POWER, critical_power)
            unlimit_critical_power_rate = Variable(f"unlimit_critical_power_rate")
            critical_power += unlimit_critical_power_rate / BINARY_SCALE
        else:
            critical_power = Variable(f"{self.source.critical_type}_critical_power")
        return critical_power

    def cal_critical(self, damage: Expression):
        if not self.source.critical_type:
            critical_strike, critical_power = 0, 0
        else:
            critical_strike, critical_power = self.set_critical_strike(), self.set_critical_power()
            if self.skill.is_frost:
                damage = damage * (1 + critical_strike * (critical_power - 1))
                critical_strike, critical_power = 0, 0
        return critical_strike, critical_power, damage

    def cal_level_reduction(self, damage: Expression):
        source_level, target_level = LEVEL, Variable("level")
        reduction = (target_level - source_level) * LEVEL_REDUCTION
        damage = damage * (1 - reduction)
        return damage

    def set_strain(self):
        ...

    def cal_strain(self, damage: Expression):
        strain = Variable("strain")
        damage = damage * (1 + strain)
        return damage

    def set_pve_damage(self):
        pve_damage_addition = Variable(pve_damage_addition_key := "pve_damage_addition")
        pve_damage_addition += self.source[pve_damage_addition_key]
        pve_damage_gain = self.source[pve_damage_gain_key := "pve_damage_cof"]
        self.source_attribute[pve_damage_gain_key] = pve_damage_gain
        return pve_damage_addition

    def cal_pve_damage(self, damage: Expression):
        pve_damage_addition = self.set_pve_damage()
        damage = damage * (1 + pve_damage_addition)
        return damage

    def set_damage_scale(self):
        if not self.target.damage_type:
            return Variable("damage_scale")
        damage_scale = Variable(damage_scale_key := f"{self.target.damage_type}_damage_scale")
        damage_scale += self.target[damage_scale_key]
        damage_cof = self.target[damage_cof_key := f"{self.target.damage_type}_damage_cof"]
        self.target_attribute[damage_cof_key] = damage_cof
        damage_cof = self.target[damage_cof_key := "coming_damage_cof"]
        self.target_attribute[damage_cof_key] = Ceil(damage_cof)
        return damage_scale

    def cal_damage_scale(self, damage: Expression):
        damage_scale = self.set_damage_scale()
        damage = damage * (1 + damage_scale)
        return damage



class BaseCallChain(BaseChain):
    formulas: list[tuple[int | Expression, int | Expression, int | Expression]]
    source_attributes: list[dict[str, int | Expression]]
    target_attributes: list[dict[str, int | Expression]]

    def __init__(self, source: "Attribute", target: "Attribute", skill: "Skill"):
        super().__init__()
        self.source, self.target, self.skill = source, target, skill
        self.formulas, self.source_attributes, self.target_attributes = [], [], []
        self.skill_attribute = {}
        self.source.critical_type = self.skill.kind_type

    def init_damage(self):
        self.source_attribute = {}
        self.source_attributes.append(self.source_attribute)
        self.target_attribute = {}
        self.target_attributes.append(self.target_attribute)

    def chain_call(self, damage):
        damage = self.cal_global_damage_scale(damage)
        damage = self.cal_damage_addition(damage)
        damage = self.cal_skill_damage_final_addition(damage)
        damage = self.cal_overcome(damage)
        damage = self.cal_defense(damage)
        critical_strike, critical_power, damage = self.cal_critical(damage)
        damage = self.cal_level_reduction(damage)
        damage = self.cal_strain(damage)
        damage = self.cal_pve_damage(damage)
        damage = self.cal_damage_scale(damage)
        return critical_strike, critical_power, damage


class DamageCallChain(BaseCallChain):
    def custom_damage_call(self):
        self.source.damage_type = self.target.damage_type = self.skill.custom_damage_type
        self.init_damage()
        damage = self.cal_custom_damage()
        damage = self.cal_level_reduction(damage)
        damage = self.cal_damage_scale(damage)
        self.formulas.append((0, 0, damage))

    def damage_call(self, damage_base, damage_rand):
        self.init_damage()
        self.source.damage_base = damage_base or self.source.damage_base
        self.source.damage_rand = damage_rand or self.source.damage_rand
        base_damage = self.cal_base_damage()
        attack_damage = self.cal_attack_damage()
        weapon_damage = self.cal_weapon_damage()
        damage = base_damage + attack_damage + weapon_damage
        return self.chain_call(damage)

    def physical_damage_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.PHYSICS
        critical_strike, critical_power, damage = self.damage_call(damage_base, damage_rand)
        self.formulas.append((critical_strike, critical_power, damage))

    def solar_damage_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.SOLAR_MAGIC
        critical_strike, critical_power, damage = self.damage_call(damage_base, damage_rand)
        self.formulas.append((critical_strike, critical_power, damage))

    def lunar_damage_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.LUNAR_MAGIC
        critical_strike, critical_power, damage = self.damage_call(damage_base, damage_rand)
        self.formulas.append((critical_strike, critical_power, damage))

    def neutral_damage_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.NEUTRAL_MAGIC
        critical_strike, critical_power, damage = self.damage_call(damage_base, damage_rand)
        self.formulas.append((critical_strike, critical_power, damage))

    def poison_damage_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.POISON
        critical_strike, critical_power, damage = self.damage_call(damage_base, damage_rand)
        self.formulas.append((critical_strike, critical_power, damage))


class SurplusCallChain(BaseCallChain):
    def surplus_call(self):
        self.init_damage()
        damage = self.cal_surplus_damage()
        return self.chain_call(damage)

    def physical_surplus_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.PHYSICS
        critical_strike, critical_power, damage = self.surplus_call()
        self.formulas.append((critical_strike, critical_power, damage))

    def solar_surplus_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.SOLAR_MAGIC
        critical_strike, critical_power, damage = self.surplus_call()
        self.formulas.append((critical_strike, critical_power, damage))

    def lunar_surplus_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.LUNAR_MAGIC
        critical_strike, critical_power, damage = self.surplus_call()
        self.formulas.append((critical_strike, critical_power, damage))

    def neutral_surplus_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.NEUTRAL_MAGIC
        critical_strike, critical_power, damage = self.surplus_call()
        self.formulas.append((critical_strike, critical_power, damage))

    def poison_surplus_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.POISON
        critical_strike, critical_power, damage = self.surplus_call()
        self.formulas.append((critical_strike, critical_power, damage))


class DamageChain(DamageCallChain, SurplusCallChain):
    def to_dict(self):
        damage_dicts = []
        for i, (critical_strike, critical_power, damage) in enumerate(self.formulas):
            source_attribute = self.source_attributes[i]
            target_attribute = self.target_attributes[i]
            damage_dict = dict(
                damage=str(damage),
                critical_strike=str(critical_strike),
                critical_power=str(critical_power),
                source_attribute={k: str(v) for k, v in source_attribute.items() if v},
                target_attribute={k: str(v) for k, v in target_attribute.items() if v}
            )
            damage_dict = {k: v for k, v in damage_dict.items() if v}
            damage_dicts.append(damage_dict)
        skill_attribute = {k: str(v) for k, v in self.skill_attribute.items() if v}
        return dict(
            damages=damage_dicts,
            skill_attribute=skill_attribute
        )
