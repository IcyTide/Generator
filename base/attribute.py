from .constant import *
from .expression import Ceil
from ..tools.lua.enums import SKILL_KIND_TYPE


class BaseType:
    major_type: str
    damage_type: str
    critical_type: str

    @property
    def kind_type(self):
        if self.damage_type == SKILL_KIND_TYPE.PHYSICS:
            return SKILL_KIND_TYPE.PHYSICS
        elif self.damage_type:
            return SKILL_KIND_TYPE.MAGIC
        else:
            return SKILL_KIND_TYPE.NONE

    def __init__(self, major_type: str = '', damage_type: str = '', critical_type: str = ''):
        self.major_type = major_type
        self.damage_type = damage_type
        self.critical_type = critical_type

    def __getitem__(self, item):
        if hasattr(self, item) is True:
            return getattr(self, item)
        raise KeyError(item)

    def __setitem__(self, key, value):
        if hasattr(self, key) is False:
            raise KeyError(key)
        setattr(self, key, value)

    def safe_get(self, key: str):
        return hasattr(self, key) and getattr(self, key)

    def safe_set(self, key: str, value):
        if hasattr(self, key) is True:
            setattr(self, key, value)


class BaseMajor(BaseType):
    agility_base: int = 0
    strength_base: int = 0
    spirit_base: int = 0
    spunk_base: int = 0
    vitality_base: int = 0
    all_major_base: int = 0

    @property
    def base_agility(self):
        return self.agility_base + self.all_major_base

    @property
    def base_strength(self):
        return self.strength_base + self.all_major_base

    @property
    def base_spirit(self):
        return self.spirit_base + self.all_major_base

    @property
    def base_spunk(self):
        return self.spunk_base + self.all_major_base

    @property
    def base_vitality(self):
        return self.vitality_base + self.all_major_base

    @property
    def major_base(self):
        key = f'{self.major_type}_base'
        return self.safe_get(key)

    @major_base.setter
    def major_base(self, value):
        key = f'{self.major_type}_base'
        self.safe_set(key, value)

    @property
    def base_major(self):
        key = f'base_{self.major_type}'
        return self.safe_get(key)


class MajorGain:
    agility_gain: int = 0
    strength_gain: int = 0
    spirit_gain: int = 0
    spunk_gain: int = 0
    vitality_gain: int = 0


class Major(BaseMajor, MajorGain):
    @property
    def agility(self):
        return int(self.base_agility * (1 + self.agility_gain / BINARY_SCALE))

    @property
    def strength(self):
        return int(self.base_strength * (1 + self.strength_gain / BINARY_SCALE))

    @property
    def spirit(self):
        return int(self.base_spirit * (1 + self.spirit_gain / BINARY_SCALE))

    @property
    def spunk(self):
        return int(self.base_spunk * (1 + self.spunk_gain / BINARY_SCALE))

    @property
    def vitality(self):
        return int(self.base_vitality * (1 + self.vitality_gain / BINARY_SCALE))

    @property
    def major(self):
        return self.safe_get(self.major_type)


class BaseAttackPower(Major):
    physical_attack_power_base: int = 0
    solar_attack_power_base: int = 0
    lunar_attack_power_base: int = 0
    solar_and_lunar_attack_power_base: int = 0
    neutral_attack_power_base: int = 0
    poison_attack_power_base: int = 0
    magical_attack_power_base: int = 0
    all_attack_power_base: int = 0

    @property
    def base_physical_attack_power(self):
        base_attack_power = self.physical_attack_power_base + self.all_attack_power_base
        return base_attack_power + int(self.strength * STRENGTH_TO_ATTACK_POWER)

    @property
    def base_magical_attack_power(self):
        base_attack_power = self.magical_attack_power_base + self.all_attack_power_base
        return base_attack_power + int(self.spunk * SPUNK_TO_ATTACK_POWER)

    @property
    def base_solar_attack_power(self):
        base_attack_power = self.solar_attack_power_base + self.solar_and_lunar_attack_power_base
        return base_attack_power + self.magical_attack_power_base

    @property
    def base_lunar_attack_power(self):
        base_attack_power = self.lunar_attack_power_base + self.solar_and_lunar_attack_power_base
        return base_attack_power + self.base_solar_attack_power

    @property
    def base_neutral_attack_power(self):
        return self.neutral_attack_power_base + self.base_magical_attack_power

    @property
    def base_poison_attack_power(self):
        return self.poison_attack_power_base + self.base_magical_attack_power


