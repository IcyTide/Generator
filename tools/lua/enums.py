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
    T = auto()
    THERAPY = auto()


class CHARACTER_ENERGY_TYPE(IntEnum):
    RAGE = auto()
    ENERGY = auto()
    SUN_ENERGY = auto()


class ABSORB_ATTRIBUTE_SHIELD_TYPE(IntEnum):
    GLOBAL = auto()
    PHYSICS = auto()
    SOLAR = auto()
    LUNAR = auto()
    NEUTRAL = auto()
    POISON = auto()


class SKILL_KIND_TYPE(StrEnum):
    PHYSICS = "physical"
    SOLAR_MAGIC = "solar"
    LUNAR_MAGIC = "lunar"
    NEUTRAL_MAGIC = "neutral"
    POISON = "poison"
    ADAPTIVE = ""
    LEAP = ""


class MOVE_STATE(IntEnum):
    ON_DEATH = auto()
    ON_FREEZE = auto()
    ON_HALT = auto()
    ON_KNOCKED_DOWN = auto()


class ATTRIBUTE_EFFECT_MODE(IntEnum):
    EFFECT_TO_SELF_AND_ROLLBACK = auto()
    EFFECT_TO_DEST_AND_ROLLBACK = auto()
    EFFECT_TO_SELF_NOT_ROLLBACK = auto()
    EFFECT_TO_DEST_NOT_ROLLBACK = auto()


