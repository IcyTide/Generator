from typing import TYPE_CHECKING

from base.constant import *
from base.expression import Expression, Int, Max, Min, Variable
from tools.lua.enums import SKILL_KIND_TYPE

if TYPE_CHECKING:
    from tools.classes.attribute import Attribute  # noqa
    from tools.classes.skill import Skill  # noqa


class BaseChain:
    source: "Attribute"
    target: "Attribute"
    skill: "Skill"

    critical_strike: float | Expression
    critical_power: float | Expression
    skill_attribute: dict[str, int | float | Expression]
    critical_attribute: dict[str, int | float | Expression]
    source_attribute: dict[str, int | Expression]
    target_attribute: dict[str, int | Expression]

    def __init__(self):
        self.rand = Variable("rand")
        self.is_critical = Variable("is_critical")
        self.need_int = True

    def set_critical_strike(self):
        offset = self.source[offset_key := f"{self.source.critical_type}_critical_strike_offset"]
        self.critical_attribute[offset_key] = offset
        rate = self.source[rate_key := f"{self.source.critical_type}_critical_strike_rate"]
        self.critical_attribute[rate_key] = rate

        resist_offset = self.target[resist_offset_key := "resist_critical_strike_offset"]
        self.critical_attribute[resist_offset_key] = resist_offset
        resist_rate = self.target[resist_rate_key := "resist_critical_strike_rate"]
        self.critical_attribute[resist_rate_key] = resist_rate

        critical_strike = Variable(f"{self.source.critical_type}_critical_strike")
        if offset or resist_offset:
            critical_strike += offset - resist_offset
            critical_strike = Min(critical_strike, MAX_CRITICAL_STRIKE)
        return critical_strike

    def set_custom_damage(self):
        custom_damage_base = self.skill[custom_damage_base_key := "custom_damage_base"]
        self.skill_attribute[custom_damage_base_key] = custom_damage_base
        return custom_damage_base

    def cal_custom_damage(self):
        return self.set_custom_damage()

    def set_base_damage(self):
        base = self.source[base_key := f"{self.source.damage_type}_damage_base"]
        self.source_attribute[base_key] = base
        if self.need_int:
            base = Int(base)
        rand = self.source[rand_key := f"{self.source.damage_type}_damage_rand"]
        self.source_attribute[rand_key] = rand
        if self.need_int:
            rand = Int(rand)
        return base, rand

    def cal_base_damage(self):
        base, rand = self.set_base_damage()
        damage = base + self.rand * rand
        return damage

    def set_attack_damage(self):
        addition = self.source[addition_key := f"{self.source.damage_type}_attack_power_addition"]
        self.source_attribute[addition_key] = addition
        gain = self.source[gain_key := f"{self.source.damage_type}_attack_power_gain"]
        self.source_attribute[gain_key] = gain
        if addition:
            addition += Variable(addition_key)
            attack_power = Variable(f"base_{self.source.damage_type}_attack_power") * (1 + addition)
            if self.need_int:
                attack_power = Int(attack_power)
            attack_power += Variable(f"extra_{self.source.damage_type}_attack_power")
        else:
            attack_power = Variable(f"{self.source.damage_type}_attack_power")

        frames = self.skill[frames_key := "frames"]
        self.skill_attribute[frames_key] = frames
        if self.skill.tick_cof != 1:
            self.skill_attribute["tick_cof"] = self.skill.tick_cof
        if self.skill.dot_damage_cof != 1:
            self.skill_attribute["dot_damage_cof"] = self.skill.dot_damage_cof
        cof = self.skill[cof_key := f"{self.source.kind_type}_attack_power_cof"]
        self.skill_attribute[cof_key] = cof
        return attack_power, cof

    def cal_attack_damage(self):
        attack_power, cof = self.set_attack_damage()
        damage = attack_power * cof
        if self.need_int:
            damage = Int(damage)
        return damage

    def set_weapon_damage(self):
        base, rand = Variable("weapon_damage"), Variable("weapon_damage_rand")
        weapon_damage = base + self.rand * rand
        cof = self.skill[cof_key := "weapon_damage_cof"]
        self.skill_attribute[cof_key] = cof
        return weapon_damage, cof

    def cal_weapon_damage(self):
        if self.source.damage_type != SKILL_KIND_TYPE.PHYSICS:
            return 0
        weapon_damage, cof = self.set_weapon_damage()
        damage = weapon_damage * cof
        if self.need_int:
            damage = Int(damage)
        return damage

    def set_global_damage_scale(self):
        scale = self.target[scale_key := "global_damage_scale"]
        if scale != 1:
            self.target_attribute[scale_key] = scale
        cof = self.target[factor_key := "global_damage_cof"]
        self.target_attribute[factor_key] = cof
        return scale

    def cal_global_damage_scale(self, damage):
        scale = self.set_global_damage_scale()
        damage = damage * scale
        if self.need_int:
            damage = Int(damage)
        return damage

    def set_skill_damage_scale(self):
        scale = self.skill[scale_key := "skill_damage_scale"]
        self.skill_attribute[scale_key] = scale
        cof = self.skill[cof_key := "skill_damage_cof"]
        self.skill_attribute[cof_key] = cof
        return scale

    def cal_skill_damage_scale(self, damage):
        scale = self.set_skill_damage_scale()
        damage = damage * (1 + scale)
        if self.need_int:
            damage = Int(damage)
        return damage

    @staticmethod
    def set_skill_damage_addition():
        return Variable("skill_damage_addition")

    def cal_skill_damage_addition(self, damage):
        addition = self.set_skill_damage_addition()
        damage = damage * (1 + addition)
        if self.need_int:
            damage = Int(damage)
        return damage

    def set_damage_addition(self):
        source_addition = self.source[source_addition_key := f"{self.source.kind_type}_damage_addition"]
        self.source_attribute[source_addition_key] = self.source[source_addition_key]
        source_gain = self.source[source_gain_key := f"{self.source.kind_type}_damage_gain"]
        self.source_attribute[source_gain_key] = source_gain

        addition = source_addition
        if not self.skill.is_dot:
            skill_addition = self.skill[skill_addition_key := "damage_addition"]
            self.skill_attribute[skill_addition_key] = skill_addition
            skill_gain = self.skill[skill_gain_key := "damage_gain"]
            self.skill_attribute[skill_gain_key] = skill_gain
            addition += skill_addition
        addition += Variable(source_addition_key)
        return addition

    def cal_damage_addition(self, damage: Expression):
        addition = self.set_damage_addition()
        damage = damage * (1 + addition)
        if self.need_int:
            damage = Int(damage)
        return damage

    def set_move_state_damage_addition(self):
        addition = self.source[addition_key := "move_state_damage_addition"]
        self.source_attribute[addition_key] = addition
        gain = self.source[gain_key := "move_state_damage_gain"]
        self.source_attribute[gain_key] = gain
        addition += Variable(addition_key)
        return addition

    def cal_move_state_damage_addition(self, damage):
        addition = self.set_move_state_damage_addition()
        damage = damage * (1 + addition)
        if self.need_int:
            damage = Int(damage)
        return damage

    def set_overcome(self):
        return Variable(f"{self.source.damage_type}_overcome")

    def cal_overcome(self, damage: Expression):
        overcome = self.set_overcome()
        damage = damage * (1 + overcome)
        if self.need_int:
            damage = Int(damage)
        return damage

    def set_defense(self):
        addition = self.target[addition_key := f"{self.target.damage_type}_shield_addition"]
        self.target_attribute[addition_key] = addition
        gain = self.target[gain_key := f"{self.target.damage_type}_shield_gain"]
        self.target_attribute[gain_key] = gain
        if addition:
            shield = Variable(f"{self.target.damage_type}_shield")
            shield += Variable(f"base_{self.target.damage_type}_shield") * addition
            if self.need_int:
                shield = Int(shield)
            shield = Max(shield, 0)
        else:
            shield = Variable(f"{self.target.damage_type}_shield")
        all_shield_ignore = Variable("all_shield_ignore")
        shield = shield * (1 - all_shield_ignore / BINARY_SCALE)
        if self.need_int:
            shield = Int(shield)
        shield_constant = Variable("shield_constant")
        defense = shield_constant / (shield + shield_constant)
        return defense

    def cal_defense(self, damage: Expression):
        defense = self.set_defense()
        damage = damage * defense
        if self.need_int:
            damage = Int(damage)
        return damage

    def set_critical_power(self):
        offset = self.source[offset_key := f"{self.source.critical_type}_critical_power_offset"]
        self.critical_attribute[offset_key] = offset
        rate = self.source[rate_key := f"{self.source.critical_type}_critical_power_rate"]
        self.critical_attribute[rate_key] = rate

        unlimit_offset = self.source[unlimit_offset_key := "unlimit_critical_power_offset"]
        self.critical_attribute[unlimit_offset_key] = unlimit_offset
        unlimit_rate = self.source[unlimit_rate_key := "unlimit_critical_power_rate"]
        self.critical_attribute[unlimit_rate_key] = unlimit_rate

        if offset:
            critical_power = Variable(f"limit_{self.source.critical_type}_critical_power")
            critical_power += offset
            critical_power = Min(critical_power, MAX_CRITICAL_POWER)
            critical_power += Variable("unlimit_critical_power_offset") + unlimit_offset
        else:
            critical_power = Variable(f"{self.source.critical_type}_critical_power")
            critical_power += unlimit_offset
        return critical_power

    def cal_critical_power(self, damage: Expression):
        if not self.source.critical_type:
            return damage
        critical_power = self.set_critical_power()
        if self.skill.is_frost:
            damage = damage * (1 + self.critical_strike * (critical_power - 1))
            self.critical_strike = 0
        else:
            damage = damage * (1 + self.is_critical * (critical_power - 1))
        if self.need_int:
            damage = Int(damage)
        return damage

    def set_level_reduction(self):
        source_level, target_level = self.source.level, Variable("level")
        reduction = (target_level - source_level) * LEVEL_REDUCTION
        return reduction

    def cal_level_reduction(self, damage: Expression):
        reduction = self.set_level_reduction()
        damage = damage * (1 - reduction)
        if self.need_int:
            damage = Int(damage)
        return damage

    @staticmethod
    def set_strain():
        return Variable("strain")

    def cal_strain(self, damage: Expression):
        strain = self.set_strain()
        damage = damage * (1 + strain)
        if self.need_int:
            damage = Int(damage)
        return damage

    def set_pve_damage(self):
        addition = self.source[addition_key := "pve_damage_addition"]
        self.source_attribute[addition_key] = addition
        gain = self.source[gain_key := "pve_damage_gain"]
        self.source_attribute[gain_key] = gain
        addition += Variable(addition_key)
        return addition

    def cal_pve_damage(self, damage: Expression):
        addition = self.set_pve_damage()
        damage = damage * (1 + addition)
        if self.need_int:
            damage = Int(damage)
        return damage

    def set_damage_scale(self):
        if not self.target.damage_type:
            return Variable("damage_scale")
        scale = self.target[scale_key := f"{self.target.damage_type}_damage_scale"]
        self.target_attribute[scale_key] = scale
        cof = self.target[cof_key := "damage_cof"]
        self.target_attribute[cof_key] = cof
        coming_scale = self.skill[coming_scale_key := "coming_damage_scale"]
        self.skill_attribute[coming_scale_key] = coming_scale
        coming_cof = self.skill[coming_cof_key := "coming_damage_cof"]
        self.skill_attribute[coming_cof_key] = coming_cof
        scale += coming_scale
        scale += Variable(scale_key)
        return scale

    def cal_damage_scale(self, damage: Expression):
        damage_scale = self.set_damage_scale()
        damage = damage * (1 + damage_scale)
        if self.need_int:
            damage = Int(damage)
        return damage