class ExtraAttackPower(Major):
    agility_to_physical_attack_power: int = 0
    strength_to_physical_attack_power: int = 0

    spunk_to_solar_attack_power: int = 0
    spirit_to_lunar_attack_power: int = 0
    spunk_to_solar_and_lunar_attack_power: int = 0
    spunk_to_neutral_attack_power: int = 0
    spirit_to_neutral_attack_power: int = 0
    spunk_to_poison_attack_power: int = 0
    spirit_to_poison_attack_power: int = 0

    vitality_to_physical_attack_power: int = 0
    vitality_to_solar_attack_power: int = 0
    vitality_to_lunar_attack_power: int = 0

    @property
    def extra_physical_attack_power(self):
        extra_attack_power = int(self.agility * self.agility_to_physical_attack_power / BINARY_SCALE)
        extra_attack_power += int(self.strength * self.strength_to_physical_attack_power / BINARY_SCALE)
        extra_attack_power += int(self.vitality * self.vitality_to_physical_attack_power / BINARY_SCALE)
        return extra_attack_power

    @property
    def extra_solar_attack_power(self):
        extra_attack_power = int(self.spunk * self.spunk_to_solar_attack_power / BINARY_SCALE)
        extra_attack_power += int(self.spunk * self.spunk_to_solar_and_lunar_attack_power / BINARY_SCALE)
        extra_attack_power += int(self.vitality * self.vitality_to_solar_attack_power / BINARY_SCALE)
        return extra_attack_power

    @property
    def extra_lunar_attack_power(self):
        extra_attack_power = int(self.spirit * self.spirit_to_lunar_attack_power / BINARY_SCALE)
        extra_attack_power += int(self.spunk * self.spunk_to_solar_and_lunar_attack_power / BINARY_SCALE)
        extra_attack_power += int(self.vitality * self.vitality_to_lunar_attack_power / BINARY_SCALE)
        return extra_attack_power

    @property
    def extra_neutral_attack_power(self):
        extra_attack_power = int(self.spunk * self.spunk_to_neutral_attack_power / BINARY_SCALE)
        extra_attack_power += int(self.spirit * self.spirit_to_neutral_attack_power / BINARY_SCALE)
        return extra_attack_power

    @property
    def extra_poison_attack_power(self):
        extra_attack_power = int(self.spunk * self.spunk_to_poison_attack_power / BINARY_SCALE)
        extra_attack_power += int(self.spirit * self.spirit_to_poison_attack_power / BINARY_SCALE)
        return extra_attack_power

    @property
    def base_attack_power(self):
        key = f'base_{self.damage_type}_attack_power'
        return self.safe_get(key)


class AttackPowerGain(BaseType):
    physical_attack_power_gain: int = 0
    solar_attack_power_gain: int = 0
    lunar_attack_power_gain: int = 0
    neutral_attack_power_gain: int = 0
    poison_attack_power_gain: int = 0
    _magical_attack_power_gain: int = 0

    @property
    def magical_attack_power_gain(self):
        return self._magical_attack_power_gain

    @magical_attack_power_gain.setter
    def magical_attack_power_gain(self, value):
        residual = value - self._magical_attack_power_gain
        self.solar_attack_power_gain += residual
        self.lunar_attack_power_gain += residual
        self.neutral_attack_power_gain += residual
        self.poison_attack_power_gain += residual
        self._magical_attack_power_gain = value

    @property
    def attack_power_gain(self):
        key = f'{self.damage_type}_attack_power_gain'
        return self.safe_get(key)


class AttackPower(BaseAttackPower, ExtraAttackPower, AttackPowerGain):
    @property
    def physical_attack_power(self):
        attack_power = int(self.base_physical_attack_power * (1 + self.physical_attack_power_gain / BINARY_SCALE))
        return attack_power + self.extra_physical_attack_power

    @property
    def solar_attack_power(self):
        attack_power = int(self.base_solar_attack_power * (1 + self.solar_attack_power_gain / BINARY_SCALE))
        return attack_power + self.extra_solar_attack_power

    @property
    def lunar_attack_power(self):
        attack_power = int(self.base_lunar_attack_power * (1 + self.lunar_attack_power_gain / BINARY_SCALE))
        return attack_power + self.extra_lunar_attack_power

    @property
    def neutral_attack_power(self):
        attack_power = int(self.base_neutral_attack_power * (1 + self.neutral_attack_power_gain / BINARY_SCALE))
        return attack_power + self.extra_neutral_attack_power

    @property
    def poison_attack_power(self):
        attack_power = int(self.base_poison_attack_power * (1 + self.poison_attack_power_gain / BINARY_SCALE))
        return attack_power + self.extra_poison_attack_power

    @property
    def attack_power(self):
        key = f'{self.damage_type}_attack_power'
        return self.safe_get(key)


class BaseCriticalStrike(Major):
    physical_critical_strike_base: int = 0
    solar_critical_strike_base: int = 0
    lunar_critical_strike_base: int = 0
    solar_and_lunar_critical_strike_base: int = 0
    neutral_critical_strike_base: int = 0
    poison_critical_strike_base: int = 0
    magical_critical_strike_base: int = 0
    all_critical_strike_base: int = 0

    @property
    def critical_strike_base(self):
        return self.safe_get(f'{self.critical_type}_critical_strike_base')

    @critical_strike_base.setter
    def critical_strike_base(self, value):
        return self.safe_set(f'{self.critical_type}_critical_strike_base', value)

    @property
    def base_physical_critical_strike(self):
        base_critical_strike = self.physical_critical_strike_base + self.all_critical_strike_base
        return base_critical_strike + int(self.agility * AGILITY_TO_CRITICAL_STRIKE / BINARY_SCALE)

    @property
    def base_magical_critical_strike(self):
        base_critical_strike = self.magical_critical_strike_base + self.all_critical_strike_base
        return base_critical_strike + int(self.spirit * SPIRIT_TO_CRITICAL_STRIKE / BINARY_SCALE)

    @property
    def base_solar_critical_strike(self):
        base_critical_strike = self.solar_critical_strike_base + self.solar_and_lunar_critical_strike_base
        return base_critical_strike + self.base_magical_critical_strike

    @property
    def base_lunar_critical_strike(self):
        base_critical_strike = self.lunar_critical_strike_base + self.solar_and_lunar_critical_strike_base
        return base_critical_strike + self.base_magical_critical_strike

    @property
    def base_neutral_critical_strike(self):
        return self.neutral_critical_strike_base + self.base_magical_critical_strike

    @property
    def base_poison_critical_strike(self):
        return self.poison_critical_strike_base + self.base_magical_critical_strike

    @property
    def base_critical_strike(self):
        key = f'{self.critical_type}_critical_strike_base'
        return self.safe_get(key)


