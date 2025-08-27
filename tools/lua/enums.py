from enum import IntEnum, StrEnum, auto


class GLOBAL(IntEnum):
    GAME_FPS = 16


class RELATION_FORCE(IntEnum):
    CHUNYANG = auto()
    PLAYER_CHUNYANG = auto()
    WANHUA = auto()
    PLAYER_WANHUA = auto()
    QIXIU = auto()
    PLAYER_QIXIU = auto()
    TIANCE = auto()
    PLAYER_TIANCE = auto()
    SHAOLIN = auto()
    PLAYER_SHAOLIN = auto()
    CANGJIAN = auto()
    PLAYER_CANGJIAN = auto()
    WUDU = auto()
    PLAYER_WUDU = auto()
    TANGMEN = auto()
    PLAYER_TANGMEN = auto()

class ROLE_TYPE(IntEnum):
    LITTLE_BOY = auto()
    STANDARD_MALE = auto()
    LITTLE_GIRL = auto()
    STANDARD_FEMALE = auto()


class PLAYER_ARENA_TYPE(IntEnum):
    DPS = auto()


class SKILL_KIND_TYPE(StrEnum):
    PHYSICS = "physical"
    SOLAR_MAGIC = "solar"
    LUNAR_MAGIC = "lunar"
    NEUTRAL_MAGIC = "neutral"
    POISON = "poison"


class ABSORB_ATTRIBUTE_SHIELD_TYPE(IntEnum):
    GLOBAL = auto()
    PHYSICS = auto()
    SOLAR = auto()
    LUNAR = auto()
    NEUTRAL = auto()
    POISON = auto()


class ATTRIBUTE_EFFECT_MODE(IntEnum):
    EFFECT_TO_SELF_AND_ROLLBACK = auto()
    EFFECT_TO_DEST_AND_ROLLBACK = auto()
    EFFECT_TO_SELF_NOT_ROLLBACK = auto()
    EFFECT_TO_DEST_NOT_ROLLBACK = auto()


