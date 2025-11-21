from typing import TYPE_CHECKING

from base.constant import *
from base.expression import Expression, Int, Variable
from tools.lua.enums import SKILL_KIND_TYPE

if TYPE_CHECKING:
    from tools.classes.damage import DamageChain  # noqa


class BaseType:
    need_int: bool = True


class DamageAdd:
    # physical_damage_base: Expression = Variable('physical_damage_base')
    # solar_damage_base: Expression = Variable('solar_damage_base')
    # lunar_damage_base: Expression = Variable('lunar_damage_base')
    # neutral_damage_base: Expression = Variable('neutral_damage_base')
    # poison_damage_base: Expression = Variable('poison_damage_base')
    #
    # physical_damage_rand: Expression = Variable('physical_damage_rand')
    # solar_damage_rand: Expression = Variable('solar_damage_rand')
    # lunar_damage_rand: Expression = Variable('lunar_damage_rand')
    # neutral_damage_rand: Expression = Variable('neutral_damage_rand')
    # poison_damage_rand: Expression = Variable('poison_damage_rand')
    physical_damage_base: int = 0
    solar_damage_base: int = 0
    lunar_damage_base: int = 0
    neutral_damage_base: int = 0
    poison_damage_base: int = 0
    adaptive_damage_base: int = 0

    physical_damage_rand: int = 0
    solar_damage_rand: int = 0
    lunar_damage_rand: int = 0
    neutral_damage_rand: int = 0
    poison_damage_rand: int = 0
    adaptive_damage_rand: int = 0

    all_damage_addition: int = 0
    physical_damage_addition: Expression = Variable("physical_damage_addition")
    magical_damage_addition: Expression = Variable("magical_damage_addition")

    move_state_damage_addition: int = 0

    skill_damage_final_cof: Expression = Variable("skill_damage_final_cof")


class AttackPower(BaseType):
    physical_attack_power_base: int = 0
    magical_attack_power_base: int = 0
    all_attack_power_base: int = 0

    base_physical_attack_power: Expression = Variable("base_physical_attack_power")
    base_solar_attack_power: Expression = Variable("base_solar_attack_power")
    base_lunar_attack_power: Expression = Variable("base_lunar_attack_power")
    base_neutral_attack_power: Expression = Variable("base_neutral_attack_power")
    base_poison_attack_power: Expression = Variable("base_poison_attack_power")

    physical_attack_power_gain: int = 0
    solar_attack_power_gain: int = 0
    lunar_attack_power_gain: int = 0
    neutral_attack_power_gain: int = 0
    poison_attack_power_gain: int = 0

    @property
    def physical_attack_power(self) -> Expression:
        if self.need_int:
            physical_attack_power_gain = Variable("physical_attack_power_gain") + self.physical_attack_power_gain
            attack_power = Int(self.base_physical_attack_power * (1 + physical_attack_power_gain / BINARY_SCALE))
            extra_physical_attack_power = Variable("extra_physical_attack_power")
            attack_power += extra_physical_attack_power
        else:
            attack_power = Variable("physical_attack_power")
            attack_power += self.physical_attack_power_gain * self.base_physical_attack_power
        return attack_power

    @property
    def solar_attack_power(self) -> Expression:
        if self.need_int:
            solar_attack_power_gain = Variable("solar_attack_power_gain") + self.solar_attack_power_gain
            attack_power = Int(self.base_solar_attack_power * (1 + solar_attack_power_gain / BINARY_SCALE))
            extra_solar_attack_power = Variable("extra_solar_attack_power")
            attack_power += extra_solar_attack_power
        else:
            attack_power = Variable("solar_attack_power")
            attack_power += self.solar_attack_power_gain / BINARY_SCALE * self.base_solar_attack_power
        return attack_power

    @property
    def lunar_attack_power(self) -> Expression:
        if self.need_int:
            lunar_attack_power_gain = Variable("lunar_attack_power_gain") + self.lunar_attack_power_gain
            attack_power = Int(self.base_lunar_attack_power * (1 + lunar_attack_power_gain / BINARY_SCALE))
            extra_lunar_attack_power = Variable("extra_lunar_attack_power")
            attack_power += extra_lunar_attack_power
        else:
            attack_power = Variable("lunar_attack_power")
            attack_power += self.lunar_attack_power_gain / BINARY_SCALE * self.base_lunar_attack_power
        return attack_power

    @property
    def neutral_attack_power(self) -> Expression:
        if self.need_int:
            neutral_attack_power_gain = Variable("neutral_attack_power_gain") + self.neutral_attack_power_gain
            attack_power = Int(self.base_neutral_attack_power * (1 + neutral_attack_power_gain / BINARY_SCALE))
            extra_neutral_attack_power = Variable("extra_neutral_attack_power")
            attack_power += extra_neutral_attack_power
        else:
            attack_power = Variable("neutral_attack_power")
            attack_power += self.neutral_attack_power_gain / BINARY_SCALE * self.base_neutral_attack_power
        return attack_power

    @property
    def poison_attack_power(self) -> Expression:
        if self.need_int:
            poison_attack_power_gain = Variable("poison_attack_power_gain") + self.poison_attack_power_gain
            attack_power = Int(self.base_poison_attack_power * (1 + poison_attack_power_gain / BINARY_SCALE))
            extra_poison_attack_power = Variable("extra_poison_attack_power")
            attack_power += extra_poison_attack_power
        else:
            attack_power = Variable("poison_attack_power")
            attack_power += self.poison_attack_power_gain / BINARY_SCALE * self.base_poison_attack_power
        return attack_power