class ExtraCriticalStrike(Major):
    agility_to_physical_critical_strike: int = 0
    strength_to_physical_critical_strike: int = 0
    spunk_to_physical_critical_strike: int = 0

    spunk_to_solar_critical_strike: int = 0
    spirit_to_lunar_critical_strike: int = 0
    spunk_to_solar_and_lunar_critical_strike: int = 0
    spunk_to_neutral_critical_strike: int = 0
    spirit_to_neutral_critical_strike: int = 0
    spirit_to_poison_critical_strike: int = 0

    vitality_to_magical_critical_strike: int = 0

    @property
    def extra_physical_critical_strike(self):
        extra_critical_strike = int(self.agility * self.agility_to_physical_critical_strike / BINARY_SCALE)
        extra_critical_strike += int(self.strength * self.strength_to_physical_critical_strike / BINARY_SCALE)
        extra_critical_strike += int(self.spunk * self.spunk_to_physical_critical_strike / BINARY_SCALE)
        return extra_critical_strike

    @property
    def extra_magical_critical_strike(self):
        extra_critical_strike = int(self.vitality * self.vitality_to_magical_critical_strike / BINARY_SCALE)
        return extra_critical_strike

    @property
    def extra_solar_critical_strike(self):
        extra_critical_strike = int(self.spunk * self.spunk_to_solar_critical_strike / BINARY_SCALE)
        extra_critical_strike += int(self.spunk * self.spunk_to_solar_and_lunar_critical_strike / BINARY_SCALE)
        return extra_critical_strike + self.extra_magical_critical_strike

    @property
    def extra_lunar_critical_strike(self):
        extra_critical_strike = int(self.spirit * self.spirit_to_lunar_critical_strike / BINARY_SCALE)
        extra_critical_strike += int(self.spunk * self.spunk_to_solar_and_lunar_critical_strike / BINARY_SCALE)
        return extra_critical_strike + self.extra_magical_critical_strike

    @property
    def extra_neutral_critical_strike(self):
        extra_critical_strike = int(self.spirit * self.spirit_to_neutral_critical_strike / BINARY_SCALE)
        extra_critical_strike += int(self.spunk * self.spunk_to_neutral_critical_strike / BINARY_SCALE)
        return extra_critical_strike + self.extra_magical_critical_strike

    @property
    def extra_poison_critical_strike(self):
        extra_critical_strike = int(self.spirit * self.spirit_to_poison_critical_strike / BINARY_SCALE)
        return extra_critical_strike + self.extra_magical_critical_strike


class FinalCriticalStrike(BaseCriticalStrike, ExtraCriticalStrike):
    @property
    def final_physical_critical_strike(self):
        return self.base_physical_critical_strike + self.extra_physical_critical_strike

    @property
    def final_solar_critical_strike(self):
        return self.base_solar_critical_strike + self.extra_solar_critical_strike

    @property
    def final_lunar_critical_strike(self):
        return self.base_lunar_critical_strike + self.extra_lunar_critical_strike

    @property
    def final_neutral_critical_strike(self):
        return self.base_neutral_critical_strike + self.extra_neutral_critical_strike

    @property
    def final_poison_critical_strike(self):
        return self.base_poison_critical_strike + self.extra_poison_critical_strike

    @property
    def final_critical_strike(self):
        key = f'final_{self.critical_type}_critical_strike'
        return self.safe_get(key)


class CriticalStrikePercent(FinalCriticalStrike):
    @property
    def physical_critical_strike_percent(self):
        critical_strike_percent = self.final_physical_critical_strike / CRITICAL_STRIKE_SCALE
        return int(critical_strike_percent * DECIMAL_SCALE) / DECIMAL_SCALE

    @property
    def solar_critical_strike_percent(self):
        critical_strike_percent = self.final_solar_critical_strike / CRITICAL_STRIKE_SCALE
        return int(critical_strike_percent * DECIMAL_SCALE) / DECIMAL_SCALE

    @property
    def lunar_critical_strike_percent(self):
        critical_strike_percent = self.final_lunar_critical_strike / CRITICAL_STRIKE_SCALE
        return int(critical_strike_percent * DECIMAL_SCALE) / DECIMAL_SCALE

    @property
    def neutral_critical_strike_percent(self):
        critical_strike_percent = self.final_neutral_critical_strike / CRITICAL_STRIKE_SCALE
        return int(critical_strike_percent * DECIMAL_SCALE) / DECIMAL_SCALE

    @property
    def poison_critical_strike_percent(self):
        critical_strike_percent = self.final_poison_critical_strike / CRITICAL_STRIKE_SCALE
        return int(critical_strike_percent * DECIMAL_SCALE) / DECIMAL_SCALE

    @property
    def critical_strike_percent(self):
        key = f'{self.critical_type}_critical_strike_percent'
        return self.safe_get(key)


