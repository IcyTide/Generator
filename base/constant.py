BINARY_SCALE = 1024
DECIMAL_SCALE = 10000

FRAME_PER_SECOND = 16

AGILITY_TO_CRITICAL_STRIKE = 250
STRENGTH_TO_ATTACK_POWER = 195
STRENGTH_TO_OVERCOME = 61
SPIRIT_TO_CRITICAL_STRIKE = 250
SPUNK_TO_ATTACK_POWER = 195
SPUNK_TO_OVERCOME = 61
PVX_TO_STRAIN = 1220
VITALITY_TO_MAX_LIFE = 10000

LEVEL = 50
LEVEL_SCALE = 33
LEVEL_CONSTANT = 660
LEVEL_REDUCTION = 0.05

DOT_DAMAGE_SCALE = 12
PHYSICAL_DAMAGE_SCALE = 8992.534 / 100
MAGICAL_DAMAGE_SCALE = 9704.743 / 100

SHIELD_PARAM = 10.912

CRITICAL_STRIKE_SCALE = 9.609 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
CRITICAL_POWER_SCALE = 3.54 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
OVERCOME_SCALE = 10.483 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
HASTE_SCALE = 10.21 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
STRAIN_SCALE = 7.117 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
TOUGHNESS_SCALE = 9.518 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)

SHIELD_BASE_MAP = {
    51: 2791,
    52: 3841,
    53: 6399,
    54: 6592
}
SHIELD_CONSTANT_MAP = {
    level: SHIELD_PARAM * (LEVEL_SCALE * level - LEVEL_CONSTANT) for level in SHIELD_BASE_MAP
}
SHIELD_CONSTANT = SHIELD_PARAM * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)

DECRITICAL_CONSTANT = 5.2 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
DODGE_CONSTANT = 13.491 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
PARRY_CONSTANT = 15.833 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)

BASE_AGILITY = 18
BASE_STRENGTH = 17
BASE_SPIRIT = 18
BASE_SPUNK = 17
BASE_VITALITY = 18
BASE_CRITICAL_POWER = 1792
BASE_MAX_LIFE = 160878
BASE_PHYSICAL_SHIELD = 2850

MAX_CRITICAL_STRIKE = 1
MAX_CRITICAL_POWER = 3
MAX_HASTE = 0.25

# Ui Constant

POSITIONS = {
    "帽子": "hat",
    "上衣": "jacket",
    "腰带": "belt",
    "护腕": "wrist",
    "下装": "bottoms",
    "鞋子": "shoes",
    "项链": "necklace",
    "腰坠": "pendant",
    "戒指1": "ring",
    "戒指2": "ring",
    "远程武器": "tertiary_weapon",
    "近战武器": "primary_weapon"
}

MAX_STRENGTH_LEVEL = 8
MAX_EMBED_LEVEL = 8

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

SPECIAL_ENCHANT_MAP = {
    "hat": {
        "dps": {
        },
        "tank": {
        }
    },
    "jacket": {
        "dps": {
        },
        "tank": {
        }
    },
    "belt": {
        "dps": {
        },
        "tank": {
        }
    },
    "wrist": {
        "dps": {
        },
        "tank": {
        }
    },
    "shoes": {
        "dps": {
        },
        "tank": {
        }
    }
}

STONE_POSITIONS = [
    "primary_weapon"
]

VERSION_SCALE = 43900 / 27800


def ROUND(num):
    return int(num + 0.5)


def EMBED_COF(level):
    if level > 6:
        cof = (level * 0.65 - 3.2) * 1.3
    else:
        cof = level * 0.195
    return cof * VERSION_SCALE


def STRENGTH_COF(level):
    return level * (0.7 + 0.3 * level) / 200


MAX_TALENT_COUNT = 6
MAX_MOBILE_TALENT_COUNT = 4
MAX_TALENT_IN_POOL = 3
MAX_RECIPE = 4

MAJOR_TYPES = {
    "力道": "strength",
    "身法": "agility",
    "元气": "spunk",
    "根骨": "spirit",
    "体质": "vitality"
}
CURRENT_VARIABLES = [
    "weapon_damage", "weapon_damage_rand",
    "{}_overcome",
    "all_shield_ignore",
]
SNAPSHOT_VARIABLES = [
    "base_{}_attack_power", "{}_attack_power_gain", "extra_{}_attack_power", "{}_attack_power",
    "{}_critical_strike",
    "{}_critical_power_percent", "{}_critical_power_rate", "unlimit_critical_power_rate", "{}_critical_power",
    "strain",
    "physical_damage_addition", "magical_damage_addition",
    "skill_damage_final_addition",
    "pve_damage_addition",
]
TARGET_VARIABLES = [
    "base_{}_shield", "{}_shield_gain", "extra_{}_shield", "{}_shield",
    "{}_damage_scale", "damage_scale",
    "level",
    "shield_constant"
]
EXTRA_VARIABLES = {
    "rand": 0.5
}
GRAD_VARIABLES = {
    "major_base": 420,
    "vitality_base": 1215,
    "physical_attack_power_base": 891,
    "magical_attack_power_base": 994,
    "weapon_damage_base": 1344,
    "strain_base": 3279,
    "all_overcome_base": 3279,
    "all_critical_strike_base": 3279,
    "all_critical_power_base": 3279
}


def LEVEL_VARIABLES(level):
    return {
        "level": level,
        "shield_base": SHIELD_BASE_MAP[level],
        "shield_constant": SHIELD_CONSTANT_MAP[level]
    }
