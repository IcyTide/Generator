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
VITALITY_TO_MAX_LIFE = 10

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
HASTE_SCALE = 10.61 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
STRAIN_SCALE = 6.734 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
TOUGHNESS_SCALE = 2.784 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
DECRITICAL_POWER_SCALE = 1.521 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
DEFAULT_SURPLUS_COF = 7.421

SHIELD_BASE_MAP = {
    134: 83679,
    133: 79721,
    132: 46901,
    131: 33338
}
SHIELD_CONSTANT_MAP = {
    level: 6.364 * (LEVEL_SCALE * level - LEVEL_CONSTANT) for level in SHIELD_BASE_MAP
}
SHIELD_CONSTANT = 6.364 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
DODGE_CONSTANT = 4.628 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)
PARRY_CONSTANT = 5.432 * (LEVEL_SCALE * LEVEL - LEVEL_CONSTANT)



BASE_MAJOR = 44
VITALITY_MAJOR = 45
BASE_CRITICAL_POWER = 1792
MAX_LIFE_BASE = 160878
PHYSICAL_SHIELD_BASE = 2850

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
            26600: "gain_10106_15",
            30800: "gain_10106_16"
        },
        "tank": {
            26600: "gain_22122_15",
            30800: "gain_22122_16"
        }
    },
    "jacket": {
        "dps": {
            26600: "gain_22151_15",
            30800: "gain_22151_16"
        },
        "tank": {
            26600: "gain_22128_15",
            30800: "gain_22128_16"

        }
    },
    "belt": {
        "dps": {
            26600: "gain_22169_1",
            30800: "gain_22169_1"
        },
        "tank": {
            26600: "gain_22129_15",
            30800: "gain_22129_16"
        }
    },
    "wrist": {
        "dps": {
            26600: "gain_38984_3",
            30800: "gain_38984_4"
        },
        "tank": {
            26600: "gain_33249_1",
            30800: "gain_33249_2"
        }
    },
    "shoes": {
        "dps": {
            26600: "gain_38985_3",
            30800: "gain_38985_4"
        },
        "tank": {
            26600: "gain_40512_1",
            30800: "gain_40512_2"
        }
    }
}

STONE_POSITIONS = [
    "primary_weapon",
    "secondary_weapon"
]


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
CURRENT_VARIABLE_TEMPLATES = [
    "{}_overcome"
]
SNAPSHOT_VARIABLE_TEMPLATES = [
    "base_{}_attack_power", "{}_attack_power",
    # "{}_attack_power_gain", "extra_{}_attack_power", # need_int required
    "{}_critical_strike",
    "{}_critical_power"
]
TARGET_VARIABLE_TEMPLATES = [
    "{}_shield_base", "{}_shield_gain",
    "{}_damage_cof"
]
CURRENT_VARIABLES = [
    "surplus",
    "base_weapon_damage", "weapon_damage_rand",
    "all_shield_ignore",
]
SNAPSHOT_VARIABLES = [
    "strain",
    "physical_damage_addition", "magical_damage_addition",
    "skill_damage_cof",
    "pve_addition_base",
]
TARGET_VARIABLES = [
    "damage_cof",
    "level",
    "shield_constant"
]
EXTRA_VARIABLES = {
    "rand": 0.5,
    "damage": Variable("damage"),
}
GRAD_VARIABLES = {
    "major_base": 308,
    "vitality_base": 1037,
    "physical_attack_power_base": 652,
    "magical_attack_power_base": 728,
    "weapon_damage_base": 984,
    "surplus_base": 2401,
    "strain_base": 2401,
    "all_overcome_base": 2401,
    "all_critical_strike_base": 2401,
    "all_critical_power_base": 2401
}


def LEVEL_VARIABLES(level):
    return {
        "level": level,
        "shield_base": SHIELD_BASE_MAP[level],
        "shield_constant": SHIELD_CONSTANT_MAP[level]
    }
