TRANSLATE_MAP = {
    "base": "基础",
    "gain": "百分比(乘算)",
    "rate": "百分比(加算)",

    "physical": "外功",
    "magical": "内功",
    "solar_and_lunar": "阴阳",
    "solar": "阳性",
    "lunar": "阴性",
    "neutral": "混元",
    "poison": "毒性",

    "major": "主属性",
    "agility": "身法",
    "strength": "力道",
    "spirit": "根骨",
    "spunk": "元气",
    "vitality": "体质",

    "attack_power": "攻击",
    "weapon_damage": "武器伤害",
    "surplus": "破招",
    "strain": "无双",
    "haste": "加速",
    "overcome": "破防",
    "critical_strike": "会心",
    "critical_power": "会心效果"
}

def get_translates(names: list | dict):
    translates = {}
    for name in names:
        translate = ""
        for k, v in TRANSLATE_MAP.items():
            if k in name:
                translate += v
        translates[name] = translate
    return translates, {v: k for k, v in translates.items()}