class CriticalStrikeRate(BaseType):
    physical_critical_strike_rate: int = 0
    solar_critical_strike_rate: int = 0
    lunar_critical_strike_rate: int = 0
    neutral_critical_strike_rate: int = 0
    poison_critical_strike_rate: int = 0

    @property
    def critical_strike_rate(self):
        return self.safe_get(f'{self.critical_type}_critical_strike_rate')


class CriticalStrike(CriticalStrikePercent, CriticalStrikeRate):
    @property
    def physical_critical_strike(self):
        critical_strike = self.physical_critical_strike_percent + self.physical_critical_strike_rate / DECIMAL_SCALE
        return critical_strike

    @property
    def solar_critical_strike(self):
        critical_strike = self.solar_critical_strike_percent + self.solar_critical_strike_rate / DECIMAL_SCALE
        return critical_strike

    @property
    def lunar_critical_strike(self):
        critical_strike = self.lunar_critical_strike_percent + self.lunar_critical_strike_rate / DECIMAL_SCALE
        return critical_strike

    @property
    def neutral_critical_strike(self):
        critical_strike = self.neutral_critical_strike_percent + self.neutral_critical_strike_rate / DECIMAL_SCALE
        return critical_strike

    @property
    def poison_critical_strike(self):
        critical_strike = self.poison_critical_strike_percent + self.poison_critical_strike_rate / DECIMAL_SCALE
        return critical_strike

    @property
    def critical_strike(self):
        return self.safe_get(f'{self.critical_type}_critical_strike')


class BaseOvercome(Major):
    physical_overcome_base: int = 0
    solar_overcome_base: int = 0
    lunar_overcome_base: int = 0
    solar_and_lunar_overcome_base: int = 0
    neutral_overcome_base: int = 0
    poison_overcome_base: int = 0
    magical_overcome_base: int = 0
    all_overcome_base: int = 0

    @property
    def overcome_base(self):
        return self.safe_get(f'{self.damage_type}_overcome_base')

    @overcome_base.setter
    def overcome_base(self, value):
        self.safe_set(f'{self.damage_type}_overcome_base', value)

    @property
    def base_physical_overcome(self):
        base_overcome = self.physical_overcome_base + self.all_overcome_base
        return base_overcome + int(self.strength * STRENGTH_TO_OVERCOME)

    @property
    def base_magical_overcome(self):
        base_overcome = self.magical_overcome_base + self.all_overcome_base
        return base_overcome + int(self.spunk * SPUNK_TO_OVERCOME)

    @property
    def base_solar_overcome(self):
        base_overcome = self.solar_overcome_base + self.solar_and_lunar_overcome_base
        return base_overcome + self.base_magical_overcome

    @property
    def base_lunar_overcome(self):
        base_overcome = self.lunar_overcome_base + self.solar_and_lunar_overcome_base
        return base_overcome + self.base_magical_overcome

    @property
    def base_neutral_overcome(self):
        return self.neutral_overcome_base + self.base_magical_overcome

    @property
    def base_poison_overcome(self):
        return self.poison_overcome_base + self.base_magical_overcome

    @property
    def base_overcome(self):
        return self.safe_get(f'base_{self.damage_type}_overcome')


class ExtraOvercome(Major):
    agility_to_physical_overcome: int = 0
    strength_to_physical_overcome: int = 0
    spunk_to_neutral_overcome: int = 0
    spirit_to_poison_overcome: int = 0

    vitality_to_physical_overcome: int = 0
    vitality_to_magical_overcome: int = 0

    @property
    def extra_physical_overcome(self):
        extra_overcome = int(self.agility * self.agility_to_physical_overcome / BINARY_SCALE)
        extra_overcome += int(self.strength * self.strength_to_physical_overcome / BINARY_SCALE)
        extra_overcome += int(self.vitality * self.vitality_to_physical_overcome / BINARY_SCALE)
        return extra_overcome

    @property
    def extra_magical_overcome(self):
        extra_overcome = int(self.vitality * self.vitality_to_magical_overcome / BINARY_SCALE)
        return extra_overcome

    @property
    def extra_solar_overcome(self):
        return self.extra_magical_overcome

    @property
    def extra_lunar_overcome(self):
        return self.extra_magical_overcome

    @property
    def extra_neutral_overcome(self):
        extra_overcome = int(self.spunk * self.spunk_to_neutral_overcome / BINARY_SCALE)
        return extra_overcome + self.extra_magical_overcome

    @property
    def extra_poison_overcome(self):
        extra_overcome = int(self.spirit * self.spirit_to_poison_overcome / BINARY_SCALE)
        return extra_overcome + self.extra_magical_overcome


class OvercomeGain:
    physical_overcome_gain: int = 0
    solar_overcome_gain: int = 0
    lunar_overcome_gain: int = 0
    neutral_overcome_gain: int = 0
    poison_overcome_gain: int = 0