class CriticalPower:
    physical_critical_power_rate: int = 0
    solar_critical_power_rate: int = 0
    lunar_critical_power_rate: int = 0
    neutral_critical_power_rate: int = 0
    poison_critical_power_rate: int = 0

    magical_critical_power_rate: int = 0

    @property
    def physical_critical_power(self):
        physical_critical_power = Variable("physical_critical_power")
        return physical_critical_power + self.physical_critical_power_rate / BINARY_SCALE

    @property
    def solar_critical_power(self):
        solar_critical_power = Variable("solar_critical_power")
        critical_power_rate = self.solar_critical_power_rate + self.magical_critical_power_rate
        return solar_critical_power + critical_power_rate / BINARY_SCALE

    @property
    def lunar_critical_power(self):
        lunar_critical_power = Variable("lunar_critical_power")
        critical_power_rate = self.lunar_critical_power_rate + self.magical_critical_power_rate
        return lunar_critical_power + critical_power_rate / BINARY_SCALE

    @property
    def neutral_critical_power(self):
        neutral_critical_power = Variable("neutral_critical_power")
        critical_power_rate = self.neutral_critical_power_rate + self.magical_critical_power_rate
        return neutral_critical_power + critical_power_rate / BINARY_SCALE

    @property
    def poison_critical_power(self):
        poison_critical_power = Variable("poison_critical_power")
        critical_power_rate = self.poison_critical_power_rate + self.magical_critical_power_rate
        return poison_critical_power + critical_power_rate / BINARY_SCALE


class CriticalStrike(CriticalPower):
    physical_critical_strike_rate: int = 0
    solar_critical_strike_rate: int = 0
    lunar_critical_strike_rate: int = 0
    neutral_critical_strike_rate: int = 0
    poison_critical_strike_rate: int = 0

    @property
    def physical_critical_strike(self):
        physical_critical_strike = Variable("physical_critical_strike")
        return physical_critical_strike + self.physical_critical_strike_rate / DECIMAL_SCALE

    @property
    def solar_critical_strike(self):
        solar_critical_strike = Variable("solar_critical_strike")
        return solar_critical_strike + self.solar_critical_strike_rate / DECIMAL_SCALE

    @property
    def lunar_critical_strike(self):
        lunar_critical_strike = Variable("lunar_critical_strike")
        return lunar_critical_strike + self.lunar_critical_strike_rate / DECIMAL_SCALE

    @property
    def neutral_critical_strike(self):
        neutral_critical_strike = Variable("neutral_critical_strike")
        return neutral_critical_strike + self.neutral_critical_strike_rate / DECIMAL_SCALE

    @property
    def poison_critical_strike(self):
        poison_critical_strike = Variable("poison_critical_strike")
        return poison_critical_strike + self.poison_critical_strike_rate / DECIMAL_SCALE

    def critical_strike(self, kind_type: SKILL_KIND_TYPE):
        return getattr(self, f"{kind_type}_critical_strike")

    def critical_power(self, kind_type: SKILL_KIND_TYPE):
        return getattr(self, f"{kind_type}_critical_power")


class Overcome:
    physical_overcome: Expression = Variable('physical_overcome')
    solar_overcome: Expression = Variable('solar_overcome')
    lunar_overcome: Expression = Variable('lunar_overcome')
    neutral_overcome: Expression = Variable('neutral_overcome')
    poison_overcome: Expression = Variable('poison_overcome')


class Minor:
    weapon_damage: Expression = Variable('weapon_damage')
    weapon_damage_rand: Expression = Variable('weapon_damage_rand')

    surplus: Expression = Variable('surplus')

    strain: Expression = Variable('strain')

    all_shield_ignore: Expression = Variable('all_shield_ignore')

    pve_addition_base: Expression = Variable('pve_addition_base')


