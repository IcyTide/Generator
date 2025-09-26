from base.constant import *


class Major:
    agility_base: int = 0
    strength_base: int = 0
    spirit_base: int = 0
    spunk_base: int = 0

    agility_gain: int = 0
    strength_gain: int = 0
    spirit_gain: int = 0
    spunk_gain: int = 0

    @property
    def agility(self) -> int:
        return int(self.agility_base * (1 + self.agility_gain))

    @property
    def strength(self) -> int:
        return int(self.strength_base * (1 + self.strength_gain))

    @property
    def spirit(self) -> int:
        return int(self.spirit_base * (1 + self.spirit_gain))

    @property
    def spunk(self) -> int:
        return int(self.spunk_base * (1 + self.spunk_gain))

    @property
    def agility_critical_strike_base(self) -> int:
        return int(self.agility * AGILITY_TO_CRITICAL_STRIKE)

    @property
    def strength_attack_power_base(self) -> int:
        return int(self.strength * STRENGTH_TO_ATTACK_POWER)

    @property
    def strength_overcome_base(self) -> int:
        return int(self.strength * STRENGTH_TO_OVERCOME)

    @property
    def spirit_critical_strike_base(self) -> int:
        return int(self.spirit * SPIRIT_TO_CRITICAL_STRIKE)

    @property
    def spunk_attack_power_base(self) -> int:
        return int(self.spunk * SPUNK_TO_ATTACK_POWER)

    @property
    def spunk_overcome_base(self) -> int:
        return int(self.spunk * SPUNK_TO_OVERCOME)


