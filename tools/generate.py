import re

from tqdm import tqdm

from kungfus import SUPPORT_KUNGFUS
from tools.lua.enums import ATTRIBUTE_TYPE
from tools.reader import BaseReader, DataFrameReader
from tools.utils import camel_to_capital, get_variable, save_code, save_json

READER = DataFrameReader()

KINDS = set(sum([[kungfu.kind, kungfu.major] for kungfu in SUPPORT_KUNGFUS], []))
SCHOOLS = set(["精简", "通用"] + [kungfu.school for kungfu in SUPPORT_KUNGFUS])

MIN_EQUIP_LEVEL = 28000
ENCHANT_START_ID = 15778

MIN_EQUIP_SCORE = {
    k: round(MIN_EQUIP_LEVEL * READER.QUALITY_COF[4] * v) for k, v in READER.POSITION_COF.items()
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
USAGE_MAP = {
    0: "PVP",
    1: "PVE",
    2: "PVX",
    3: "ALL"
}

STONE_LEVELS = {
    "(壹)": 1,
    "(贰)": 2,
    "(叁)": 3,
    "(肆)": 4,
    "(伍)": 5,
    "(陆)": 6
}
ATTR_ABBR = {
    "therapy_base": "治疗",
    "overcome_base": "破防",
    "critical_strike_base": "会心",
    "critical_power_base": "会效",
    "haste_base": "加速",
    "surplus_base": "破招",
    "strain_base": "无双",
    "physical_shield": "外防",
    "magical_shield": "内防",
    "toughness": "御劲",
    "decritical_power": "化劲"
}

MAX_BASE_ATTR = 6
MAX_MAGIC_ATTR = 16
MAX_EMBED_ATTR = 3
MAX_ENCHANT_ATTR = 4
MAX_STONE_ATTR = 3
MAX_SET_COUNT = 6
MAX_SET_ATTR = 4


def set_reader(reader: BaseReader):
    global READER
    READER = reader


def get_row_from_reader(table_name: str, row_id: int):
    rows = READER.query(table_name, dict(ID=row_id))
    if not rows:
        return None
    return rows[0]


def simplify_attrs(attrs):
    attributes, recipes, gains = {}, [], []
    for attr in attrs:
        if attr['attr_type'] == "event":
            gains.append(attr['value'])
        elif attr['attr_type'] == "recipe":
            recipes.append(attr['value'])
        elif attr_type := attr['attr_type']:
            if attr_type not in attributes:
                attributes[attr_type] = 0
            attributes[attr_type] += attr['value']
    return attributes, recipes, gains


def get_attr_desc(attr):
    attr_rows = READER.query("attrib_txts", dict(ID=attr))
    if not attr_rows:
        return ""
    attr_row = attr_rows[0]
    return re.sub(r"{.*}", "{}", attr_row['GeneratedMagic'])


def get_recipe_desc(recipe_id, recipe_level):
    recipe_rows = READER.query("recipe_txts", dict(ID=recipe_id, Level=recipe_level))
    if not recipe_rows:
        return "", ""
    recipe_row = recipe_rows[0]
    value = get_variable("recipe", recipe_id, recipe_level)
    return recipe_row['Desc'], value


def get_event_desc(event_id):
    event_rows = READER.query("event_txts", dict(ID=event_id))
    if not event_rows:
        desc = event_rows[0]['Desc']
    else:
        desc = ""
    event_rows = READER.query("event_settings", dict(ID=event_id))
    if event_rows:
        event_row = event_rows[0]
        if event_row['Odds']:
            value = get_variable("gain", event_row['SkillID'], event_row['SkillLevel'])
        else:
            value = ""
    else:
        value = ""
    return desc, value


def get_attr(attr_id: int = None, attr: str = None, param_1: int = None, param_2: int = None):
    if attr_id:
        attr_row = READER.query("attrib_settings", dict(ID=attr_id))[0]
        attr = attr_row['ModifyType']
        param_1, param_2 = attr_row['Param1Max'], attr_row['Param2Max']
    cap_attr = camel_to_capital(attr[2:])
    attr_type = ATTRIBUTE_TYPE[cap_attr]  # noqa
    if attr_type == ATTRIBUTE_TYPE.SKILL_EVENT_HANDLER:
        desc, value = get_event_desc(param_1)
    elif attr_type == ATTRIBUTE_TYPE.SET_EQUIPMENT_RECIPE:
        desc, value = get_recipe_desc(param_1, param_2)
    else:
        desc, value = get_attr_desc(attr), param_1
    return {
        "attr": attr,
        "attr_type": attr_type,
        "value": value,
        "desc": desc
    }


def get_equip_tags(detail):
    tags = []
    attr_tags = []
    if detail['school'] == "精简":
        tags += ["精简"]
    for attr in detail['magic']:
        if detail.get('skill') and "特效" not in tags:
            tags += ["特效"]
        if attr['attr_type'] == "event" and attr['value'] and "特效" not in tags:
            tags += ["特效"]
            continue
        for k, v in ATTR_ABBR.items():
            if k in attr['attr_type'] and v not in attr_tags:
                attr_tags.append(v)
                break
    return tags + attr_tags


def get_base_attrs(row):
    attrs = []
    for i in range(MAX_BASE_ATTR):
        if not (attr := row[f'Base{i + 1}Type']):
            break
        param_1, parma_2 = row[f'Base{i + 1}Max'], row[f'Base{i + 1}Min']
        attrs.append(get_attr(attr=attr, param_1=param_1, param_2=parma_2))
    return attrs


def get_magic_attrs(row):
    attrs = []
    for i in range(MAX_MAGIC_ATTR):
        if not (attr_id := row[f'Magic{i + 1}Type']):
            break
        attrs.append(get_attr(attr_id=attr_id))
    return attrs


def get_embed_attrs(row):
    attrs = []
    for i in range(MAX_EMBED_ATTR):
        if not (attr_id := row[f'DiamondAttributeID{i + 1}']):
            break
        attrs.append(get_attr(attr_id=attr_id))
    return attrs


def get_set_attrs(row):
    set_id, attrs = 0, {}
    set_id = int(row['SetID'])
    if not set_id:
        return set_id, attrs
    set_row = READER.query("set_settings", dict(ID=set_id))[0]
    for i in range(1, MAX_SET_COUNT):
        for j in range(MAX_SET_ATTR):
            if attr_id := set_row[f"{i + 1}_{j + 1}"]:
                if i + 1 not in attrs:
                    attrs[i + 1] = []
                attrs[i + 1].append(get_attr(attr_id=attr_id))
    return set_id, attrs


def get_equip_detail(row):
    detail = {
        "id": row['ID'], "name": row['Name'], "school": row['BelongSchool'], "kind": row['MagicKind'],
        "position": POSITION_MAP[row['SubType']], "usage": USAGE_MAP[row['EquipUsage']],
        "level": int(row['Level']), "score": int(row['Score']), "max_strength": int(row['MaxStrengthLevel'])
    }
    item_row = READER.query("item_txts", dict(ItemID=row['UiID']))[0]
    detail['icon_id'] = int(item_row['IconID'])
    detail['desc'] = item_row['Desc']
    detail['base'] = get_base_attrs(row)
    detail['magic'] = get_magic_attrs(row)
    detail['embed'] = get_embed_attrs(row)
    detail['set_id'], detail['sets'] = get_set_attrs(row)

    if row['SkillID']:
        detail['skill'] = int(row['SkillID']), int(row['SkillLevel'])
    detail['tags'] = get_equip_tags(detail)

    if detail['position'] == "primary_weapon" and row['DetailType'] == 9:
        detail['position'] = "big_sword"
    return detail


def get_equip_code(detail):
    detail['base'], _, _ = simplify_attrs(detail['base'])
    detail['magic'], detail['recipes'], detail['gains'] = simplify_attrs(detail['magic'])
    detail['embed'], _, _ = simplify_attrs(detail['embed'])
    sets = {}
    for count, attrs in detail['sets'].items():
        sets[count] = {}
        sets[count]['attributes'], sets[count]['recipes'], sets[count]['gains'] = simplify_attrs(attrs)
    detail['sets'] = sets
    if skill := detail.pop("skill", None):
        detail['gains'].append(get_variable("gain", *skill))  # noqa
    for key in ["desc", "icon_id", "usage"]:
        detail.pop(key, None)
    return detail


def build_equip_code(details: dict[int, dict]):
    results = {}
    for detail in details.values():
        position, school, kind, usage = detail['position'], detail['school'], detail['kind'], detail['usage']
        if usage in ["PVP", "PVX"]:
            continue
        if position not in results:
            results[position] = {}
        if school not in results[position]:
            results[position][school] = {}
        if kind not in results[position][school]:
            results[position][school][kind] = {}
        name = f"{detail['name']}#{detail['id']} ({detail['level']} {' '.join(detail.pop('tags'))})"
        results[position][school][kind][name] = get_equip_code(detail.copy())
    return results


def get_equip_list(equip_tab):
    equip_tab = equip_tab[equip_tab.SubType.isin(MIN_EQUIP_SCORE)]
    equip_tab = equip_tab[equip_tab.Score >= equip_tab.SubType.map(MIN_EQUIP_SCORE)]
    equip_tab = equip_tab[(equip_tab.MagicKind.isin(KINDS)) & (equip_tab.BelongSchool.isin(SCHOOLS))]
    equip_tab = equip_tab.sort_values(["SubType", "Score", "ID"], ascending=False)

    results = {}
    for row in tqdm(equip_tab.to_dict("records")):
        detail = get_equip_detail(row)
        results[detail['id']] = detail
    return results, build_equip_code(results)


def get_enchant_attrs(row):
    attrs = []
    for i in range(MAX_ENCHANT_ATTR):
        if not (attr := row[f"Attribute{i + 1}ID"]):
            continue
        cap_attr = camel_to_capital(attr[2:])
        attr_type = ATTRIBUTE_TYPE[cap_attr]  # noqa
        value = row[f"Attribute{i + 1}Value1"]
        attrs.append({
            "attr": attr,
            "attr_type": attr_type,
            "value": int(value) if value.isdigit() else value,
            "desc": get_attr_desc(attr)
        })
    return attrs


def get_enchant_detail(row):
    detail = {
        "id": row['ID'], "name": row['Name'], "desc": row['AttriName'],
        "position": POSITION_MAP[row['DestItemSubType']], "score": int(row['Score']),
        "attributes": get_enchant_attrs(row), "temporary": bool(row['Time'])
    }
    return detail


def get_enchant_code(detail):
    detail['attributes'], _, _ = simplify_attrs(detail['attributes'])
    for key in ["desc", "position"]:
        detail.pop(key, None)
    return detail


def build_enchant_code(details: dict[int, dict]):
    results = dict(consumables={})
    for detail in details.values():
        position, desc = detail['position'], detail['desc']
        if not desc:
            continue
        if position not in results:
            results[position] = {}

        detail = get_enchant_code(detail.copy())
        if not detail['attributes']:
            continue
        temporary = detail.pop("temporary")
        name = f"{detail['name']} {desc}"
        if temporary:
            results['consumables'][name] = detail['attributes']
        else:
            results[position][name] = detail
    return results


def get_enchants_list(enchant_settings):
    enchant_tab = enchant_settings[(enchant_settings.ID >= ENCHANT_START_ID) & (enchant_settings.DiamondType1 == 0)]
    enchant_tab = enchant_tab.sort_values(["Score", "ID"], ascending=False)
    results = {}
    for row in tqdm(enchant_tab.to_dict("records")):
        detail = get_enchant_detail(row)
        results[detail['id']] = detail
    return results, build_enchant_code(results)


def get_stone_attrs(row):
    attrs = []
    for i in range(MAX_STONE_ATTR):
        if not (attr := row[f'Attribute{i + 1}ID']):
            break
        cap_attr = camel_to_capital(attr[2:])
        attr_type = ATTRIBUTE_TYPE[cap_attr]  # noqa
        value = row[f'Attribute{i + 1}Value1']
        attrs.append({
            "attr": attr,
            "attr_type": attr_type,
            "value": int(value),
            "desc": get_attr_desc(attr)
        })
    return attrs


def get_stone_detail(row):
    item_rows = READER.query("other_settings", dict(EnchantID=int(row['ID'])))
    item_ids = [row['ID'] for row in item_rows]
    level = 0
    for key in STONE_LEVELS:
        if key in row['Name']:
            level = STONE_LEVELS[key]
    if not level:
        return {}
    detail = {
        "enchant_id": row['ID'], "item_ids": item_ids, "name": row['Name'], "level": level,
        "attributes": get_stone_attrs(row)
    }
    return detail


def get_stone_code(detail):
    detail['attributes'], _, _ = simplify_attrs(detail['attributes'])
    return detail


def build_stone_code(details: dict[int, dict]):
    results = {}
    for detail in details.values():
        attributes = detail['attributes']
        detail = get_stone_code(detail.copy())
        if len(attributes) != len(detail['attributes']):
            continue
        node = results
        for attribute in detail['attributes']:
            if attribute not in node:
                node[attribute] = {}
            node = node[attribute]
        level = detail['level']
        node[level] = detail
    return results


def get_stones_list(enchant_settings):
    stone_tab = enchant_settings[enchant_settings.DiamondType1 > 0]

    results = {}
    for row in tqdm(stone_tab.to_dict("records")):
        detail = get_stone_detail(row)
        if not detail:
            continue
        for item_id in detail['item_ids']:
            results[item_id] = detail
    return results, build_stone_code(results)


def generate():
    armor_json, armor_code = get_equip_list(READER.TABLES['armor_settings'])
    save_json("armors", armor_json)
    trinket_json, trinket_code = get_equip_list(READER.TABLES['trinket_settings'])
    save_json("trinkets", trinket_json)
    weapon_json, weapon_code = get_equip_list(READER.TABLES['weapon_settings'])
    save_json("weapons", weapon_json)
    save_code("equipments", armor_code | trinket_code | weapon_code)
    enchant_json, enchant_code = get_enchants_list(READER.TABLES["enchant_settings"])
    save_code("enchants", enchant_code)
    save_json("enchants", enchant_json)
    stone_json, stone_code = get_stones_list(READER.TABLES['enchant_settings'])
    save_code("stones", stone_code)
    save_json("stones", stone_json)


if __name__ == '__main__':
    generate()
