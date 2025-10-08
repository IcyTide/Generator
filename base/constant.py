from base.expression import Variable

BINARY_SCALE = 1024
DECIMAL_SCALE = 10000

FRAME_PER_SECOND = 16

AGILITY_TO_CRITICAL_STRIKE = 0.9
STRENGTH_TO_ATTACK_POWER = 0.163
STRENGTH_TO_OVERCOME = 0.3
SPIRIT_TO_CRITICAL_STRIKE = 0.9
SPUNK_TO_ATTACK_POWER = 0.181
SPUNK_TO_OVERCOME = 0.3

LEVEL = 130
LEVEL_SCALE = 1155
LEVEL_CONSTANT = 130350
LEVEL_REDUCTION = 0.05

DOT_DAMAGE_SCALE = 12
PHYSICAL_DAMAGE_SCALE = 10
MAGICAL_DAMAGE_SCALE = 12

CRITICAL_STRIKE_SCALE = 9.985 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
CRITICAL_POWER_SCALE = 3.679 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
OVERCOME_SCALE = 11.412 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
HASTE_SCALE = 10.610 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
STRAIN_SCALE = 6.734 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
DEFAULT_SURPLUS_COF = 7.421

SHIELD_SCALE = 6.364
SHIELD_BASE_MAP = {
    134: 83679,
    133: 79721,
    132: 46901,
    131: 33338
}

BASE_MAJOR = 44
BASE_CRITICAL_POWER = 1792

# Ui Constant
QUALITY_COF = {
    1: 1,
    2: 1.4,
    3: 1.6,
    4: 1.8,
    5: 2.5
}
POSITION_COF = {
    0: 1.2,
    1: 0.6,
    2: 1,
    3: 0.9,
    4: 0.5,
    5: 0.5,
    6: 0.7,
    7: 0.5,
    8: 1,
    9: 0.7,
    10: 0.7,
}
POSITION_MAP = {
    0: "primary_weapon",
    1: "tertiary_weapon",
    2: "jacket",
    3: "hat",
    4: "necklace",
    5: "ring",
    6: "belt",
    7: "pendant",
    8: "bottoms",
    9: "shoes",
    10: "wrist",
}
POSITIONS = {
    "hat": "hat",
    "jacket": "jacket",
    "belt": "belt",
    "wrist": "wrist",
    "bottoms": "bottoms",
    "shoes": "shoes",
    "necklace": "necklace",
    "pendant": "pendant",
    "ring_1": "ring",
    "ring_2": "ring",
    "tertiary_weapon": "tertiary_weapon",
    "primary_weapon": "primary_weapon"
}
MAX_BASE_ATTR = 6
MAX_MAGIC_ATTR = 16
MAX_EMBED_ATTR = 3

MAX_STRENGTH_LEVEL = 8
MAX_EMBED_LEVEL = 8
MAX_STONE_ATTR = 3

EMBED_POSITIONS = {
    "hat": 2,
    "jacket": 2,
    "belt": 2,
    "wrist": 2,
    "bottoms": 2,
    "shoes": 2,
    "necklace": 1,
    "pendant": 1,
    "ring": 0,
    "tertiary_weapon": 1,
    "primary_weapon": 3,
    "secondary_weapon": 3
}


def ROUND(num):
    return int(num + 0.5)


def EMBED_COF(level):
    if level > 6:
        cof = (level * 0.65 - 3.2) * 1.3
    else:
        cof = level * 0.195
    return cof * 1.345


def STRENGTH_COF(level):
    return level * (0.7 + 0.3 * level) / 200


MAX_TALENT_COUNT = 7
MAX_TALENT_IN_POOL = 3
MAX_RECIPE = 4

MAJORS = dict(
    力道="strength",
    身法="agility",
    元气="spunk",
    根骨="spirit"
)
CURRENT_VARIABLE_TEMPLATE = ["{}_overcome"]
SNAPSHOT_VARIABLE_TEMPLATE = [
    "base_{}_attack_power", "{}_attack_power_gain", "extra_{}_attack_power",
    "{}_critical_strike_percent", "{}_critical_strike_rate",
    "{}_critical_power_percent", "{}_critical_power_rate"
]
TARGET_VARIABLE_TEMPLATE = [
    "{}_shield_base", "{}_shield_gain",
    "{}_damage_cof"
]
CURRENT_VARIABLE = [
    "surplus",
    "weapon_damage", "weapon_damage_rand",
    "all_shield_ignore",
]
SNAPSHOT_VARIABLE = [
    "strain",
    "pve_addition_base",
    "physical_damage_addition", "magical_damage_addition"
]
EXTRA_VARIABLES = {
    "rand": 0.5,
    "damage": Variable("damage"),
    "target_level": Variable("target_level")
}