class AttackPower(Major):
    physical_attack_power_base: int = 0
    solar_attack_power_base: int = 0
    lunar_attack_power_base: int = 0
    _solar_and_lunar_attack_power_base: int = 0
    neutral_attack_power_base: int = 0
    poison_attack_power_base: int = 0
    _magical_attack_power_base: int = 0

    physical_attack_power_gain: int = 0
    solar_attack_power_gain: int = 0
    lunar_attack_power_gain: int = 0
    neutral_attack_power_gain: int = 0
    poison_attack_power_gain: int = 0

    agility_to_physical_attack_power: int = 0
    strength_to_physical_attack_power: int = 0
    spunk_to_solar_attack_power: int = 0
    spirit_to_lunar_attack_power: int = 0
    spunk_to_solar_and_lunar_attack_power: int = 0
    spunk_to_neutral_attack_power: int = 0
    spirit_to_neutral_attack_power: int = 0
    spunk_to_poison_attack_power: int = 0
    spirit_to_poison_attack_power: int = 0

    @property
    def solar_and_lunar_attack_power_base(self) -> int:
        return self._solar_and_lunar_attack_power_base

    @solar_and_lunar_attack_power_base.setter
    def solar_and_lunar_attack_power_base(self, value):
        residual = value - self._solar_and_lunar_attack_power_base
        self.solar_attack_power_base += residual
        self.lunar_attack_power_base += residual
        self._solar_and_lunar_attack_power_base = value

    @property
    def magical_attack_power_base(self) -> int:
        return self._magical_attack_power_base

    @magical_attack_power_base.setter
    def magical_attack_power_base(self, value):
        residual = value - self._magical_attack_power_base
        self.solar_attack_power_base += residual
        self.lunar_attack_power_base += residual
        self.neutral_attack_power_base += residual
        self.poison_attack_power_base += residual
        self._magical_attack_power_base = value

    @property
    def extra_physical_attack_power(self) -> int:
        if self.agility_to_physical_attack_power:
            return int(self.agility * self.agility_to_physical_attack_power / BINARY_SCALE)
        if self.strength_to_physical_attack_power:
            return int(self.strength * self.strength_to_physical_attack_power / BINARY_SCALE)
        return 0

    @property
    def extra_solar_attack_power(self) -> int:
        if self.spunk_to_solar_attack_power:
            return int(self.spunk * self.spunk_to_solar_attack_power / BINARY_SCALE)
        if self.spunk_to_solar_and_lunar_attack_power:
            return int(self.spunk * self.spunk_to_solar_and_lunar_attack_power / BINARY_SCALE)
        return 0

    @property
    def extra_lunar_attack_power(self) -> int:
        if self.spirit_to_lunar_attack_power:
            return int(self.spirit * self.spirit_to_lunar_attack_power / BINARY_SCALE)
        if self.spunk_to_solar_and_lunar_attack_power:
            return int(self.spunk * self.spunk_to_solar_and_lunar_attack_power / BINARY_SCALE)
        return 0

    @property
    def extra_neutral_attack_power(self) -> int:
        if self.spirit_to_neutral_attack_power:
            return int(self.spirit * self.spirit_to_neutral_attack_power / BINARY_SCALE)
        if self.spunk_to_neutral_attack_power:
            return int(self.spunk * self.spunk_to_neutral_attack_power / BINARY_SCALE)
        return 0

    @property
    def extra_poison_attack_power(self) -> int:
        if self.spirit_to_poison_attack_power:
            return int(self.spirit * self.spirit_to_poison_attack_power / BINARY_SCALE)
        if self.spunk_to_poison_attack_power:
            return int(self.spunk * self.spunk_to_poison_attack_power / BINARY_SCALE)
        return 0

    @property
    def base_physical_attack_power(self) -> int:
        return self.physical_attack_power_base + self.strength_attack_power_base

    @property
    def base_solar_attack_power(self) -> int:
        return self.solar_attack_power_base + self.spunk_attack_power_base

    @property
    def base_lunar_attack_power(self) -> int:
        return self.lunar_attack_power_base + self.spunk_attack_power_base

    @property
    def base_neutral_attack_power(self) -> int:
        return self.neutral_attack_power_base + self.spunk_attack_power_base

    @property
    def base_poison_attack_power(self) -> int:
        return self.poison_attack_power_base + self.spunk_attack_power_base

    @property
    def physical_attack_power(self) -> int:
        base_attack_power = int(self.base_physical_attack_power * (1 + self.physical_attack_power_gain / BINARY_SCALE))
        return base_attack_power + self.extra_physical_attack_power

    @property
    def solar_attack_power(self) -> int:
        base_attack_power = int(self.base_solar_attack_power * (1 + self.solar_attack_power_gain / BINARY_SCALE))
        return base_attack_power + self.extra_solar_attack_power

    @property
    def lunar_attack_power(self) -> int:
        base_attack_power = int(self.base_lunar_attack_power * (1 + self.lunar_attack_power_gain / BINARY_SCALE))
        return base_attack_power + self.extra_lunar_attack_power

    @property
    def neutral_attack_power(self) -> int:
        base_attack_power = int(self.base_neutral_attack_power * (1 + self.neutral_attack_power_gain / BINARY_SCALE))
        return base_attack_power + self.extra_neutral_attack_power

    @property
    def poison_attack_power(self) -> int:
        base_attack_power = int(self.base_poison_attack_power * (1 + self.poison_attack_power_gain / BINARY_SCALE))
        return base_attack_power + self.extra_poison_attack_power


