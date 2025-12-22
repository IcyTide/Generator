import re

from tools.lua.enums import ATTRIBUTE_TYPE
from tools.utils import camel_to_capital, get_variable, read_tab


class BaseReader:
    TABLES: dict = {}

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

    def __init__(self):
        ...

    def query(self, table_name, condition) -> list[dict]:
        ...

    def get_attr_desc(self, attr):
        attr_rows = self.query("attrib_txts", dict(ID=attr))
        if not attr_rows:
            return ""
        attr_row = attr_rows[0]
        return re.sub(r"{.*}", "{}", attr_row['GeneratedMagic'])

    def get_recipe_desc(self, recipe_id, recipe_level):
        recipe_rows = self.query("recipe_txts", dict(ID=recipe_id, Level=recipe_level))
        if not recipe_rows:
            return "", ""
        recipe_row = recipe_rows[0]
        value = get_variable("recipe", recipe_id, recipe_level)
        return recipe_row['Desc'], value

    def get_event_desc(self, event_id):
        event_rows = self.query("event_txts", dict(ID=event_id))
        if not event_rows:
            desc = event_rows[0]['Desc']
        else:
            desc = ""
        event_rows = self.query("event_settings", dict(ID=event_id))
        if event_rows:
            event_row = event_rows[0]
            if event_row['Odds']:
                value = get_variable("gain", event_row['SkillID'], event_row['SkillLevel'])
            else:
                value = ""
        else:
            value = ""
        return desc, value

    def get_attr(self, attr_id: int = None, attr: str = None, param_1: int = None, param_2: int = None):
        if attr_id:
            attr_row = self.query("attrib_settings", dict(ID=attr_id))[0]
            attr = attr_row['ModifyType']
            param_1, param_2 = attr_row['Param1Max'], attr_row['Param2Max']
        cap_attr = camel_to_capital(attr[2:])
        attr_type = ATTRIBUTE_TYPE[cap_attr]  # noqa
        if attr_type == ATTRIBUTE_TYPE.SKILL_EVENT_HANDLER:
            desc, value = self.get_event_desc(param_1)
        elif attr_type == ATTRIBUTE_TYPE.SET_EQUIPMENT_RECIPE:
            desc, value = self.get_recipe_desc(param_1, param_2)
        else:
            desc, value = self.get_attr_desc(attr), param_1
        return {
            "attr": attr,
            "attr_type": attr_type,
            "value": value,
            "desc": desc
        }


class DataFrameReader(BaseReader):
    TABLES = dict(
        weapon_settings=read_tab("settings/item/Custom_Weapon.tab"),
        armor_settings=read_tab("settings/item/Custom_Armor.tab"),
        trinket_settings=read_tab("settings/item/Custom_Trinket.tab"),
        enchant_settings=read_tab("settings/item/Enchant.tab"),
        attrib_settings=read_tab("settings/item/Attrib.tab"),
        set_settings=read_tab("settings/item/Set.tab"),
        other_settings=read_tab("settings/item/Other.tab"),
        event_settings=read_tab("settings/skill/SkillEvent.tab", "settings/skill_mobile/SkillEvent.tab"),

        item_txts=read_tab("ui/scheme/case/Item.txt"),
        attrib_txts=read_tab("ui/scheme/case/Attribute.txt"),
        recipe_txts=read_tab("ui/scheme/case/EquipmentRecipe.txt"),
        event_txts=read_tab("ui/scheme/case/SkillEvent.txt")
    )

    def __init__(self):
        super().__init__()
        self.cal_score(self.TABLES['weapon_settings'])
        self.cal_score(self.TABLES['armor_settings'])
        self.cal_score(self.TABLES['trinket_settings'])

    def cal_score(self, df):
        quality_factor = df['Quality'].map(self.QUALITY_COF).fillna(0)
        position_factor = df['SubType'].map(self.POSITION_COF).fillna(0)
        df['Score'] = (df['Level'].astype(int) * quality_factor * position_factor).round().astype(int)

    def query(self, table_name, condition) -> list[dict]:
        table = self.TABLES[table_name]
        rows = table
        for k, v in condition.items():
            rows = rows[rows[k] == v]
        return rows.to_dict("records")
