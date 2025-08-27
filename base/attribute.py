from base.constant import *
from base.expression import Expression, Int, Variable


class DamageAttribute:
    physical_damage_base: int = 0
    solar_damage_base: int = 0
    lunar_damage_base: int = 0
    neutral_damage_base: int = 0
    poison_damage_base: int = 0

    physical_damage_rand: int = 0
    solar_damage_rand: int = 0
    lunar_damage_rand: int = 0
    neutral_damage_rand: int = 0
    poison_damage_rand: int = 0

    physical_damage_addition: Expression = Variable("physical_damage_addition")
    magical_damage_addition: Expression = Variable("magical_damage_addition")


class Major:
    agility_base: Expression = Variable('agility_base')
    strength_base: Expression = Variable('strength_base')
    spirit_base: Expression = Variable('spirit_base')
    spunk_base: Expression = Variable('spunk_base')

    agility_gain: Expression = Variable('agility_gain')
    strength_gain: Expression = Variable('strength_gain')
    spirit_gain: Expression = Variable('spirit_gain')
    spunk_gain: Expression = Variable('spunk_gain')

    @property
    def agility(self) -> Expression:
        return Int(self.agility_base * (1 + self.agility_gain))

    @property
    def strength(self) -> Expression:
        return Int(self.strength_base * (1 + self.strength_gain))

    @property
    def spirit(self) -> Expression:
        return Int(self.spirit_base * (1 + self.spirit_gain))

    @property
    def spunk(self) -> Expression:
        return Int(self.spunk_base * (1 + self.spunk_gain))

    @property
    def agility_critical_strike_base(self) -> Expression:
        return Int(self.agility * AGILITY_TO_CRITICAL_STRIKE)

    @property
    def strength_attack_power_base(self) -> Expression:
        return Int(self.strength * STRENGTH_TO_ATTACK_POWER)

    @property
    def strength_overcome_base(self) -> Expression:
        return Int(self.strength * STRENGTH_TO_OVERCOME)

    @property
    def spirit_critical_strike_base(self) -> Expression:
        return Int(self.spirit * SPIRIT_TO_CRITICAL_STRIKE)

    @property
    def spunk_attack_power_base(self) -> Expression:
        return Int(self.spunk * SPUNK_TO_ATTACK_POWER)

    @property
    def spunk_overcome_base(self) -> Expression:
        return Int(self.spunk * SPUNK_TO_OVERCOME)


class AttackPower(Major):
    physical_attack_power_base: Expression = Variable('physical_attack_power_base')
    solar_attack_power_base: Expression = Variable('solar_attack_power_base')
    lunar_attack_power_base: Expression = Variable('lunar_attack_power_base')
    neutral_attack_power_base: Expression = Variable('neutral_attack_power_base')
    poison_attack_power_base: Expression = Variable('poison_attack_power_base')

    physical_attack_power_gain: Expression = Variable('physical_attack_power_gain')
    solar_attack_power_gain: Expression = Variable('solar_attack_power_gain')
    lunar_attack_power_gain: Expression = Variable('lunar_attack_power_gain')
    neutral_attack_power_gain: Expression = Variable('neutral_attack_power_gain')
    poison_attack_power_gain: Expression = Variable('poison_attack_power_gain')

    @property
    def physical_attack_power_extra(self):
        return 0

    @property
    def solar_attack_power_extra(self):
        return 0

    @property
    def lunar_attack_power_extra(self):
        return 0

    @property
    def neutral_attack_power_extra(self):
        return 0

    @property
    def poison_attack_power_extra(self):
        return 0

    @property
    def base_physical_attack_power(self) -> Expression:
        return self.physical_attack_power_base + self.strength_attack_power_base

    @property
    def base_solar_attack_power(self) -> Expression:
        return self.solar_attack_power_base + self.spunk_attack_power_base

    @property
    def base_lunar_attack_power(self) -> Expression:
        return self.lunar_attack_power_base + self.spunk_attack_power_base

    @property
    def base_neutral_attack_power(self) -> Expression:
        return self.neutral_attack_power_base + self.spunk_attack_power_base

    @property
    def base_poison_attack_power(self) -> Expression:
        return self.poison_attack_power_base + self.spunk_attack_power_base

    @property
    def physical_attack_power(self) -> Expression:
        attack_power = Int(self.base_physical_attack_power * (1 + self.physical_attack_power_gain / BINARY_SCALE))
        return attack_power + self.physical_attack_power_extra

    @property
    def solar_attack_power(self) -> Expression:
        attack_power = Int(self.base_solar_attack_power * (1 + self.solar_attack_power_gain / BINARY_SCALE))
        return attack_power + self.solar_attack_power_extra

    @property
    def lunar_attack_power(self) -> Expression:
        attack_power = Int(self.base_lunar_attack_power * (1 + self.lunar_attack_power_gain / BINARY_SCALE))
        return attack_power + self.lunar_attack_power_extra

    @property
    def neutral_attack_power(self) -> Expression:
        attack_power = Int(self.base_neutral_attack_power * (1 + self.neutral_attack_power_gain / BINARY_SCALE))
        return attack_power + self.neutral_attack_power_extra

    @property
    def poison_attack_power(self) -> Expression:
        attack_power = Int(self.base_poison_attack_power * (1 + self.poison_attack_power_gain / BINARY_SCALE))
        return attack_power + self.poison_attack_power_extra


class CriticalStrike(Major):
    physical_critical_strike_base: Expression = Variable('physical_critical_strike_base')
    solar_critical_strike_base: Expression = Variable('solar_critical_strike_base')
    lunar_critical_strike_base: Expression = Variable('lunar_critical_strike_base')
    neutral_critical_strike_base: Expression = Variable('neutral_critical_strike_base')
    poison_critical_strike_base: Expression = Variable('poison_critical_strike_base')

    physical_critical_strike_rate: Expression = Variable('physical_critical_strike_rate')
    solar_critical_strike_rate: Expression = Variable('solar_critical_strike_rate')
    lunar_critical_strike_rate: Expression = Variable('lunar_critical_strike_rate')
    neutral_critical_strike_rate: Expression = Variable('neutral_critical_strike_rate')
    poison_critical_strike_rate: Expression = Variable('poison_critical_strike_rate')


class Overcome(Major):
    physical_overcome_base: Expression = Variable('physical_overcome_base')
    solar_overcome_base: Expression = Variable('solar_overcome_base')
    lunar_overcome_base: Expression = Variable('lunar_overcome_base')
    neutral_overcome_base: Expression = Variable('neutral_overcome_base')
    poison_overcome_base: Expression = Variable('poison_overcome_base')

    physical_overcome_gain: Expression = Variable('physical_overcome_gain')
    solar_overcome_gain: Expression = Variable('solar_overcome_gain')
    lunar_overcome_gain: Expression = Variable('lunar_overcome_gain')
    neutral_overcome_gain: Expression = Variable('neutral_overcome_gain')
    poison_overcome_gain: Expression = Variable('poison_overcome_gain')


class Attribute(DamageAttribute, AttackPower, CriticalStrike, Overcome):
    pass