class ATTRIBUTE_TYPE(StrEnum):
    # Useless Attribute
    USELESS = ""
    KUNGFU_TYPE = ""

    ACTIVE_THREAT_COEFFICIENT = ""
    DROP_DEFENCE = ""
    BEAT_BACK_RATE = ""
    DECRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = ""

    # Resource Attribute
    ACCUMULATE = ""
    MAX_RAGE = ""
    MAX_SUN_ENERGY = ""
    MAX_MOON_ENERGY = ""

    MAX_LIFE_PERCENT_ADD = ""
    MAX_MANA_BASE = ""
    MANA_REPLENISH = ""
    MANA_REPLENISH_EXT = ""
    MANA_REPLENISH_PERCENT = ""
    MOVE_SPEED_PERCENT = ""

    # Script Attribute
    EXECUTE_SCRIPT = ""
    EXECUTE_SCRIPT_WITH_PARAM = ""
    EXECUTE_SCRIPT_SETUP = ""
    EXECUTE_SCRIPT_BULLET_TO_DEST = ""
    EXECUTE_SCRIPT_BULLET_TO_DEST_AND_ROLLBACK = ""
    CAST_SKILL = ""
    CAST_SKILL_TARGET_SELF = ""
    CAST_SKILL_TARGET_DST = ""
    CALL_BUFF = ""
    DEL_SINGLE_BUFF_BY_ID_AND_LEVEL = ""
    SKILL_EVENT_HANDLER = ""
    SET_ADAPTIVE_SKILL_TYPE = ""
    CALL_KNOCKED_DOWN = ""

    SET_TALENT_RECIPE = "recipe"
    # Damage Attribute
    SKILL_PHYSICS_DAMAGE = "physical_damage_base"
    SKILL_SOLAR_DAMAGE = "solar_damage_base"
    SKILL_LUNAR_DAMAGE = "lunar_damage_base"
    SKILL_NEUTRAL_DAMAGE = "neutral_damage_base"
    SKILL_POISON_DAMAGE = "poison_damage_base"

    SKILL_PHYSICS_DAMAGE_RAND = "physical_damage_rand"
    SKILL_SOLAR_DAMAGE_RAND = "solar_damage_rand"
    SKILL_LUNAR_DAMAGE_RAND = "lunar_damage_rand"
    SKILL_NEUTRAL_DAMAGE_RAND = "neutral_damage_rand"
    SKILL_POISON_DAMAGE_RAND = "poison_damage_rand"

    CALL_PHYSICS_DAMAGE = "call_physical_damage"
    CALL_SOLAR_DAMAGE = "call_solar_damage"
    CALL_LUNAR_DAMAGE = "call_lunar_damage"
    CALL_NEUTRAL_DAMAGE = "call_neutral_damage"
    CALL_POISON_DAMAGE = "call_poison_damage"

    CALL_SURPLUS_PHYSICS_DAMAGE = "call_physical_surplus"
    CALL_SURPLUS_SOLAR_DAMAGE = "call_solar_surplus"
    CALL_SURPLUS_LUNAR_DAMAGE = "call_lunar_surplus"
    CALL_SURPLUS_NEUTRAL_DAMAGE = "call_neutral_surplus"
    CALL_SURPLUS_POISON_DAMAGE = "call_poison_surplus"

    # Major Attribute

    # Attack Attribute
    PHYSICS_ATTACK_POWER_BASE = "physical_attack_power_base"
    SOLAR_ATTACK_POWER_BASE = "solar_attack_power_base"
    LUNAR_ATTACK_POWER_BASE = "lunar_attack_power_base"
    NEUTRAL_ATTACK_POWER_BASE = "neutral_attack_power_base"
    POISON_ATTACK_POWER_BASE = "poison_attack_power_base"

    PHYSICS_ATTACK_POWER_PERCENT = "physical_attack_power_gain"
    SOLAR_ATTACK_POWER_PERCENT = "solar_attack_power_gain"
    LUNAR_ATTACK_POWER_PERCENT = "lunar_attack_power_gain"
    NEUTRAL_ATTACK_POWER_PERCENT = "neutral_attack_power_gain"
    POISON_ATTACK_POWER_PERCENT = "poison_attack_power_gain"

    # Overcome Attribute
    PHYSICS_OVERCOME_PERCENT = "physical_overcome_gain"

    # Critical Attribute
    PHYSICS_CRITICAL_STRIKE_BASE_RATE = "physical_critical_strike_rate"
    SOLAR_CRITICAL_STRIKE_BASE_RATE = "solar_critical_strike_rate"
    LUNAR_CRITICAL_STRIKE_BASE_RATE = "lunar_critical_strike_rate"
    NEUTRAL_CRITICAL_STRIKE_BASE_RATE = "neutral_critical_strike_rate"
    POISON_CRITICAL_STRIKE_BASE_RATE = "poison_critical_strike_rate"

    PHYSICS_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = "physical_critical_power_rate"
    SOLAR_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = "solar_critical_power_rate"
    LUNAR_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = "lunar_critical_power_rate"
    NEUTRAL_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = "neutral_critical_power_rate"
    POISON_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = "poison_critical_power_rate"
    MAGIC_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = "magical_critical_power_rate"
    MAGIC_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = "magical_critical_power_rate"

    # Minor Attribute
    SURPLUS_VALUE_ADD_PERCENT = "surplus_gain"
    STRAIN_PERCENT = "strain_gain"

    # Defense Attribute
    PHYSICS_SHIELD_BASE = "physical_shield_base"
    MAGIC_SHIELD = "magical_shield_base"

    # Damage Cof Attribute
    PHYSICS_DAMAGE_COEFFICIENT = "physical_damage_cof"
    SOLAR_DAMAGE_COEFFICIENT = "solar_damage_cof"
    LUNAR_DAMAGE_COEFFICIENT = "lunar_damage_cof"
    NEUTRAL_DAMAGE_COEFFICIENT = "neutral_damage_cof"
    POISON_DAMAGE_COEFFICIENT = "poison_damage_cof"

    # Cof Attribute
    VITALITY_TO_MAX_MANA_COF = ""

    STRENGTH_TO_PHYSICS_ATTACK_POWER_COF = "strength_to_physical_attack_power"
    STRENGTH_TO_PHYSICS_OVERCOME_COF = "strength_to_physical_overcome"

    SPUNK_TO_SOLAR_AND_LUNAR_ATTACK_POWER_COF = "spunk_to_solar_and_lunar_attack_power"
    SPUNK_TO_SOLAR_AND_LUNAR_CRITICAL_STRIKE_COF = "spunk_to_solar_and_lunar_critical_strike"

    # Other Attribute
    ALL_SHIELD_IGNORE_PERCENT = "all_shield_ignore"
    ALL_DAMAGE_ADD_PERCENT = "all_damage_addition"
    DST_NPC_DAMAGE_COEFFICIENT = "pve_addition"
    GLOBAL_DAMGAGE_FACTOR = "global_damage_factor"


class BUFF_COMPARE_FLAG(IntEnum):
    EQUAL = auto()
    NOT_EQUAL = auto()
    GREATER_EQUAL = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    LESS = auto()


class SKILL_COMPARE_FLAG(IntEnum):
    EQUAL = auto()
    NOT_EQUAL = auto()
    GREATER_EQUAL = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    LESS = auto()


ENV_VARIABLES = [
    GLOBAL, RELATION_FORCE, ROLE_TYPE, PLAYER_ARENA_TYPE, SKILL_KIND_TYPE, ABSORB_ATTRIBUTE_SHIELD_TYPE,
    ATTRIBUTE_EFFECT_MODE, ATTRIBUTE_TYPE, BUFF_COMPARE_FLAG, SKILL_COMPARE_FLAG
]