class FinalOvercome(BaseOvercome, ExtraOvercome, OvercomeGain):
    @property
    def final_physical_overcome(self):
        final_overcome = int(self.base_physical_overcome * (1 + self.physical_overcome_gain / BINARY_SCALE))
        return final_overcome + self.extra_physical_overcome

    @property
    def final_solar_overcome(self):
        final_overcome = int(self.base_solar_overcome * (1 + self.solar_overcome_gain / BINARY_SCALE))
        return final_overcome + self.extra_solar_overcome

    @property
    def final_lunar_overcome(self):
        final_overcome = int(self.base_lunar_overcome * (1 + self.lunar_overcome_gain / BINARY_SCALE))
        return final_overcome + self.extra_lunar_overcome

    @property
    def final_neutral_overcome(self):
        final_overcome = int(self.base_neutral_overcome * (1 + self.neutral_overcome_gain / BINARY_SCALE))
        return final_overcome + self.extra_neutral_overcome

    @property
    def final_poison_overcome(self):
        final_overcome = int(self.base_poison_overcome * (1 + self.poison_overcome_gain / BINARY_SCALE))
        return final_overcome + self.extra_poison_overcome

    @property
    def final_overcome(self):
        return self.safe_get(f'final_{self.damage_type}_overcome')


class Overcome(FinalOvercome):
    @property
    def physical_overcome(self):
        overcome = self.final_physical_overcome / OVERCOME_SCALE
        return int(overcome * BINARY_SCALE) / BINARY_SCALE

    @property
    def solar_overcome(self):
        overcome = self.final_solar_overcome / OVERCOME_SCALE
        return int(overcome * BINARY_SCALE) / BINARY_SCALE

    @property
    def lunar_overcome(self):
        overcome = self.final_lunar_overcome / OVERCOME_SCALE
        return int(overcome * BINARY_SCALE) / BINARY_SCALE

    @property
    def neutral_overcome(self):
        overcome = self.final_neutral_overcome / OVERCOME_SCALE
        return int(overcome * BINARY_SCALE) / BINARY_SCALE

    @property
    def poison_overcome(self):
        overcome = self.final_poison_overcome / OVERCOME_SCALE
        return int(overcome * BINARY_SCALE) / BINARY_SCALE

    @property
    def overcome(self):
        return self.safe_get(f'{self.damage_type}_overcome')


class BaseCriticalPower(BaseType):
    physical_critical_power_base: int = 0
    solar_critical_power_base: int = 0
    lunar_critical_power_base: int = 0
    solar_and_lunar_critical_power_base: int = 0
    neutral_critical_power_base: int = 0
    poison_critical_power_base: int = 0
    magical_critical_power_base: int = 0
    all_critical_power_base: int = 0

    @property
    def critical_power_base(self):
        return self.safe_get(f'{self.critical_type}_critical_power_base')

    @critical_power_base.setter
    def critical_power_base(self, value):
        self.safe_set(f'{self.critical_type}_critical_power_base', value)

    @property
    def base_physical_critical_power(self):
        return self.physical_critical_power_base + self.all_critical_power_base

    @property
    def base_magical_critical_power(self):
        return self.magical_critical_power_base + self.all_critical_power_base

    @property
    def base_solar_critical_power(self):
        critical_power = self.solar_critical_power_base + self.solar_and_lunar_critical_power_base
        return critical_power + self.base_magical_critical_power

    @property
    def base_lunar_critical_power(self):
        critical_power = self.lunar_critical_power_base + self.solar_and_lunar_critical_power_base
        return critical_power + self.base_magical_critical_power

    @property
    def base_neutral_critical_power(self):
        return self.neutral_critical_power_base + self.base_magical_critical_power

    @property
    def base_poison_critical_power(self):
        return self.poison_critical_power_base + self.base_magical_critical_power

    @property
    def base_critical_power(self):
        return self.safe_get(f'base_{self.critical_type}_critical_power')


class CriticalPowerPercent(BaseCriticalPower):
    @property
    def physical_critical_power_percent(self):
        critical_power_percent = self.base_physical_critical_power / CRITICAL_POWER_SCALE
        return int(critical_power_percent * BINARY_SCALE) / BINARY_SCALE

    @property
    def solar_critical_power_percent(self):
        critical_power_percent = self.base_solar_critical_power / CRITICAL_POWER_SCALE
        return int(critical_power_percent * BINARY_SCALE) / BINARY_SCALE

    @property
    def lunar_critical_power_percent(self):
        critical_power_percent = self.base_lunar_critical_power / CRITICAL_POWER_SCALE
        return int(critical_power_percent * BINARY_SCALE) / BINARY_SCALE

    @property
    def neutral_critical_power_percent(self):
        critical_power_percent = self.base_neutral_critical_power / CRITICAL_POWER_SCALE
        return int(critical_power_percent * BINARY_SCALE) / BINARY_SCALE

    @property
    def poison_critical_power_percent(self):
        critical_power_percent = self.base_poison_critical_power / CRITICAL_POWER_SCALE
        return int(critical_power_percent * BINARY_SCALE) / BINARY_SCALE

    @property
    def critical_power_percent(self):
        return self.safe_get(f'{self.critical_type}_critical_power_percent')


