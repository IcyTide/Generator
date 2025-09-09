from base.constant import *
from base.damage import DamageChain
from base.expression import Expression, Int, Variable
from tools.lua.enums import SKILL_KIND_TYPE


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

    physical_damage_rand: int = 0
    solar_damage_rand: int = 0
    lunar_damage_rand: int = 0
    neutral_damage_rand: int = 0
    poison_damage_rand: int = 0

    all_damage_addition: int = 0
    physical_damage_addition: Expression = Variable("physical_damage_addition")
    magical_damage_addition: Expression = Variable("magical_damage_addition")

    move_state_damage_addition: Expression = Variable("move_state_damage_addition")


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
    base_physical_attack_power: Expression = Variable('base_physical_attack_power')
    base_solar_attack_power: Expression = Variable('base_solar_attack_power')
    base_lunar_attack_power: Expression = Variable('base_lunar_attack_power')
    base_neutral_attack_power: Expression = Variable('base_neutral_attack_power')
    base_poison_attack_power: Expression = Variable('base_poison_attack_power')

    physical_attack_power_gain: Expression = Variable('physical_attack_power_gain')
    solar_attack_power_gain: Expression = Variable('solar_attack_power_gain')
    lunar_attack_power_gain: Expression = Variable('lunar_attack_power_gain')
    neutral_attack_power_gain: Expression = Variable('neutral_attack_power_gain')
    poison_attack_power_gain: Expression = Variable('poison_attack_power_gain')

    extra_physical_attack_power: Expression = Variable('extra_physical_attack_power')
    extra_solar_attack_power: Expression = Variable('extra_solar_attack_power')
    extra_lunar_attack_power: Expression = Variable('extra_lunar_attack_power')
    extra_neutral_attack_power: Expression = Variable('extra_neutral_attack_power')
    extra_poison_attack_power: Expression = Variable('extra_poison_attack_power')

    @property
    def physical_attack_power(self) -> Expression:
        attack_power = Int(self.base_physical_attack_power * (1 + self.physical_attack_power_gain / BINARY_SCALE))
        return attack_power + self.extra_physical_attack_power

    @property
    def solar_attack_power(self) -> Expression:
        attack_power = Int(self.base_solar_attack_power * (1 + self.solar_attack_power_gain / BINARY_SCALE))
        return attack_power + self.extra_solar_attack_power

    @property
    def lunar_attack_power(self) -> Expression:
        attack_power = Int(self.base_lunar_attack_power * (1 + self.lunar_attack_power_gain / BINARY_SCALE))
        return attack_power + self.extra_lunar_attack_power

    @property
    def neutral_attack_power(self) -> Expression:
        attack_power = Int(self.base_neutral_attack_power * (1 + self.neutral_attack_power_gain / BINARY_SCALE))
        return attack_power + self.extra_neutral_attack_power

    @property
    def poison_attack_power(self) -> Expression:
        attack_power = Int(self.base_poison_attack_power * (1 + self.poison_attack_power_gain / BINARY_SCALE))
        return attack_power + self.extra_poison_attack_power


class CriticalPower:
    physical_critical_power_base: Expression = Variable('physical_critical_power_base')
    solar_critical_power_base: Expression = Variable('solar_critical_power_base')
    lunar_critical_power_base: Expression = Variable('lunar_critical_power_base')
    neutral_critical_power_base: Expression = Variable('neutral_critical_power_base')
    poison_critical_power_base: Expression = Variable('poison_critical_power_base')

    physical_critical_power_rate: Expression = Variable('physical_critical_power_rate')
    solar_critical_power_rate: Expression = Variable('solar_critical_power_rate')
    lunar_critical_power_rate: Expression = Variable('lunar_critical_power_rate')
    neutral_critical_power_rate: Expression = Variable('neutral_critical_power_rate')
    poison_critical_power_rate: Expression = Variable('poison_critical_power_rate')

    magical_critical_power_rate: int = 0

    @property
    def physical_critical_power_percent(self):
        return self.physical_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def solar_critical_power_percent(self):
        return self.solar_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def lunar_critical_power_percent(self):
        return self.lunar_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def neutral_critical_power_percent(self):
        return self.neutral_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def poison_critical_power_percent(self):
        return self.poison_critical_power_base / CRITICAL_POWER_SCALE

    @property
    def physical_critical_power(self):
        critical_power_rate = BASE_CRITICAL_POWER + self.physical_critical_power_rate
        return self.physical_critical_power_percent + critical_power_rate / BINARY_SCALE

    @property
    def solar_critical_power(self):
        critical_power_rate = BASE_CRITICAL_POWER + self.solar_critical_power_rate + self.magical_critical_power_rate
        return self.solar_critical_power_percent + critical_power_rate / BINARY_SCALE

    @property
    def lunar_critical_power(self):
        critical_power_rate = BASE_CRITICAL_POWER + self.lunar_critical_power_rate + self.magical_critical_power_rate
        return self.lunar_critical_power_percent + critical_power_rate / BINARY_SCALE

    @property
    def neutral_critical_power(self):
        critical_power_rate = BASE_CRITICAL_POWER + self.neutral_critical_power_rate + self.magical_critical_power_rate
        return self.neutral_critical_power_percent + critical_power_rate / BINARY_SCALE

    @property
    def poison_critical_power(self):
        critical_power_rate = BASE_CRITICAL_POWER + self.poison_critical_power_rate + self.magical_critical_power_rate
        return self.poison_critical_power_percent + critical_power_rate / BINARY_SCALE