class BaseCallChain(BaseChain):
    damages: list[int | Expression]
    source_attributes: list[dict[str, int | Expression]]
    target_attributes: list[dict[str, int | Expression]]

    def __init__(self, source: "Attribute", target: "Attribute", skill: "Skill"):
        super().__init__()
        self.source, self.target, self.skill = source, target, skill
        self.damages, self.source_attributes, self.target_attributes = [], [], []
        self.skill_attribute, self.critical_attribute = {}, {}
        self.source.critical_type = self.skill.kind_type
        if self.source.critical_type:
            self.critical_strike = self.set_critical_strike()
        else:
            self.critical_strike = 0

    def init_damage(self):
        self.source_attribute = {}
        self.source_attributes.append(self.source_attribute)
        self.target_attribute = {}
        self.target_attributes.append(self.target_attribute)

    def chain_call(self, damage):
        damage = self.cal_global_damage_scale(damage)
        damage = self.cal_skill_damage_scale(damage)
        damage = self.cal_damage_addition(damage)
        damage = self.cal_skill_damage_addition(damage)
        damage = self.cal_move_state_damage_addition(damage)
        damage = self.cal_overcome(damage)
        damage = self.cal_defense(damage)
        damage = self.cal_critical_power(damage)
        damage = self.cal_level_reduction(damage)
        damage = self.cal_strain(damage)
        damage = self.cal_pve_damage(damage)
        damage = self.cal_damage_scale(damage)
        return damage


