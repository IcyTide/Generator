from pandas import DataFrame
from tqdm import tqdm

from base.constant import *
from kungfus import SUPPORT_KUNGFUS
from tools.lua.enums import ATTRIBUTE_TYPE
from tools.settings import *
from tools.utils import camel_to_capital, get_variable, save_code

KINDS = set(sum([[kungfu.kind, kungfu.major] for kungfu in SUPPORT_KUNGFUS], []))  # & {"治疗", "防御"}
SCHOOLS = set(["精简", "通用"] + [kungfu.school for kungfu in SUPPORT_KUNGFUS])

MIN_EQUIP_LEVEL = 30200
ENCHANT_START_ID = 15778
MIN_EQUIP_SCORE = {
    k: round(MIN_EQUIP_LEVEL * QUALITY_COF[4] * v) for k, v in POSITION_COF.items()
}


def cal_score(df: DataFrame):
    df['Score'] = df.apply(
        lambda x: round(x['Level'] * QUALITY_COF.get(x['Quality'], 0) * POSITION_COF.get(x['SubType'], 0)),
        axis=1
    )


cal_score(armor_settings)
cal_score(trinket_settings)
cal_score(weapon_settings)

ATTR_ABBR = {
    "therapy_base": "治疗",
    "overcome_base": "破防",
    "critical_strike_base": "会心",
    "critical_power_base": "会效",
    "haste_base": "加速",
    "surplus_base": "破招",
    "strain_base": "无双"
}
SECONDARY_WEAPON_DETAIL_TYPE = 9

MAX_SET_COUNT = 4
MAX_SET_ATTR = 4


def get_equip_name(detail):
    if detail['school'] == "精简":
        abbrs = ["精简"]
    elif detail["gains"]:
        abbrs = ["特效"]
    else:
        abbrs = []
    for attr in detail['magic']:
        for k, v in ATTR_ABBR.items():
            if k in attr:
                abbrs.append(v)
                break
    return f"{detail['name']}#{detail['id']} ({detail['level']} {' '.join(abbrs)})"


def get_equip_detail(row):
    detail = {
        "id": row.ID, "name": row.Name, "school": row.BelongSchool, "kind": row.MagicKind, "level": int(row.Level),
        "max_strength": int(row.MaxStrengthLevel), "set_id": 0,
    }
    item_row = item_settings[item_settings.ItemID == row.UiID]
    if not item_row.empty:
        detail['icon_id'] = int(item_row.iloc[0]['IconID'])
    detail['base'] = base_attrs = {}
    detail['magic'] = magic_attrs = {}
    detail['embed'] = embed_attrs = {}
    detail['gains'] = gains = []
    detail['recipes'] = recipes = []
    detail['sets'] = sets = {}
    for i in range(MAX_BASE_ATTR):
        if not (attr := getattr(row, f'Base{i + 1}Type')):
            break
        attr = camel_to_capital(attr[2:])
        attr_type = ATTRIBUTE_TYPE[attr]  # noqa
        if not attr_type:
            continue
        base_attrs[attr_type] = int(getattr(row, f'Base{i + 1}Max'))
    for i in range(MAX_MAGIC_ATTR):
        if not (attr_id := getattr(row, f'Magic{i + 1}Type')):
            break
        attr_row = attrib_settings[attrib_settings.ID == attr_id].iloc[0]
        attr = camel_to_capital(attr_row.ModifyType[2:])
        attr_type = ATTRIBUTE_TYPE[attr]  # noqa
        if not attr_type:
            continue
        if attr_type == ATTRIBUTE_TYPE.SKILL_EVENT_HANDLER:
            gains.append(get_variable(int(attr_row.Param1Max)))
        elif attr_type == ATTRIBUTE_TYPE.SET_EQUIPMENT_RECIPE:
            recipes.append(get_variable(int(attr_row.Param1Max), int(attr_row.Param2Max)))
        else:
            magic_attrs[attr_type] = int(attr_row.Param1Max)
    for i in range(MAX_EMBED_ATTR):
        if not (attr_id := getattr(row, f'DiamondAttributeID{i + 1}')):
            break
        attr_row = attrib_settings[attrib_settings.ID == attr_id].iloc[0]
        attr = camel_to_capital(attr_row.ModifyType[2:])
        attr_type = ATTRIBUTE_TYPE[attr]  # noqa
        if not attr_type:
            continue
        embed_attrs[attr_type] = int(attr_row.Param1Max)  # noqa

    if row.SkillID:
        gains.append(get_variable(int(row.SkillID), int(row.SkillLevel), "__"))

    if not row.SetID:
        return detail
    detail['set_id'] = int(row.SetID)
    set_row = set_settings[set_settings.ID == row.SetID].iloc[0]
    for i in range(1, MAX_SET_COUNT):
        for j in range(MAX_SET_ATTR):
            if attr_id := getattr(set_row, f"{i + 1}_{j + 1}"):
                attr_row = attrib_settings[attrib_settings.ID == attr_id].iloc[0]
                attr = camel_to_capital(attr_row.ModifyType[2:])
                attr_type = ATTRIBUTE_TYPE[attr]  # noqa
                if not attr_type:
                    continue
                if i + 1 not in sets:
                    sets[i + 1] = {}
                if attr_type == ATTRIBUTE_TYPE.SKILL_EVENT_HANDLER:
                    if "gains" not in sets[i + 1]:
                        sets[i + 1]["gains"] = []
                    sets[i + 1]["gains"].append(get_variable(int(attr_row.Param1Max)))
                elif attr_type == ATTRIBUTE_TYPE.SET_EQUIPMENT_RECIPE:
                    if "recipes" not in sets[i + 1]:
                        sets[i + 1]["recipes"] = []
                    sets[i + 1]["recipes"].append(get_variable(int(attr_row.Param1Max), int(attr_row.Param2Max)))
                else:
                    if "attributes" not in sets[i + 1]:
                        sets[i + 1]["attributes"] = {}
                    sets[i + 1]["attributes"][attr_type] = int(attr_row.Param1Max)  # noqa
    return detail