class CriticalPowerRate(BaseType):
    physical_critical_power_rate: int = 0
    solar_critical_power_rate: int = 0
    lunar_critical_power_rate: int = 0
    neutral_critical_power_rate: int = 0
    poison_critical_power_rate: int = 0
    _magical_critical_power_rate: int = 0
    _all_critical_power_rate: int = 0
    unlimit_critical_power_rate: int = 0

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
        self.magical_critical_power_rate += residual
        self._all_critical_power_rate = value


class CriticalPower(CriticalPowerPercent, CriticalPowerRate):
    @property
    def physical_critical_power(self):
        critical_power = self.physical_critical_power_percent + self.physical_critical_power_rate / BINARY_SCALE
        critical_power = min(critical_power, MAX_CRITICAL_POWER)
        return critical_power + self.unlimit_critical_power_rate / BINARY_SCALE

    @property
    def solar_critical_power(self):
        critical_power = self.solar_critical_power_percent + self.solar_critical_power_rate / BINARY_SCALE
        critical_power = min(critical_power, MAX_CRITICAL_POWER)
        return critical_power + self.unlimit_critical_power_rate / BINARY_SCALE

    @property
    def lunar_critical_power(self):
        critical_power = self.lunar_critical_power_percent + self.lunar_critical_power_rate / BINARY_SCALE
        critical_power = min(critical_power, MAX_CRITICAL_POWER)
        return critical_power + self.unlimit_critical_power_rate / BINARY_SCALE

    @property
    def neutral_critical_power(self):
        critical_power = self.neutral_critical_power_percent + self.neutral_critical_power_rate / BINARY_SCALE
        critical_power = min(critical_power, MAX_CRITICAL_POWER)
        return critical_power + self.unlimit_critical_power_rate / BINARY_SCALE

    @property
    def poison_critical_power(self):
        critical_power = self.poison_critical_power_percent + self.poison_critical_power_rate / BINARY_SCALE
        critical_power = min(critical_power, MAX_CRITICAL_POWER)
        return critical_power + self.unlimit_critical_power_rate / BINARY_SCALE

    @property
    def critical_power(self):
        return self.safe_get(f'{self.critical_type}_critical_power')


class BaseShield:
    physical_shield_base: int = 0
    solar_shield_base: int = 0
    lunar_shield_base: int = 0
    neutral_shield_base: int = 0
    poison_shield_base: int = 0
    magical_shield_base: int = 0

    @property
    def base_physical_shield(self):
        return self.physical_shield_base

    @property
    def base_magical_shield(self):
        return self.magical_shield_base

    @property
    def base_solar_shield(self):
        return self.solar_shield_base + self.base_magical_shield

    @property
    def base_lunar_shield(self):
        return self.lunar_shield_base + self.base_magical_shield

    @property
    def base_neutral_shield(self):
        return self.neutral_shield_base + self.base_magical_shield

    @property
    def base_poison_shield(self):
        return self.poison_shield_base + self.base_magical_shield


class ExtraShield(Major):
    physical_shield_add: int = 0

    vitality_to_physical_shield: int = 0
    vitality_to_magical_shield: int = 0

    @property
    def extra_physical_shield(self):
        extra_shield = int(self.vitality * self.vitality_to_physical_shield / BINARY_SCALE)
        return extra_shield + self.physical_shield_add

    @property
    def extra_magical_shield(self):
        extra_shield = int(self.vitality * self.vitality_to_magical_shield / BINARY_SCALE)
        return extra_shield

    @property
    def extra_solar_shield(self):
        return self.extra_magical_shield

    @property
    def extra_lunar_shield(self):
        return self.extra_magical_shield

    @property
    def extra_neutral_shield(self):
        return self.extra_magical_shield

    @property
    def extra_poison_shield(self):
        return self.extra_magical_shield


class ShieldGain(BaseType):
    physical_shield_gain: int = 0
    solar_shield_gain: int = 0
    lunar_shield_gain: int = 0
    neutral_shield_gain: int = 0
    poison_shield_gain: int = 0

    @property
    def shield_gain(self):
        return self.safe_get(f'{self.damage_type}_shield_gain')


class Shield(BaseShield, ExtraShield, ShieldGain):
    @property
    def physical_shield(self):
        final_shield = int(self.base_physical_shield * (1 + self.physical_shield_gain / BINARY_SCALE))
        return max(final_shield, 0) + self.extra_physical_shield

    @property
    def solar_shield(self):
        final_shield = int(self.base_solar_shield * (1 + self.solar_shield_gain / BINARY_SCALE))
        return max(final_shield, 0) + self.extra_magical_shield

    @property
    def lunar_shield(self):
        final_shield = int(self.base_lunar_shield * (1 + self.lunar_shield_gain / BINARY_SCALE))
        return max(final_shield, 0) + self.extra_magical_shield

    @property
    def neutral_shield(self):
        final_shield = int(self.base_neutral_shield * (1 + self.neutral_shield_gain / BINARY_SCALE))
        return max(final_shield, 0) + self.extra_magical_shield

    @property
    def poison_shield(self):
        final_shield = int(self.base_poison_shield * (1 + self.poison_shield_gain / BINARY_SCALE))
        return max(final_shield, 0) + self.extra_magical_shield

    @property
    def magical_shield(self):
        return max(self.solar_shield, self.lunar_shield, self.neutral_shield, self.poison_shield)