class CriticalStrike(Major):
    physical_critical_strike_base: int = 0
    solar_critical_strike_base: int = 0
    lunar_critical_strike_base: int = 0
    _solar_and_lunar_critical_strike_base: int = 0
    neutral_critical_strike_base: int = 0
    poison_critical_strike_base: int = 0
    _magical_critical_strike_base: int = 0
    _all_critical_strike_base: int = 0

    physical_critical_strike_rate: int = 0
    solar_critical_strike_rate: int = 0
    lunar_critical_strike_rate: int = 0
    neutral_critical_strike_rate: int = 0
    poison_critical_strike_rate: int = 0

    agility_to_physical_critical_strike: int = 0
    strength_to_physical_critical_strike: int = 0
    spunk_to_physical_critical_strike: int = 0
    spunk_to_solar_critical_strike: int = 0
    spirit_to_lunar_critical_strike: int = 0
    spunk_to_solar_and_lunar_critical_strike: int = 0
    spirit_to_neutral_critical_strike: int = 0

    @property
    def solar_and_lunar_critical_strike_base(self) -> int:
        return self._solar_and_lunar_critical_strike_base

    @solar_and_lunar_critical_strike_base.setter
    def solar_and_lunar_critical_strike_base(self, value):
        residual = value - self.solar_and_lunar_critical_strike_base
        self.solar_critical_strike_base += residual
        self.lunar_critical_strike_base += residual
        self._solar_and_lunar_critical_strike_base = value

    @property
    def magical_critical_strike_base(self) -> int:
        return self._magical_critical_strike_base

    @magical_critical_strike_base.setter
    def magical_critical_strike_base(self, value):
        residual = value - self.magical_critical_strike_base
        self.solar_critical_strike_base += residual
        self.lunar_critical_strike_base += residual
        self.neutral_critical_strike_base += residual
        self.poison_critical_strike_base += residual
        self._magical_critical_strike_base = value

    @property
    def all_critical_strike_base(self) -> int:
        return self._all_critical_strike_base

    @all_critical_strike_base.setter
    def all_critical_strike_base(self, value):
        residual = value - self.all_critical_strike_base
        self.physical_critical_strike_base += residual
        self.solar_critical_strike_base += residual
        self.lunar_critical_strike_base += residual
        self.neutral_critical_strike_base += residual
        self.poison_critical_strike_base += residual
        self._all_critical_strike_base = value

    @property
    def extra_physical_critical_strike(self) -> int:
        if self.agility_to_physical_critical_strike:
            return int(self.agility * self.agility_to_physical_critical_strike / BINARY_SCALE)
        if self.strength_to_physical_critical_strike:
            return int(self.strength * self.strength_to_physical_critical_strike / BINARY_SCALE)
        if self.spunk_to_physical_critical_strike:
            return int(self.spunk * self.spunk_to_physical_critical_strike / BINARY_SCALE)
        return 0

    @property
    def extra_solar_critical_strike(self) -> int:
        if self.spunk_to_solar_critical_strike:
            return int(self.spunk * self.spunk_to_solar_critical_strike / BINARY_SCALE)
        if self.spunk_to_solar_and_lunar_critical_strike:
            return int(self.spunk * self.spunk_to_solar_and_lunar_critical_strike / BINARY_SCALE)
        return 0

    @property
    def extra_lunar_critical_strike(self) -> int:
        if self.spirit_to_lunar_critical_strike:
            return int(self.spirit * self.spirit_to_lunar_critical_strike / BINARY_SCALE)
        if self.spunk_to_solar_and_lunar_critical_strike:
            return int(self.spunk * self.spunk_to_solar_and_lunar_critical_strike / BINARY_SCALE)
        return 0

    @property
    def extra_neutral_critical_strike(self) -> int:
        if self.spirit_to_neutral_critical_strike:
            return int(self.spirit * self.spirit_to_neutral_critical_strike / BINARY_SCALE)
        return 0

    @property
    def extra_poison_critical_strike(self) -> int:
        return 0

    @property
    def base_physical_critical_strike(self) -> int:
        return self.physical_critical_strike_base + self.agility_critical_strike_base

    @property
    def base_solar_critical_strike(self) -> int:
        return self.solar_critical_strike_base + self.spirit_critical_strike_base

    @property
    def base_lunar_critical_strike(self) -> int:
        return self.lunar_critical_strike_base + self.spirit_critical_strike_base

    @property
    def base_neutral_critical_strike(self) -> int:
        return self.neutral_critical_strike_base + self.spirit_critical_strike_base

    @property
    def base_poison_critical_strike(self) -> int:
        return self.poison_critical_strike_base + self.spirit_critical_strike_base

    @property
    def physical_critical_strike_percent(self) -> float:
        return (self.base_physical_critical_strike + self.extra_physical_critical_strike) / CRITICAL_STRIKE_SCALE

    @property
    def solar_critical_strike_percent(self) -> float:
        return (self.base_solar_critical_strike + self.extra_solar_critical_strike) / CRITICAL_STRIKE_SCALE

    @property
    def lunar_critical_strike_percent(self) -> float:
        return (self.base_lunar_critical_strike + self.extra_lunar_critical_strike) / CRITICAL_STRIKE_SCALE

    @property
    def neutral_critical_strike_percent(self) -> float:
        return (self.base_neutral_critical_strike + self.extra_neutral_critical_strike) / CRITICAL_STRIKE_SCALE

    @property
    def poison_critical_strike_percent(self) -> float:
        return (self.base_poison_critical_strike + self.extra_poison_critical_strike) / CRITICAL_STRIKE_SCALE

    @property
    def physical_critical_strike(self) -> float:
        return self.physical_critical_strike_percent + self.physical_critical_strike_rate / DECIMAL_SCALE

    @property
    def solar_critical_strike(self) -> float:
        return self.solar_critical_strike_percent + self.solar_critical_strike_rate / DECIMAL_SCALE

    @property
    def lunar_critical_strike(self) -> float:
        return self.lunar_critical_strike_percent + self.lunar_critical_strike_rate / DECIMAL_SCALE

    @property
    def neutral_critical_strike(self) -> float:
        return self.neutral_critical_strike_percent + self.neutral_critical_strike_rate / DECIMAL_SCALE

    @property
    def poison_critical_strike(self) -> float:
        return self.poison_critical_strike_percent + self.poison_critical_strike_rate / DECIMAL_SCALE