def get_equip_list(equip_tab):
    equip_tab = equip_tab[equip_tab.SubType.isin(MIN_EQUIP_SCORE)]
    equip_tab = equip_tab[equip_tab.Score >= equip_tab.SubType.map(MIN_EQUIP_SCORE)]
    equip_tab = equip_tab[(equip_tab.MagicKind.isin(KINDS)) & (equip_tab.BelongSchool.isin(SCHOOLS))]
    equip_tab = equip_tab[(~equip_tab.MagicType.str.contains("PVP")) & (~equip_tab.MagicType.str.contains("PVX"))]
    equip_tab = equip_tab.sort_values(["SubType", "Score", "ID"], ascending=False)

    results = {}
    for row in tqdm(equip_tab.itertuples()):
        detail = get_equip_detail(row)
        name = get_equip_name(detail)
        position = POSITION_MAP[row.SubType]  # noqa
        if position not in results:
            results[position] = {}
        school, kind = detail['school'], detail['kind']
        if school not in results[position]:
            results[position][school] = {}
        if kind not in results[position][school]:
            results[position][school][kind] = {}
        results[position][school][kind][name] = detail
    return results


def get_weapon_list():
    return {
        **get_equip_list(weapon_settings[weapon_settings.DetailType != SECONDARY_WEAPON_DETAIL_TYPE]),
        "secondary_weapon": get_equip_list(
            weapon_settings[weapon_settings.DetailType == SECONDARY_WEAPON_DETAIL_TYPE]
        )['primary_weapon']
    }


def get_enchants_list():
    enchant_tab = enchant_settings[(enchant_settings.ID >= ENCHANT_START_ID) & (enchant_settings.DiamondType1 == 0)]
    enchant_tab = enchant_tab.sort_values(["Score", "ID"], ascending=False)
    results = {"consumable": {}}
    for row in tqdm(enchant_tab.itertuples()):
        attr = row.Attribute1ID  # noqa
        attr = camel_to_capital(attr[2:])
        attr_type = ATTRIBUTE_TYPE[attr]  # noqa
        if not attr_type or attr_type == ATTRIBUTE_TYPE.SKILL_EVENT_HANDLER:
            continue
        name = f"{row.Name} {row.AttriName}"  # noqa
        position = POSITION_MAP[row.DestItemSubType]  # noqa
        attributes = {attr_type: int(row.Attribute1Value1)}  # noqa
        if row.Time:  # noqa
            results["consumable"][name] = attributes
        else:
            if position not in results:
                results[position] = {}
            results[position][name] = dict(id=row.ID, score=int(row.Score), attributes=attributes)  # noqa
    results["secondary_weapon"] = results["primary_weapon"]
    return results


def get_stones_list():
    stone_level_mapping = {
        "(壹)": "1",
        "(贰)": "2",
        "(叁)": "3",
        "(肆)": "4",
        "(伍)": "5",
        "(陆)": "6"
    }
    result = {}
    stone_tab = enchant_settings[enchant_settings.DiamondType1 > 0]

    for row in tqdm(stone_tab.itertuples()):
        name = row.Name  # noqa
        level = ""
        for key in stone_level_mapping:
            if key in name:
                level = stone_level_mapping[key]
                break
        attrs = row.Attribute1ID, row.Attribute2ID, row.Attribute3ID  # noqa
        attr_types = [ATTRIBUTE_TYPE[camel_to_capital(attr[2:])] for attr in attrs if attr]  # noqa
        if not all(attr_types):
            continue
        values = row.Attribute1Value1, row.Attribute2Value1, row.Attribute3Value1  # noqa
        node = result
        attributes = {}
        for attr_type, value in zip(attr_types, values):
            if attr_type not in node:
                node[attr_type] = {}
            node = node[attr_type]
            attributes[attr_type] = int(value)
        if row.TabIndex:  # noqa
            stone_id = int(row.TabIndex) - 1  # noqa
        else:
            stone_id = int(stone_tab.loc[row.Index - 1].TabIndex)  # noqa
        if level in node:
            node[level]['id'].append(stone_id)
        else:
            node[level] = dict(id=[stone_id], name=name, level=int(level), attributes=attributes)
    return result


def generate():
    save_code("equipments", {
        **get_equip_list(armor_settings),
        **get_equip_list(trinket_settings),
        **get_weapon_list()
    })
    save_code("enchants", get_enchants_list())
    save_code("stones", get_stones_list())


if __name__ == '__main__':
    generate()