class CriticalStrike(Major, CriticalPower):
    base_physical_critical_strike: Expression = Variable('base_physical_critical_strike')
    base_solar_critical_strike: Expression = Variable('base_solar_critical_strike')
    base_lunar_critical_strike: Expression = Variable('base_lunar_critical_strike')
    base_neutral_critical_strike: Expression = Variable('base_neutral_critical_strike')
    base_poison_critical_strike: Expression = Variable('base_poison_critical_strike')

    physical_critical_strike_rate: Expression = Variable('physical_critical_strike_rate')
    solar_critical_strike_rate: Expression = Variable('solar_critical_strike_rate')
    lunar_critical_strike_rate: Expression = Variable('lunar_critical_strike_rate')
    neutral_critical_strike_rate: Expression = Variable('neutral_critical_strike_rate')
    poison_critical_strike_rate: Expression = Variable('poison_critical_strike_rate')

    @property
    def physical_critical_strike_extra(self):
        return 0

    @property
    def physical_critical_strike_percent(self):
        return self.base_physical_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def solar_critical_strike_percent(self):
        return self.base_solar_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def lunar_critical_strike_percent(self):
        return self.base_lunar_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def neutral_critical_strike_percent(self):
        return self.base_neutral_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def poison_critical_strike_percent(self):
        return self.base_poison_critical_strike / CRITICAL_STRIKE_SCALE

    @property
    def physical_critical_strike(self):
        return self.physical_critical_strike_percent + self.physical_critical_strike_rate / DECIMAL_SCALE

    @property
    def solar_critical_strike(self):
        return self.solar_critical_strike_percent + self.solar_critical_strike_rate / DECIMAL_SCALE

    @property
    def lunar_critical_strike(self):
        return self.lunar_critical_strike_percent + self.lunar_critical_strike_rate / DECIMAL_SCALE

    @property
    def neutral_critical_strike(self):
        return self.neutral_critical_strike_percent + self.neutral_critical_strike_rate / DECIMAL_SCALE

    @property
    def poison_critical_strike(self):
        return self.poison_critical_strike_percent + self.poison_critical_strike_rate / DECIMAL_SCALE

    def critical_strike(self, kind_type: SKILL_KIND_TYPE):
        return getattr(self, kind_type.value + "_critical_strike")

    def critical_power(self, kind_type: SKILL_KIND_TYPE):
        return getattr(self, kind_type.value + "_critical_power")


class Overcome(Major):
    base_physical_overcome: Expression = Variable('physical_overcome_base')
    base_solar_overcome: Expression = Variable('solar_overcome_base')
    base_lunar_overcome: Expression = Variable('lunar_overcome_base')
    base_neutral_overcome: Expression = Variable('neutral_overcome_base')
    base_poison_overcome: Expression = Variable('poison_overcome_base')

    physical_overcome_gain: Expression = Variable('physical_overcome_gain')
    solar_overcome_gain: Expression = Variable('solar_overcome_gain')
    lunar_overcome_gain: Expression = Variable('lunar_overcome_gain')
    neutral_overcome_gain: Expression = Variable('neutral_overcome_gain')
    poison_overcome_gain: Expression = Variable('poison_overcome_gain')

    extra_physical_overcome: Expression = Variable('extra_physical_overcome')
    extra_solar_overcome: Expression = Variable('extra_solar_overcome')
    extra_lunar_overcome: Expression = Variable('extra_lunar_overcome')
    extra_neutral_overcome: Expression = Variable('extra_neutral_overcome')
    extra_poison_overcome: Expression = Variable('extra_poison_overcome')

    @property
    def final_physical_overcome(self):
        overcome = Int(self.base_physical_overcome * (1 + self.physical_overcome_gain / BINARY_SCALE))
        return overcome + self.extra_physical_overcome

    @property
    def final_solar_overcome(self):
        overcome = Int(self.base_solar_overcome * (1 + self.solar_overcome_gain / BINARY_SCALE))
        return overcome + self.extra_lunar_overcome

    @property
    def final_lunar_overcome(self):
        overcome = Int(self.base_lunar_overcome * (1 + self.lunar_overcome_gain / BINARY_SCALE))
        return overcome + self.extra_lunar_overcome

    @property
    def final_neutral_overcome(self):
        overcome = Int(self.base_neutral_overcome * (1 + self.neutral_overcome_gain / BINARY_SCALE))
        return overcome + self.extra_neutral_overcome

    @property
    def final_poison_overcome(self):
        overcome = Int(self.base_poison_overcome * (1 + self.poison_overcome_gain / BINARY_SCALE))
        return overcome + self.extra_poison_overcome

    @property
    def physical_overcome(self):
        return self.final_physical_overcome / OVERCOME_SCALE

    @property
    def solar_overcome(self):
        return self.final_solar_overcome / OVERCOME_SCALE

    @property
    def lunar_overcome(self):
        return self.final_lunar_overcome / OVERCOME_SCALE

    @property
    def neutral_overcome(self):
        return self.final_neutral_overcome / OVERCOME_SCALE

    @property
    def poison_overcome(self):
        return self.final_poison_overcome / OVERCOME_SCALE


