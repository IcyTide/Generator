from tools.utils import read_tab


class BaseReader:
    TABLES: dict = {}

    def __init__(self):
        ...

    def query(self, table_name, condition) -> list[dict]:
        ...


class DataFrameReader(BaseReader):
    TABLES = dict(
        weapon_settings=read_tab("settings/item/Custom_Weapon.tab"),
        armor_settings = read_tab("settings/item/Custom_Armor.tab"),
        trinket_settings = read_tab("settings/item/Custom_Trinket.tab"),
        enchant_settings = read_tab("settings/item/Enchant.tab"),
        attrib_settings = read_tab("settings/item/Attrib.tab"),
        set_settings = read_tab("settings/item/Set.tab"),
        other_settings = read_tab("settings/item/Other.tab"),
        event_settings = read_tab("settings/skill/SkillEvent.tab", "settings/skill_mobile/SkillEvent.tab"),

        item_txts = read_tab("ui/scheme/case/Item.txt"),
        attrib_txts = read_tab("ui/scheme/case/Attribute.txt"),
        recipe_txts = read_tab("ui/scheme/case/EquipmentRecipe.txt"),
        event_txts = read_tab("ui/scheme/case/SkillEvent.txt")
    )
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