class Overcome(Major):
    physical_overcome_base: int = 0
    solar_overcome_base: int = 0
    lunar_overcome_base: int = 0
    _solar_and_lunar_overcome_base: int = 0
    neutral_overcome_base: int = 0
    poison_overcome_base: int = 0
    _magical_overcome_base: int = 0

    physical_overcome_gain: int = 0
    solar_overcome_gain: int = 0
    lunar_overcome_gain: int = 0
    neutral_overcome_gain: int = 0
    poison_overcome_gain: int = 0

    agility_to_physical_overcome: int = 0
    strength_to_physical_overcome: int = 0
    spunk_to_neutral_overcome: int = 0
    spirit_to_poison_overcome: int = 0

    @property
    def solar_and_lunar_overcome_base(self) -> int:
        return self._solar_and_lunar_overcome_base

    @solar_and_lunar_overcome_base.setter
    def solar_and_lunar_overcome_base(self, value):
        residual = value - self.solar_and_lunar_overcome_base
        self.solar_overcome_base += residual
        self.lunar_overcome_base += residual
        self._solar_and_lunar_overcome_base = value

    @property
    def magical_overcome_base(self) -> int:
        return self._magical_overcome_base

    @magical_overcome_base.setter
    def magical_overcome_base(self, value):
        residual = value - self.magical_overcome_base
        self.solar_overcome_base += residual
        self.lunar_overcome_base += residual
        self.neutral_overcome_base += residual
        self.poison_overcome_base += residual
        self._magical_overcome_base = value

    @property
    def extra_physical_overcome(self) -> int:
        if self.agility_to_physical_overcome:
            return int(self.agility * self.agility_to_physical_overcome / BINARY_SCALE)
        if self.strength_to_physical_overcome:
            return int(self.strength * self.strength_to_physical_overcome / BINARY_SCALE)
        return 0

    @property
    def extra_solar_overcome(self) -> int:
        return 0

    @property
    def extra_lunar_overcome(self) -> int:
        return 0

    @property
    def extra_neutral_overcome(self) -> int:
        if self.spunk_to_neutral_overcome:
            return int(self.spunk * self.spunk_to_neutral_overcome / BINARY_SCALE)
        return 0

    @property
    def extra_poison_overcome(self) -> int:
        if self.spirit_to_poison_overcome:
            return int(self.spirit * self.spirit_to_poison_overcome / BINARY_SCALE)
        return 0

    @property
    def base_physical_overcome(self) -> int:
        return self.physical_overcome_base + self.strength_overcome_base

    @property
    def base_solar_overcome(self) -> int:
        return self.solar_overcome_base + self.spunk_overcome_base

    @property
    def base_lunar_overcome(self) -> int:
        return self.lunar_overcome_base + self.spunk_overcome_base

    @property
    def base_neutral_overcome(self) -> int:
        return self.neutral_overcome_base + self.spunk_overcome_base

    @property
    def base_poison_overcome(self) -> int:
        return self.poison_overcome_base + self.spunk_overcome_base

    @property
    def final_physical_overcome(self) -> int:
        base_overcome = int(self.base_physical_overcome * (1 + self.physical_overcome_gain / BINARY_SCALE))
        return base_overcome + self.extra_physical_overcome

    @property
    def final_solar_overcome(self) -> int:
        base_overcome = int(self.base_solar_overcome * (1 + self.solar_overcome_gain / BINARY_SCALE))
        return base_overcome + self.extra_solar_overcome

    @property
    def final_lunar_overcome(self) -> int:
        base_overcome = int(self.base_lunar_overcome * (1 + self.lunar_overcome_gain / BINARY_SCALE))
        return base_overcome + self.extra_lunar_overcome

    @property
    def final_neutral_overcome(self) -> int:
        base_overcome = int(self.base_neutral_overcome * (1 + self.neutral_overcome_gain / BINARY_SCALE))
        return base_overcome + self.extra_neutral_overcome

    @property
    def final_poison_overcome(self) -> int:
        base_overcome = int(self.base_poison_overcome * (1 + self.poison_overcome_gain / BINARY_SCALE))
        return base_overcome + self.extra_poison_overcome

    @property
    def physical_overcome(self) -> float:
        return self.final_physical_overcome / OVERCOME_SCALE

    @property
    def solar_overcome(self) -> float:
        return self.final_solar_overcome / OVERCOME_SCALE

    @property
    def lunar_overcome(self) -> float:
        return self.final_lunar_overcome / OVERCOME_SCALE

    @property
    def neutral_overcome(self) -> float:
        return self.final_neutral_overcome / OVERCOME_SCALE

    @property
    def poison_overcome(self) -> float:
        return self.final_poison_overcome / OVERCOME_SCALE


