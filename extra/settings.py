import json


STONES = json.load(open("assets/json/stones.json", encoding="utf-8"))
EQUIPMENT_BY_POSITIONS = {
    0: "weapon_settings",
    1: "weapon_settings",
    2: "armor_settings",
    3: "armor_settings",
    4: "trinket_settings",
    5: "trinket_settings",
    6: "armor_settings",
    7: "trinket_settings",
    8: "armor_settings",
    9: "armor_settings",
    10: "armor_settings"
}
EQUIPMENT_BY_TABS = {
    6: "weapon_settings",
    7: "armor_settings",
    8: "trinket_settings"
}

ENCHANTS = "enchant_settings"
STONE_BY_ITEM_IDS = {int(k): v for k, v in STONES.items()}
STONE_BY_ENCHANT_IDS = {v['enchant_id']: v for v in STONES.values()}
EMBED_BY_ITEM_IDS = {
    **{24442 + i: i + 1 for i in range(8)},
    **{24423 + i: i + 1 for i in range(8)},
}
EMBED_BY_ENCHANT_IDS = {
    **{6210 + i: i + 1 for i in range(8)},
    **{6218 + i: i + 1 for i in range(8)},
}