class DamageCallChain(BaseCallChain):
    def custom_damage_call(self):
        self.source.damage_type = self.target.damage_type = self.skill.custom_damage_type
        self.init_damage()
        self.critical_strike = 0
        damage = self.cal_custom_damage()
        damage = self.cal_level_reduction(damage)
        damage = self.cal_damage_scale(damage)
        self.damages.append(damage)

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
        damage = self.damage_call(damage_base, damage_rand)
        self.damages.append(damage)

    def solar_damage_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.SOLAR_MAGIC
        damage = self.damage_call(damage_base, damage_rand)
        self.damages.append(damage)

    def lunar_damage_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.LUNAR_MAGIC
        damage = self.damage_call(damage_base, damage_rand)
        self.damages.append(damage)

    def neutral_damage_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.NEUTRAL_MAGIC
        damage = self.damage_call(damage_base, damage_rand)
        self.damages.append(damage)

    def poison_damage_call(self, damage_base, damage_rand):
        self.source.damage_type = self.target.damage_type = SKILL_KIND_TYPE.POISON
        damage = self.damage_call(damage_base, damage_rand)
        self.damages.append(damage)


class DamageChain(DamageCallChain):
    def to_dict(self):
        damage_dicts = []
        for i, damage in enumerate(self.damages):
            source_attribute = self.source_attributes[i]
            target_attribute = self.target_attributes[i]
            damage_dict = dict(
                damage=str(damage),
                source_attribute={k: str(v) for k, v in source_attribute.items() if v},
                target_attribute={k: str(v) for k, v in target_attribute.items() if v}
            )
            damage_dict = {k: v for k, v in damage_dict.items() if v}
            damage_dicts.append(damage_dict)
        return dict(
            damages=damage_dicts,
            critical_strike=str(self.critical_strike),
            critical_attribute={k: str(v) for k, v in self.critical_attribute.items() if v},
            skill_attribute={k: str(v) for k, v in self.skill_attribute.items() if v}
        )
