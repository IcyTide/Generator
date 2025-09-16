from typing import TYPE_CHECKING

from base.constant import *
from base.expression import Expression, Int, Variable
from tools.lua.enums import SKILL_KIND_TYPE

if TYPE_CHECKING:
    from tools.classes.skill import Skill  # noqa
    from tools.classes.attribute import Attribute, Target  # noqa


class DamageChain:
    damage: int | Expression
    critical_damage: int | Expression
    critical_strike: Expression

    def __init__(self, source: "Attribute", target: "Target", skill: "Skill"):
        self.source = source
        self.target = target
        self.skill = skill

        self.damage, self.critical_damage, self.rand = 0, 0, Variable("rand")

        self.need_int = True

    def physical_damage_call(self, damage_base, damage_rand):
        damage_base = damage_base or self.source.physical_damage_base
        damage_rand = damage_rand or self.source.physical_damage_rand
        self.cal_base_damage(damage_base, damage_rand)
        self.cal_attack_power_damage(self.source.physical_attack_power, self.skill.physical_attack_power_cof)
        self.cal_weapon_damage()
        self.physical_chain()

    def solar_damage_call(self, damage_base, damage_rand):
        damage_base = damage_base or self.source.solar_damage_base
        damage_rand = damage_rand or self.source.solar_damage_rand
        self.cal_base_damage(damage_base, damage_rand)
        self.cal_attack_power_damage(self.source.solar_attack_power, self.skill.magical_attack_power_cof)
        self.solar_chain()

    def lunar_damage_call(self, damage_base, damage_rand):
        damage_base = damage_base or self.source.lunar_damage_base
        damage_rand = damage_rand or self.source.lunar_damage_rand
        self.cal_base_damage(damage_base, damage_rand)
        self.cal_attack_power_damage(self.source.lunar_attack_power, self.skill.magical_attack_power_cof)
        self.lunar_chain()

    def neutral_damage_call(self, damage_base, damage_rand):
        damage_base = damage_base or self.source.neutral_damage_base
        damage_rand = damage_rand or self.source.neutral_damage_rand
        self.cal_base_damage(damage_base, damage_rand)
        self.cal_attack_power_damage(self.source.neutral_attack_power, self.skill.magical_attack_power_cof)
        self.neutral_chain()

    def poison_damage_call(self, damage_base, damage_rand):
        damage_base = damage_base or self.source.poison_damage_base
        damage_rand = damage_rand or self.source.poison_damage_rand
        self.cal_base_damage(damage_base, damage_rand)
        self.cal_attack_power_damage(self.source.poison_attack_power, self.skill.magical_attack_power_cof)
        self.poison_chain()

    def physical_surplus_call(self, damage_base, damage_rand):
        damage_base = damage_base or self.source.physical_damage_base
        damage_rand = damage_rand or self.source.physical_damage_rand
        self.cal_base_damage(damage_base, damage_rand)
        self.cal_surplus_damage()
        self.physical_chain()

    def solar_surplus_call(self, damage_base, damage_rand):
        damage_base = damage_base or self.source.solar_damage_base
        damage_rand = damage_rand or self.source.solar_damage_rand
        self.cal_base_damage(damage_base, damage_rand)
        self.cal_surplus_damage()
        self.solar_chain()

    def lunar_surplus_call(self, damage_base, damage_rand):
        damage_base = damage_base or self.source.lunar_damage_base
        damage_rand = damage_rand or self.source.lunar_damage_rand
        self.cal_base_damage(damage_base, damage_rand)
        self.cal_surplus_damage()
        self.lunar_chain()

    def neutral_surplus_call(self, damage_base, damage_rand):
        damage_base = damage_base or self.source.neutral_damage_base
        damage_rand = damage_rand or self.source.neutral_damage_rand
        self.cal_base_damage(damage_base, damage_rand)
        self.cal_surplus_damage()
        self.neutral_chain()

    def poison_surplus_call(self, damage_base, damage_rand):
        damage_base = damage_base or self.source.physical_damage_base
        damage_rand = damage_rand or self.source.physical_damage_rand
        self.cal_base_damage(damage_base, damage_rand)
        self.cal_surplus_damage()
        self.poison_chain()

    def physical_chain(self):
        self.chain(
            self.source.physical_damage_addition, self.source.physical_overcome,
            self.target.physical_shield, self.target.physical_damage_cof
        )

    def solar_chain(self):
        self.chain(
            self.source.magical_damage_addition, self.source.solar_overcome,
            self.target.solar_shield, self.target.solar_damage_cof
        )

    def lunar_chain(self):
        self.chain(
            self.source.magical_damage_addition, self.source.lunar_overcome,
            self.target.lunar_shield, self.target.lunar_damage_cof
        )

    def neutral_chain(self):
        self.chain(
            self.source.magical_damage_addition, self.source.neutral_overcome,
            self.target.neutral_shield, self.target.neutral_damage_cof
        )

    def poison_chain(self):
        self.chain(
            self.source.magical_damage_addition, self.source.poison_overcome,
            self.target.poison_shield, self.target.poison_damage_cof
        )

    def chain(self, damage_addition, overcome, shield, damage_cof):
        self.cal_global_damage()
        self.cal_damage_add(damage_addition + self.source.all_damage_addition, self.source.move_state_damage_addition)
        self.cal_overcome(overcome)
        self.cal_defense(shield)
        self.cal_level_reduction()
        self.cal_strain()
        self.cal_pve_add()
        self.cal_damage_cof(damage_cof + self.target.coming_damage_cof)

    def cal_base_damage(self, damage_base, damage_rand):
        damage = damage_base + self.rand * damage_rand
        if self.need_int:
            self.damage += Int(damage)
        else:
            self.damage += damage

    def cal_attack_power_damage(self, attack_power, attack_power_cof):
        damage = attack_power * attack_power_cof
        if self.need_int:
            self.damage += Int(damage)
        else:
            self.damage += damage

    def cal_surplus_damage(self):
        damage = self.source.surplus * DEFAULT_SURPLUS_COF
        if self.need_int:
            self.damage += Int(damage)
        else:
            self.damage += damage

    def cal_weapon_damage(self):
        damage = (self.source.weapon_damage + self.rand * self.source.weapon_damage_rand) * self.skill.weapon_damage_cof
        if self.need_int:
            self.damage += Int(damage)
        else:
            self.damage += damage

    def cal_global_damage(self):
        rate = (self.target.global_damage_factor + (1 << 20)) / (1 << 20)
        self.damage *= rate
        if self.need_int:
            self.damage = Int(self.damage)

    def cal_damage_add(self, damage_addition, move_state_damage_addition):
        rate = 1 + (damage_addition + self.skill.damage_addition) / BINARY_SCALE
        self.damage *= rate
        if self.need_int:
            self.damage = Int(self.damage)
        rate = 1 + move_state_damage_addition / BINARY_SCALE
        self.damage *= rate
        if self.need_int:
            self.damage = Int(self.damage)

    def cal_overcome(self, overcome):
        if self.need_int:
            rate = 1 + Int(overcome * BINARY_SCALE) / BINARY_SCALE
            self.damage = Int(self.damage * rate)
        else:
            self.damage *= 1 + overcome

    def cal_defense(self, shield):
        shield_constant = SHIELD_SCALE * (LEVEL_SCALE * self.target.level - LEVEL_CONSTANT)
        shield = Int(shield * (1 - self.source.all_shield_ignore / BINARY_SCALE))
        defense = shield / (shield + shield_constant)
        if self.need_int:
            rate = 1 - Int(defense * BINARY_SCALE) / BINARY_SCALE
            self.damage = Int(self.damage * rate)
        else:
            self.damage *= (1 - defense)

    def cal_level_reduction(self):
        rate = (self.target.level - self.source.level) * LEVEL_REDUCTION
        self.damage *= rate
        if self.need_int:
            self.damage = Int(self.damage)

    def cal_strain(self):
        if self.need_int:
            rate = 1 + Int(self.source.strain * BINARY_SCALE) / BINARY_SCALE
            self.damage = Int(self.damage * rate)
        else:
            self.damage *= 1 + self.source.strain

    def cal_pve_add(self):
        rate = 1 + self.source.pve_addition / BINARY_SCALE
        self.damage *= rate
        if self.need_int:
            self.damage = Int(self.damage)

    def cal_damage_cof(self, damage_cof):
        rate = 1 + damage_cof / BINARY_SCALE
        self.damage *= rate
        if self.need_int:
            self.damage = Int(self.damage)

    def cal_critical(self, kind_type: SKILL_KIND_TYPE):
        damage = Variable("damage")
        if self.need_int:
            rate = Int(self.source.critical_power(kind_type) * BINARY_SCALE) / BINARY_SCALE
            self.critical_damage = Int(damage * rate)
        else:
            rate = self.source.critical_power(kind_type)
            self.critical_damage = damage * rate
        self.critical_strike = self.source.critical_strike(kind_type)

    def to_dict(self):
        self.cal_critical(self.skill.kind_type)
        # terms =  self.damage.terms | self.critical_damage.terms | self.critical_strike.terms
        # recipes = sorted(term for term in terms if term.startswith("_"))
        return dict(
            damage=str(self.damage), critical_damage=str(self.critical_damage),
            critical_strike=str(self.critical_strike)
        )