class Minor:
    weapon_damage_base: Expression = Variable('weapon_damage_base')
    weapon_damage_rand: Expression = Variable('weapon_damage_rand')
    weapon_damage_gain: Expression = Variable('weapon_damage_gain')

    surplus_base: Expression = Variable('surplus_base')
    surplus_gain: Expression = Variable('surplus_gain')

    strain_base: Expression = Variable('strain_base')
    strain_gain: Expression = Variable('strain_gain')
    strain_rate: Expression = Variable('strain_rate')

    all_shield_ignore: Expression = Variable('all_shield_ignore')

    pve_addition: Expression = Variable('pve_addition')

    @property
    def base_weapon_damage(self):
        return Int(self.weapon_damage_base * (1 + self.weapon_damage_gain / BINARY_SCALE))

    @property
    def weapon_damage(self):
        return Int(self.base_weapon_damage + self.weapon_damage_rand / 2)

    @property
    def surplus(self):
        return Int(self.surplus_base * (1 + self.surplus_gain / BINARY_SCALE))

    @property
    def base_strain(self):
        return Int(self.strain_base * (1 + self.strain_gain / BINARY_SCALE))

    @property
    def strain_percent(self):
        return self.base_strain / STRAIN_SCALE

    @property
    def strain(self):
        return self.strain_percent + self.strain_rate / BINARY_SCALE


class Defense:
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
        return Int(self.physical_shield_base * (1 + self.physical_shield_gain / BINARY_SCALE))

    @property
    def solar_shield(self):
        return Int(self.solar_shield_base * (1 + self.solar_shield_gain / BINARY_SCALE))

    @property
    def lunar_shield(self):
        return Int(self.lunar_shield_base * (1 + self.lunar_shield_gain / BINARY_SCALE))

    @property
    def neutral_shield(self):
        return Int(self.neutral_shield_base * (1 + self.neutral_shield_gain / BINARY_SCALE))

    @property
    def poison_shield(self):
        return Int(self.poison_shield_base * (1 + self.poison_shield_gain / BINARY_SCALE))


class DamageCof:
    physical_damage_cof: Expression = Variable('physical_damage_cof')
    solar_damage_cof: Expression = Variable('solar_damage_cof')
    lunar_damage_cof: Expression = Variable('lunar_damage_cof')
    neutral_damage_cof: Expression = Variable('neutral_damage_cof')
    poison_damage_cof: Expression = Variable('poison_damage_cof')


class Target(Defense, DamageCof):
    damage_chain: DamageChain

    level: Expression = Variable('target_level')
    global_damage_factor: int = 0

    def call_physical_damage(self, damage_base, damage_rand):
        self.damage_chain.physical_damage_call(damage_base, damage_rand)

    def call_solar_damage(self, damage_base, damage_rand):
        self.damage_chain.solar_damage_call(damage_base, damage_rand)

    def call_lunar_damage(self, damage_base, damage_rand):
        self.damage_chain.lunar_damage_call(damage_base, damage_rand)

    def call_physical_surplus(self, damage_base, damage_rand):
        self.damage_chain.physical_surplus_call(damage_base, damage_rand)

    def call_solar_surplus(self, damage_base, damage_rand):
        self.damage_chain.solar_surplus_call(damage_base, damage_rand)

    def call_lunar_surplus(self, damage_base, damage_rand):
        self.damage_chain.lunar_surplus_call(damage_base, damage_rand)

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