class DamageBase(BaseType):
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

    @property
    def damage_base(self):
        return self.safe_get(f'{self.damage_type}_damage_base')

    @damage_base.setter
    def damage_base(self, value):
        self.safe_set(f'{self.damage_type}_damage_base', value)

    @property
    def damage_rand(self):
        return self.safe_get(f'{self.damage_type}_damage_rand')

    @damage_rand.setter
    def damage_rand(self, value):
        self.safe_set(f'{self.damage_type}_damage_rand', value)


class DamageCof(BaseType):
    physical_damage_cof: int = 0
    solar_damage_cof: int = 0
    lunar_damage_cof: int = 0
    neutral_damage_cof: int = 0
    poison_damage_cof: int = 0

    adaptive_damage_cof: int = 0

    coming_damage_cof: int = 0

    skill_damage_final_cof: int = 0
    pve_damage_cof: int = 0

    @property
    def damage_cof(self):
        return self.safe_get(f'{self.damage_type}_damage_cof')

    @property
    def physical_damage_scale(self):
        return (self.physical_damage_cof + Ceil(self.coming_damage_cof)) / BINARY_SCALE

    @property
    def solar_damage_scale(self):
        return (self.solar_damage_cof + Ceil(self.coming_damage_cof)) / BINARY_SCALE

    @property
    def lunar_damage_scale(self):
        return (self.lunar_damage_cof + Ceil(self.coming_damage_cof)) / BINARY_SCALE

    @property
    def neutral_damage_scale(self):
        return (self.neutral_damage_cof + Ceil(self.coming_damage_cof)) / BINARY_SCALE

    @property
    def poison_damage_scale(self):
        return (self.poison_damage_cof + Ceil(self.coming_damage_cof)) / BINARY_SCALE

    @property
    def damage_scale(self):
        return self.safe_get(f'{self.damage_type}_damage_scale')

    @property
    def pve_damage_addition(self):
        return self.pve_damage_cof / BINARY_SCALE

    @property
    def skill_damage_final_addition(self):
        return self.skill_damage_final_cof / BINARY_SCALE


class WeaponDamage:
    weapon_damage_base: int = 0
    weapon_damage_rand: int = 0
    weapon_damage_gain: int = 0

    @property
    def weapon_damage(self):
        return int(self.weapon_damage_base * (1 + self.weapon_damage_gain / BINARY_SCALE))


class Haste:
    haste_base: int = 0
    haste_rate: int = 0
    unlimit_haste_rate: int = 0

    @property
    def haste_percent(self):
        haste_percent = self.haste_base / HASTE_SCALE
        return int(haste_percent * BINARY_SCALE) / BINARY_SCALE

    @property
    def haste(self):
        haste = self.haste_percent + self.haste_rate / BINARY_SCALE
        haste = min(haste, MAX_HASTE)
        return haste + self.unlimit_haste_rate / BINARY_SCALE


class Surplus:
    surplus_base: int = 0
    surplus_gain: int = 0

    @property
    def surplus(self):
        return int(self.surplus_base * (1 + self.surplus_gain / BINARY_SCALE))


class Strain:
    strain_base: int = 0
    strain_gain: int = 0
    strain_rate: int = 0

    @property
    def final_strain(self):
        return int(self.strain_base * (1 + self.strain_gain / BINARY_SCALE))

    @property
    def strain_percent(self):
        strain_percent = self.final_strain / STRAIN_SCALE
        return int(strain_percent * BINARY_SCALE) / BINARY_SCALE

    @property
    def strain(self):
        return self.strain_percent + self.strain_rate / BINARY_SCALE


class Dodge(Major):
    dodge_base: int = 0
    dodge_rate: int = 0

    vitality_to_dodge: int = 0

    @property
    def extra_dodge(self):
        extra_dodge = int(self.vitality * self.vitality_to_dodge / BINARY_SCALE)
        return extra_dodge

    @property
    def final_dodge(self):
        return self.dodge_base + self.extra_dodge

    @property
    def dodge_percent(self):
        dodge_percent = self.final_dodge / (self.final_dodge + DODGE_CONSTANT)
        return int(dodge_percent * DECIMAL_SCALE) / DECIMAL_SCALE

    @property
    def dodge(self):
        return self.dodge_percent + self.dodge_rate / DECIMAL_SCALE


class Parry(Major):
    parry_base: int = 0
    parry_gain: int = 0
    parry_rate: int = 0

    parry_value_base: int = 0
    parry_value_gain: int = 0

    agility_to_parry: int = 0
    vitality_to_parry: int = 0
    agility_to_parry_value: int = 0
    vitality_to_parry_value: int = 0

    @property
    def extra_parry(self):
        extra_parry = int(self.agility * self.agility_to_parry / BINARY_SCALE)
        extra_parry += int(self.vitality * self.vitality_to_parry / BINARY_SCALE)
        return extra_parry

    @property
    def final_parry(self):
        return int(self.parry_base * (1 + self.parry_gain / BINARY_SCALE)) + self.extra_parry

    @property
    def parry_percent(self):
        parry_percent = self.final_parry / (self.final_parry + PARRY_CONSTANT)
        return int(parry_percent * DECIMAL_SCALE) / DECIMAL_SCALE

    @property
    def parry(self):
        return self.parry_percent + self.parry_rate / DECIMAL_SCALE

    @property
    def extra_parry_value(self):
        extra_parry_value = int(self.agility * self.agility_to_parry_value / BINARY_SCALE)
        extra_parry_value += int(self.vitality * self.vitality_to_parry_value / BINARY_SCALE)
        return extra_parry_value

    @property
    def parry_value(self):
        return int(self.parry_value_base * (1 + self.parry_value_gain / BINARY_SCALE)) + self.extra_parry_value