class Defense(BaseType):
    physical_shield_base: Expression = Variable('physical_shield_base')
    solar_shield_base: Expression = Variable('solar_shield_base')
    lunar_shield_base: Expression = Variable('lunar_shield_base')
    neutral_shield_base: Expression = Variable('neutral_shield_base')
    poison_shield_base: Expression = Variable('poison_shield_base')

    physical_shield_gain: Expression = Variable('physical_shield_gain')
    solar_shield_gain: Expression = Variable('solar_shield_gain')
    lunar_shield_gain: Expression = Variable('lunar_shield_gain')
    neutral_shield_gain: Expression = Variable('neutral_shield_gain')
    poison_shield_gain: Expression = Variable('poison_shield_gain')

    @property
    def physical_shield(self):
        physical_shield = self.physical_shield_base * (1 + self.physical_shield_gain / BINARY_SCALE)
        if self.need_int:
            physical_shield = Int(physical_shield)
        return physical_shield

    @property
    def solar_shield(self):
        solar_shield = self.solar_shield_base * (1 + self.solar_shield_gain / BINARY_SCALE)
        if self.need_int:
            solar_shield = Int(solar_shield)
        return solar_shield

    @property
    def lunar_shield(self):
        lunar_shield = self.lunar_shield_base * (1 + self.lunar_shield_gain / BINARY_SCALE)
        if self.need_int:
            lunar_shield = Int(lunar_shield)
        return lunar_shield

    @property
    def neutral_shield(self):
        neutral_shield = self.neutral_shield_base * (1 + self.neutral_shield_gain / BINARY_SCALE)
        if self.need_int:
            neutral_shield = Int(neutral_shield)
        return neutral_shield

    @property
    def poison_shield(self):
        poison_shield = self.poison_shield_base * (1 + self.poison_shield_gain / BINARY_SCALE)
        if self.need_int:
            poison_shield = Int(poison_shield)
        return poison_shield


class DamageCof:
    physical_damage_cof: Expression = Variable('physical_damage_cof')
    solar_damage_cof: Expression = Variable('solar_damage_cof')
    lunar_damage_cof: Expression = Variable('lunar_damage_cof')
    neutral_damage_cof: Expression = Variable('neutral_damage_cof')
    poison_damage_cof: Expression = Variable('poison_damage_cof')

    coming_damage_cof: int = 0

    def damage_cof(self, kind_type: SKILL_KIND_TYPE = ""):
        if kind_type:
            return getattr(self, f"{kind_type}_damage_cof")
        else:
            return Variable('damage_cof')


class Target(Defense, DamageCof):
    damage_chain: "DamageChain"

    level: Expression = Variable('level')

    resist_critical_strike_rate: int = 0
    global_damage_factor: int = 0
    global_damage_scale: float = 0
    
    @property
    def resist_critical_strike(self):
        return self.resist_critical_strike_rate / DECIMAL_SCALE

    def call_physical_damage(self, damage_base, damage_rand):
        self.damage_chain.physical_damage_call(damage_base, damage_rand)

    def call_solar_damage(self, damage_base, damage_rand):
        self.damage_chain.solar_damage_call(damage_base, damage_rand)

    def call_lunar_damage(self, damage_base, damage_rand):
        self.damage_chain.lunar_damage_call(damage_base, damage_rand)

    def call_neutral_damage(self, damage_base, damage_rand):
        self.damage_chain.neutral_damage_call(damage_base, damage_rand)

    def call_poison_damage(self, damage_base, damage_rand):
        self.damage_chain.poison_damage_call(damage_base, damage_rand)

    def call_adaptive_damage(self, damage_base, damage_rand):
        self.damage_chain.adaptive_damage_call(damage_base, damage_rand)

    def call_physical_surplus(self, damage_base, damage_rand):
        self.damage_chain.physical_surplus_call(damage_base, damage_rand)

    def call_solar_surplus(self, damage_base, damage_rand):
        self.damage_chain.solar_surplus_call(damage_base, damage_rand)

    def call_lunar_surplus(self, damage_base, damage_rand):
        self.damage_chain.lunar_surplus_call(damage_base, damage_rand)

    def call_neutral_surplus(self, damage_base, damage_rand):
        self.damage_chain.neutral_surplus_call(damage_base, damage_rand)

    def call_poison_surplus(self, damage_base, damage_rand):
        self.damage_chain.poison_surplus_call(damage_base, damage_rand)

    def __getitem__(self, item):
        if item in dir(self):
            return getattr(self, item)
        return None

    def __setitem__(self, key, value):
        if key in dir(self):
            setattr(self, key, value)


class Attribute(DamageAdd, AttackPower, CriticalStrike, Overcome, Minor):
    level: int = LEVEL

    def __getitem__(self, item):
        if item in dir(self):
            return getattr(self, item)
        return None

    def __setitem__(self, key, value):
        if key in dir(self):
            setattr(self, key, value)