class CriticalPower:
    physical_critical_power_base: int = 0
    solar_critical_power_base: int = 0
    lunar_critical_power_base: int = 0
    _solar_and_lunar_critical_power_base: int = 0
    neutral_critical_power_base: int = 0
    poison_critical_power_base: int = 0
    _magical_critical_power_base: int = 0
    _all_critical_power_base: int = 0

    physical_critical_power_rate: int = 0
    solar_critical_power_rate: int = 0
    lunar_critical_power_rate: int = 0
    neutral_critical_power_rate: int = 0
    poison_critical_power_rate: int = 0
    _magical_critical_power_rate: int = 0
    _all_critical_power_rate: int = 0

    @property
    def solar_and_lunar_critical_power_base(self):
        return self._solar_and_lunar_critical_power_base

    @solar_and_lunar_critical_power_base.setter
    def solar_and_lunar_critical_power_base(self, value):
        residual = value - self.solar_and_lunar_critical_power_base
        self.solar_critical_power_base += residual
        self.lunar_critical_power_base += residual
        self._solar_and_lunar_critical_power_base = value

    @property
    def magical_critical_power_base(self):
        return self._magical_critical_power_base

    @magical_critical_power_base.setter
    def magical_critical_power_base(self, value):
        residual = value - self.magical_critical_power_base
        self.solar_critical_power_base += residual
        self.lunar_critical_power_base += residual
        self.neutral_critical_power_base += residual
        self.poison_critical_power_base += residual
        self._magical_critical_power_base = value

    @property
    def all_critical_power_base(self):
        return self._all_critical_power_base

    @all_critical_power_base.setter
    def all_critical_power_base(self, value):
        residual = value - self.all_critical_power_base
        self.physical_critical_power_base += residual
        self.solar_critical_power_base += residual
        self.lunar_critical_power_base += residual
        self.neutral_critical_power_base += residual
        self.poison_critical_power_base += residual
        self._all_critical_power_base = value

    @property
    def magical_critical_power_rate(self):
        return self._magical_critical_power_rate

    @magical_critical_power_rate.setter
    def magical_critical_power_rate(self, value):
        residual = value - self.magical_critical_power_rate
        self.solar_critical_power_rate += residual
        self.lunar_critical_power_rate += residual
        self.neutral_critical_power_rate += residual
        self.poison_critical_power_rate += residual
        self._magical_critical_power_rate = value

    @property
    def all_critical_power_rate(self):
        return self._all_critical_power_rate

    @all_critical_power_rate.setter
    def all_critical_power_rate(self, value):
        residual = value - self.all_critical_power_rate
        self.physical_critical_power_rate += residual
        self.solar_critical_power_rate += residual
        self.lunar_critical_power_rate += residual
        self.neutral_critical_power_rate += residual
        self.poison_critical_power_rate += residual
        self._all_critical_power_rate = value

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
        return self.physical_critical_power_percent + self.physical_critical_power_rate / BINARY_SCALE

    @property
    def solar_critical_power(self):
        return self.solar_critical_power_percent + self.solar_critical_power_rate / BINARY_SCALE

    @property
    def lunar_critical_power(self):
        return self.lunar_critical_power_percent + self.lunar_critical_power_rate / BINARY_SCALE

    @property
    def neutral_critical_power(self):
        return self.neutral_critical_power_percent + self.neutral_critical_power_rate / BINARY_SCALE

    @property
    def poison_critical_power(self):
        return self.poison_critical_power_percent + self.poison_critical_power_rate / BINARY_SCALE