class ATTRIBUTE_TYPE(StrEnum):
    # Useless Attribute
    USELESS = ""
    INVALID = ""
    KUNGFU_TYPE = ""

    ADAPT_ATTRIBUTE_TYPE = ""
    ACTIVE_THREAT_COEFFICIENT = ""
    DROP_DEFENCE = ""
    BEAT_BACK_RATE = ""
    KNOCKED_DOWN_RATE = ""
    REPULSED_RATE = ""
    DECRITICAL_DAMAGE_POWER_BASE = ""
    DECRITICAL_DAMAGE_POWER_PERCENT = ""
    DECRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = ""
    DECRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = ""

    NO_LIMIT_CHANGE_SKILL_ICON = ""

    # Resource Attribute
    CURRENT_RAGE = ""
    CURRENT_ENERGY = ""

    ACCUMULATE = ""
    CURRENT_SUN_ENERGY = ""
    CURRENT_MOON_ENERGY = ""
    MAX_ACCUMULATE_VALUE = ""
    MAX_RAGE = ""
    MAX_ENERGY = ""
    MAX_SUN_ENERGY = ""
    MAX_MOON_ENERGY = ""
    MAX_LIFE_BASE = ""
    MAX_LIFE_ADDITIONAL = ""
    MAX_LIFE_PERCENT_ADD = ""
    FINAL_MAX_LIFE_ADD_PERCENT = ""
    MAX_MANA_BASE = ""
    MAX_MANA_ADDITIONAL = ""

    RAGE_REPLENISH = ""
    ENERGY_REPLENISH = ""
    LIFE_REPLENISH_EXT = ""
    LIFE_REPLENISH_PERCENT = ""
    MANA_REPLENISH = ""
    MANA_REPLENISH_EXT = ""
    MANA_REPLENISH_PERCENT = ""
    MANA_REPLENISH_COEFFICIENT = ""
    MODIFY_COST_MANA_PERCENT = ""
    MODIFY_COST_ENERGY_PERCENT = ""
    MOVE_SPEED_PERCENT = ""
    JUMP_SPEED_BASE = ""

    SET_USE_BIG_SWORD_FLAG = ""
    STOP_MAKE_SUN_POWER = ""
    STOP_MAKE_MOON_POWER = ""
    DISBLE_SCRIPT_SET_ENERGY = ""

    PHYSICS_REFLECTION_PERCENT = ""
    SOLAR_MAGIC_REFLECTION_PERCENT = ""
    LUNAR_MAGIC_REFLECTION_PERCENT = ""
    NEUTRAL_MAGIC_REFLECTION_PERCENT = ""
    POISON_MAGIC_REFLECTION_PERCENT = ""

    DAMAGE_TO_MANA_FOR_SELF = ""
    DAMAGE_TO_LIFE_FOR_SELF = ""
    REDUCE_DAMAGE_WHEN_LIFE_CHANGED = ""
    SRC_CALL_COMMON_DETACH_BUFF_SCRIPT = ""
    ADD_GLOBAL_ABSORB_SHIELD_RECORD_ONLY_BY_SELF_MAX_LIFE = ""

    DASH = ""
    PULL = ""
    HALT = ""
    SPOOF = ""
    REVIVE = ""
    SILENCE = ""
    IMMUNITY = ""
    IMMUNITY_COMBO = ""
    IMMUNITY_COMBO_ALL = ""
    DISABLE_SPRINT_FLAG = ""
    ADD_TRANSPARENCY_VALUE = ""
    ADD_SPRINT_POWER_REVIVE = ""
    ADD_SPRINT_POWER_MAX = ""
    ADD_HORSE_SPRINT_POWER_MAX = ""
    DIVING_FRAME_BASE = ""

    # Script Attribute
    EXECUTE_SCRIPT = ""
    EXECUTE_SCRIPT_WITH_PARAM = ""
    EXECUTE_SCRIPT_SETUP = ""
    EXECUTE_SCRIPT_BULLET_TO_DEST = ""
    EXECUTE_SCRIPT_BULLET_TO_DEST_AND_ROLLBACK = ""
    PRE_DIE_EXECUTE_SCRIPT = ""
    CAST_SKILL = ""
    CAST_SKILL_TARGET_SELF = ""
    CAST_SKILL_TARGET_SRC = ""
    CAST_SKILL_TARGET_DST = ""
    CALL_BUFF = ""
    CALL_SUB_BUFF = ""
    CONSUME_BUFF = ""
    DEL_SINGLE_BUFF_BY_ID_AND_LEVEL = ""
    DEL_SINGLE_GROUP_BUFF_BY_ID_AND_LEVEL = ""
    DEL_SINGLE_BUFF_BY_FUNCTIONTYPE = ""
    DEL_MULTI_GROUP_BUFF_BY_ID = ""
    DEL_MULTI_GROUP_BUFF_BY_FUNCTIONTYPE = ""
    DETACH_SINGLE_BUFF = ""
    CALL_REPULSED = ""
    CALL_KNOCKED_DOWN = ""
    CALL_ADD_KNOCKED_DOWN_FRAME = ""
    MODIFY_COOL_DOWN = ""
    CLEAR_COOL_DOWN = ""
    DASH_TO_POINT = ""
    DASH_BACKWARD = ""
    SKILL_MOVE = ""
    DIRECT_CAST_MASK = ""

    SET_ADAPTIVE_SKILL_TYPE = "adaptive"
    SET_TALENT_RECIPE = "recipe"
    SET_EQUIPMENT_RECIPE = "recipe"
    SKILL_EVENT_HANDLER = "event"
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
    CALL_ADAPTIVE_DAMAGE = "call_adaptive_damage"

    CALL_SURPLUS_PHYSICS_DAMAGE = "call_physical_surplus"
    CALL_SURPLUS_SOLAR_DAMAGE = "call_solar_surplus"
    CALL_SURPLUS_LUNAR_DAMAGE = "call_lunar_surplus"
    CALL_SURPLUS_NEUTRAL_DAMAGE = "call_neutral_surplus"
    CALL_SURPLUS_POISON_DAMAGE = "call_poison_surplus"

    # Major Attribute
    VITALITY_BASE = "vitality_base"
    AGILITY_BASE = "agility_base"
    STRENGTH_BASE = "strength_base"
    SPIRIT_BASE = "spirit_base"
    SPUNK_BASE = "spunk_base"

    BASE_POTENTIAL_ADD = "all_major_base"

    VITALITY_BASE_PERCENT_ADD = "vitality_gain"
    AGILITY_BASE_PERCENT_ADD = "agility_gain"
    STRENGTH_BASE_PERCENT_ADD = "strength_gain"
    SPIRIT_BASE_PERCENT_ADD = "spirit_gain"
    SPUNK_BASE_PERCENT_ADD = "spunk_gain"

    # Attack/Therapy Attribute
    THERAPY_POWER_BASE = ""
    THERAPY_POWER_PERCENT = ""
    THERAPY_COEFFICIENT = ""
    MODIFY_THREAT = ""

    PHYSICS_ATTACK_POWER_BASE = "physical_attack_power_base"
    SOLAR_ATTACK_POWER_BASE = "solar_attack_power_base"
    LUNAR_ATTACK_POWER_BASE = "lunar_attack_power_base"
    SOLAR_AND_LUNAR_ATTACK_POWER_BASE = "solar_and_lunar_attack_power_base"
    NEUTRAL_ATTACK_POWER_BASE = "neutral_attack_power_base"
    POISON_ATTACK_POWER_BASE = "poison_attack_power_base"
    MAGIC_ATTACK_POWER_BASE = "magical_attack_power_base"
    ALL_TYPE_ATTACK_POWER_BASE = "all_attack_power_base"

    PHYSICS_ATTACK_POWER_PERCENT = "physical_attack_power_gain"
    SOLAR_ATTACK_POWER_PERCENT = "solar_attack_power_gain"
    LUNAR_ATTACK_POWER_PERCENT = "lunar_attack_power_gain"
    NEUTRAL_ATTACK_POWER_PERCENT = "neutral_attack_power_gain"
    NEUTRAL_ATTACK_POWER_PERCNET = "neutral_attack_power_gain"
    POISON_ATTACK_POWER_PERCENT = "poison_attack_power_gain"
    MAGIC_ATTACK_POWER_PERCENT = "magical_attack_power_gain"

    # Hit
    ALL_TYPE_HIT_VALUE = ""

    PHYSICS_HIT_BASE_RATE = ""
    SOLAR_HIT_BASE_RATE = ""
    LUNAR_HIT_BASE_RATE = ""
    NEUTRAL_HIT_BASE_RATE = ""
    POISON_HIT_BASE_RATE = ""

    # Overcome Attribute
    PHYSICS_OVERCOME_BASE = "physical_overcome_base"
    SOLAR_OVERCOME_BASE = "solar_overcome_base"
    LUNAR_OVERCOME_BASE = "lunar_overcome_base"
    SOLAR_AND_LUNAR_OVERCOME_BASE = "solar_and_lunar_overcome_base"
    NEUTRAL_OVERCOME_BASE = "neutral_overcome_base"
    POISON_OVERCOME_BASE = "poison_overcome_base"
    MAGIC_OVERCOME = "magical_overcome_base"
    ALL_TYPE_OVERCOME_BASE = "all_overcome_base"

    PHYSICS_OVERCOME_PERCENT = "physical_overcome_gain"
    SOLAR_OVERCOME_PERCENT = "solar_overcome_gain"
    LUNAR_OVERCOME_PERCENT = "lunar_overcome_gain"
    NEUTRAL_OVERCOME_PERCENT = "neutral_overcome_gain"
    POISON_OVERCOME_PERCENT = "poison_overcome_gain"

    # Critical Attribute

    ALL_TYPE_CRITICAL_STRIKE = "all_critical_strike_base"
    PHYSICS_CRITICAL_STRIKE = "physical_critical_strike_base"
    SOLAR_CRITICAL_STRIKE = "solar_critical_strike_base"
    LUNAR_CRITICAL_STRIKE = "lunar_critical_strike_base"
    SOLAR_AND_LUNAR_CRITICAL_STRIKE = "solar_and_lunar_critical_strike_base"
    NEUTRAL_CRITICAL_STRIKE = "neutral_critical_strike_base"
    POISON_CRITICAL_STRIKE = "poison_critical_strike_base"
    MAGIC_CRITICAL_STRIKE = "magical_critical_strike_base"

    PHYSICS_CRITICAL_STRIKE_BASE_RATE = "physical_critical_strike_rate"
    SOLAR_CRITICAL_STRIKE_BASE_RATE = "solar_critical_strike_rate"
    LUNAR_CRITICAL_STRIKE_BASE_RATE = "lunar_critical_strike_rate"
    NEUTRAL_CRITICAL_STRIKE_BASE_RATE = "neutral_critical_strike_rate"
    POISON_CRITICAL_STRIKE_BASE_RATE = "poison_critical_strike_rate"

    ALL_TYPE_CRITICAL_DAMAGE_POWER_BASE = "all_critical_power_base"
    PHYSICS_CRITICAL_DAMAGE_POWER_BASE = "physical_critical_power_base"
    SOLAR_CRITICAL_DAMAGE_POWER_BASE = "solar_critical_power_base"
    LUNAR_CRITICAL_DAMAGE_POWER_BASE = "lunar_critical_power_base"
    SOLAR_AND_LUNAR_CRITICAL_DAMAGE_POWER_BASE = "solar_and_lunar_critical_power_base"
    NEUTRAL_CRITICAL_DAMAGE_POWER_BASE = "neutral_critical_power_base"
    POISON_CRITICAL_DAMAGE_POWER_BASE = "poison_critical_power_base"
    MAGIC_CRITICAL_DAMAGE_POWER_BASE = "magical_critical_power_base"

    PHYSICS_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = "physical_critical_power_rate"
    PHYSICS_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = "physical_critical_power_rate"
    SOLAR_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = "solar_critical_power_rate"
    SOLAR_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = "solar_critical_power_rate"
    LUNAR_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = "lunar_critical_power_rate"
    LUNAR_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = "lunar_critical_power_rate"
    NEUTRAL_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = "neutral_critical_power_rate"
    NEUTRAL_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = "neutral_critical_power_rate"
    POISON_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = "poison_critical_power_rate"
    POISON_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = "poison_critical_power_rate"
    MAGIC_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = "magical_critical_power_rate"
    MAGIC_CRITICAL_DAMAGE_POWER_BASE_KILO_NUM_RATE = "magical_critical_power_rate"

    UNLIMIT_CRITICAL_DAMAGE_POWER_KILO_NUM_RATE = "all_critical_power_rate"

    # Minor Attribute
    MELEE_WEAPON_DAMAGE_BASE = "weapon_damage_base"
    MELEE_WEAPON_DAMAGE_RAND = "weapon_damage_rand"
    MELEE_WEAPON_DAMAGE_PERCENT = "weapon_damage_gain"
    MELEE_WEAPON_ATTACK_SPEED_BASE = ""
    RANGE_WEAPON_DAMAGE_BASE = ""
    RANGE_WEAPON_DAMAGE_RAND = ""
    RANGE_WEAPON_ATTACK_SPEED_BASE = ""
    NONE_WEAPON_ATTACK_SPEED_BASE = ""
    SURPLUS_VALUE_BASE = "surplus_base"
    SURPLUS_VALUE_ADD_PERCENT = "surplus_gain"
    STRAIN_BASE = "strain_base"
    STRAIN_PERCENT = "strain_gain"
    STRAIN_RATE = "strain_rate"
    HASTE_BASE = "haste_base"
    HASTE_BASE_PERCENT_ADD = ""
    UNLIMIT_HASTE_BASE_PERCENT_ADD = ""

    # Defense Attribute
    DODGE = ""
    PARRY_BASE = ""
    PARRY_BASE_RATE = ""
    PARRY_VALUE_BASE = ""
    TOUGHNESS_BASE = ""

    PHYSICS_SHIELD_BASE = "physical_shield_base"
    MAGIC_SHIELD = "magical_shield_base"
    PHYSICS_SHIELD_PERCENT = "physical_shield_gain"
    SOLAR_MAGIC_SHIELD_PERCENT = "solar_shield_gain"
    LUNAR_MAGIC_SHIELD_PERCENT = "lunar_shield_gain"
    NEUTRAL_MAGIC_SHIELD_PERCENT = "neutral_shield_gain"
    POISON_MAGIC_SHIELD_PERCENT = "poison_shield_gain"

    PHYSICS_SHIELD_ADDITIONAL = ""

    PHYSICS_RESIST_PERCENT = ""
    SOLAR_MAGIC_RESIST_PERCENT = ""
    LUNAR_MAGIC_RESIST_PERCENT = ""
    NEUTRAL_MAGIC_RESIST_PERCENT = ""
    POISON_MAGIC_RESIST_PERCENT = ""

    GLOBAL_RESIST_PERCENT = ""
    GLOBAL_BLOCK = ""

    # Damage/Therapy Cof Attribute
    PHYSICS_DAMAGE_COEFFICIENT = "physical_damage_cof"
    SOLAR_DAMAGE_COEFFICIENT = "solar_damage_cof"
    LUNAR_DAMAGE_COEFFICIENT = "lunar_damage_cof"
    NEUTRAL_DAMAGE_COEFFICIENT = "neutral_damage_cof"
    POISON_DAMAGE_COEFFICIENT = "poison_damage_cof"

    BE_THERAPY_COEFFICIENT = ""

    # Cof Attribute
    VITALITY_TO_MAX_MANA_COF = ""
    THERAPY_POWER_TO_MAGIC_ATTACK_POWER_COF = ""
    AGILITY_TO_PARRY_COF = ""
    AGILITY_TO_PARRY_VALUE_COF = ""
    POISON_ATTACK_POWER_TO_THERAPY_POWER_COF = ""

    AGILITY_TO_PHYSICS_ATTACK_POWER_COF = "agility_to_physical_attack_power"
    AGILITY_TO_PHYSICS_CRITICAL_STRIKE_COF = "agility_to_physical_critical_strike"
    AGILITY_TO_PHYSICS_OVERCOME_COF = "agility_to_physical_overcome"
    STRENGTH_TO_PHYSICS_ATTACK_POWER_COF = "strength_to_physical_attack_power"
    STRENGTH_TO_PHYSICS_OVERCOME_COF = "strength_to_physical_overcome"
    STRENGTH_TO_PHYSICS_CRITICAL_STRIKE_COF = "strength_to_physical_critical_strike"

    SPIRIT_TO_LUNAR_ATTACK_POWER_COF = "spirit_to_lunar_attack_power"
    SPIRIT_TO_NEUTRAL_ATTACK_POWER_COF = "spirit_to_neutral_attack_power"
    SPIRIT_TO_POISON_ATTACK_POWER_COF = "spirit_to_poison_attack_power"
    SPIRIT_TO_LUNAR_CRITICAL_STRIKE_COF = "spirit_to_lunar_critical_strike"
    SPIRIT_TO_NEUTRAL_CRITICAL_STRIKE_COF = "spirit_to_neutral_critical_strike"
    SPIRIT_TO_POISON_OVERCOME_COF = "spirit_to_poison_overcome"
    SPUNK_TO_SOLAR_ATTACK_POWER_COF = "spunk_to_solar_attack_power"
    SPUNK_TO_SOLAR_AND_LUNAR_ATTACK_POWER_COF = "spunk_to_solar_and_lunar_attack_power"
    SPUNK_TO_NEUTRAL_ATTACK_POWER_COF = "spunk_to_neutral_attack_power"
    SPUNK_TO_POISON_ATTACK_POWER_COF = "spunk_to_poison_attack_power"
    SPUNK_TO_NEUTRAL_OVERCOME_COF = "spunk_to_neutral_overcome"
    SPUNK_TO_PHYSICS_CRITICAL_STRIKE_COF = "spunk_to_physical_critical_strike"
    SPUNK_TO_SOLAR_CRITICAL_STRIKE_COF = "spunk_to_solar_critical_strike"
    SPUNK_TO_SOLAR_AND_LUNAR_CRITICAL_STRIKE_COF = "spunk_to_solar_and_lunar_critical_strike"
    SPUNK_TO_NEUTRAL_CRITICAL_STRIKE_COF = "spunk_to_neutral_critical_strike"

    # Other Attribute
    ALL_SHIELD_IGNORE_PERCENT = "all_shield_ignore"
    ALL_DAMAGE_ADD_PERCENT = "all_damage_addition"
    ALL_PHYSICS_DAMAGE_ADD_PERCENT = "physical_damage_addition"
    ALL_MAGIC_DAMAGE_ADD_PERCENT = "magical_damage_addition"
    ADD_DAMAGE_BY_DST_MOVE_STATE = "move_state_damage_addition"
    DST_NPC_DAMAGE_COEFFICIENT = "pve_addition_base"
    GLOBAL_DAMGAGE_FACTOR = "global_damage_factor"
    SKILL_DAMAGE_FINAL_COF = "skill_damage_final_cof"


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
    GLOBAL, RELATION_FORCE, ROLE_TYPE, PLAYER_ARENA_TYPE, CHARACTER_ENERGY_TYPE, ABSORB_ATTRIBUTE_SHIELD_TYPE,
    SKILL_KIND_TYPE, MOVE_STATE, ATTRIBUTE_EFFECT_MODE, ATTRIBUTE_TYPE, BUFF_COMPARE_FLAG, SKILL_COMPARE_FLAG
]