class TherapyPower(Major):
    therapy_power_base: int = 0
    therapy_power_gain: int = 0

    spirit_to_therapy_power: int = 0

    @property
    def extra_therapy_power(self):
        return int(self.spirit * self.spirit_to_therapy_power / BINARY_SCALE)

    @property
    def therapy_power(self):
        therapy = int(self.therapy_power_base * (1 + self.therapy_power_gain / BINARY_SCALE))
        return therapy + self.extra_therapy_power


class Life(Major):
    max_life_base: int = 0
    max_life_add: int = 0
    max_life_gain: int = 0
    max_life_final_gain: int = 0

    vitality_to_max_life: int = 0

    @property
    def base_max_life(self):
        return self.max_life_base + self.vitality * VITALITY_TO_MAX_LIFE

    @property
    def extra_max_life(self):
        extra_max_life = int(self.vitality * self.vitality_to_max_life / BINARY_SCALE)
        return extra_max_life + self.max_life_add

    @property
    def final_max_life(self):
        max_life = int(self.base_max_life * (1 + self.max_life_gain / BINARY_SCALE))
        return max_life + self.extra_max_life

    @property
    def max_life(self):
        return int(self.final_max_life * (1 + self.max_life_final_gain / BINARY_SCALE))


class Mana(Major): ...


class DecriticalPower:
    decritical_power_base: int = 0
    decritical_power_gain: int = 0
    decritical_power_rate: int = 0

    @property
    def final_decritical_power(self):
        return int(self.decritical_power_base * (1 + self.decritical_power_gain / BINARY_SCALE))

    @property
    def decritical_power_percent_inner(self):
        fval = self.final_decritical_power
        total_val = fval + DECRITICAL_POWER_SCALE
        decritical_power_percent = fval / total_val
        return int(decritical_power_percent * BINARY_SCALE) / BINARY_SCALE

    @property
    def decritical_power_percent(self):
        return int(self.decritical_power_percent_inner * DECIMAL_SCALE) / DECIMAL_SCALE

    @property
    def decritical_power(self):
        val = self.decritical_power_percent_inner + self.decritical_power_rate / BINARY_SCALE
        return int(val * DECIMAL_SCALE) / DECIMAL_SCALE


class Toughness:
    toughness_base: int = 0
    toughness_gain: int = 0
    toughness_rate: int = 0

    @property
    def final_toughness(self):
        return int(self.toughness_base * (1 + self.toughness_gain / BINARY_SCALE))

    @property
    def toughness_percent(self):
        toughness_percent = self.final_toughness / TOUGHNESS_SCALE
        return int(toughness_percent * DECIMAL_SCALE) / DECIMAL_SCALE

    @property
    def toughness(self):
        return self.toughness_percent + self.toughness_rate / DECIMAL_SCALE


class Other:
    _all_damage_gain: int = 0
    physical_damage_gain: int = 0
    magical_damage_gain: int = 0

    move_state_damage_gain: int = 0

    all_shield_ignore: int = 0

    global_damage_factor: int = 0

    resist_critical_strike_rate: int = 0

    @property
    def all_damage_gain(self):
        return self._all_damage_gain

    @all_damage_gain.setter
    def all_damage_gain(self, value):
        residual = value - self._all_damage_gain
        self.physical_damage_gain += residual
        self.magical_damage_gain += residual
        self._all_damage_gain = value

    @property
    def physical_damage_addition(self):
        return self.physical_damage_gain / BINARY_SCALE

    @property
    def magical_damage_addition(self):
        return self.magical_damage_gain / BINARY_SCALE

    @property
    def move_state_damage_addition(self):
        return self.move_state_damage_gain / BINARY_SCALE

    @property
    def global_damage_scale(self):
        return (int(self.global_damage_factor) + (1 << 20)) / (1 << 20)

    @property
    def resist_critical_strike(self):
        return self.resist_critical_strike_rate / DECIMAL_SCALE


class BaseAttribute(
    AttackPower,
    CriticalStrike,
    Overcome,
    CriticalPower,
    Shield,
    DamageBase,
    DamageCof,
    WeaponDamage,
    Haste,
    Surplus,
    Strain,
    Dodge,
    Parry,
    TherapyPower,
    Life,
    Mana,
    DecriticalPower,
    Toughness,
    Other,
):
    level: int = 0

    equip_score: int = 0

    def init(self):
        self.vitality_base = BASE_VITALITY
        self.all_major_base = BASE_MAJOR
        self.all_critical_power_rate = BASE_CRITICAL_POWER
        self.physical_shield_base = BASE_PHYSICAL_SHIELD
        self.max_life_base = BASE_MAX_LIFE
        self.level = LEVEL