class Minor:
    surplus_base: int = 0
    surplus_gain: int = 0

    strain_base: int = 0
    strain_gain: int = 0
    strain_rate: int = 0

    all_shield_ignore: int = 0

    _all_damage_addition: int = 0
    physical_damage_addition: int = 0
    magical_damage_addition: int = 0

    move_state_damage_addition: int = 0

    pve_addition_base: int = 0

    @property
    def surplus(self):
        return int(self.surplus_base * (1 + self.surplus_gain / BINARY_SCALE))

    @property
    def final_strain(self):
        return int(self.strain_base * (1 + self.strain_gain / BINARY_SCALE))

    @property
    def strain_percent(self):
        return self.final_strain / STRAIN_SCALE

    @property
    def strain(self):
        return self.strain_percent + self.strain_rate / BINARY_SCALE

    @property
    def all_damage_addition(self):
        return self._all_damage_addition

    @all_damage_addition.setter
    def all_damage_addition(self, value):
        residual = value - self.all_damage_addition
        self.physical_damage_addition += residual
        self.magical_damage_addition += residual
        self._all_damage_addition = value


class Defense:
    physical_shield_base: int = 0
    solar_shield_base: int = 0
    lunar_shield_base: int = 0
    neutral_shield_base: int = 0
    poison_shield_base: int = 0
    _magical_shield_base: int = 0

    physical_shield_gain: int = 0
    solar_shield_gain: int = 0
    lunar_shield_gain: int = 0
    neutral_shield_gain: int = 0
    poison_shield_gain: int = 0

    @property
    def magical_shield_base(self):
        return self._magical_shield_base

    @magical_shield_base.setter
    def magical_shield_base(self, value):
        residual = value - self.magical_shield_base
        self.solar_shield_base += residual
        self.lunar_shield_base += residual
        self.neutral_shield_base += residual
        self.poison_shield_base += residual
        self._magical_shield_base = value

    @property
    def physical_shield(self) -> int:
        return int(self.physical_shield_base * (1 + self.physical_shield_gain / BINARY_SCALE))

    @property
    def solar_shield(self) -> int:
        return int(self.solar_shield_base * (1 + self.solar_shield_gain / BINARY_SCALE))

    @property
    def lunar_shield(self) -> int:
        return int(self.lunar_shield_base * (1 + self.lunar_shield_gain / BINARY_SCALE))

    @property
    def neutral_shield(self) -> int:
        return int(self.neutral_shield_base * (1 + self.neutral_shield_gain / BINARY_SCALE))

    @property
    def poison_shield(self) -> int:
        return int(self.poison_shield_base * (1 + self.poison_shield_gain / BINARY_SCALE))


class DamageCof:
    physical_damage_cof: int = 0
    solar_damage_cof: int = 0
    lunar_damage_cof: int = 0
    neutral_damage_cof: int = 0
    poison_damage_cof: int = 0


class Target(Defense, DamageCof):
    level: int = 0
    global_damage_factor: int = 0

    def __getitem__(self, item):
        if item in dir(self):
            return getattr(self, item)
        return None

    def __setitem__(self, key, value):
        if key in dir(self):
            setattr(self, key, value)


class Attribute(AttackPower, CriticalStrike, Overcome, CriticalPower, Minor, Target):
    level: int = LEVEL
