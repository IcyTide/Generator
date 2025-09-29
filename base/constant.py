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
        cof =  (level * 0.65 - 3.2) * 1.3
    else:
        cof =  level * 0.195
    return cof * 1.35


def STRENGTH_COF(level):
    return level * (0.7 + 0.3 * level) / 200