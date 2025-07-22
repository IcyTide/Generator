from tools.classes import AliasBase
from tools.lua.enums import ATTRIBUTE_TYPE
from tools.settings import buff_settings, buff_txts
from tools.utils import camel_to_capital


class Buff(AliasBase):
    _aliases = {
        "Name": "buff_name",
        "MaxStackNum": "max_stack",
        "Count": "max_tick"
    }
    buff_id: int
    buff_level: int = 0

    max_level: int

    is_stackable: bool
    is_countable: bool

    max_stack: int
    max_tick: int
    interval: int

    def __init__(self, buff_id: int):
        self.buff_id = buff_id
        self.setting_rows = buff_settings[buff_settings['ID'] == self.buff_id]
        self.max_level = self.setting_rows["Level"].max()

        # self.active_attributes = self.get_attributes('active')
        # self.end_attributes = self.get_attributes('end_time')

    def get_attributes(self, prefix):
        result = {"attributes": [], "recipes": []}
        i = 0
        while hasattr(self, f'{prefix}_attrib{i + 1}'):
            i += 1
            attr = getattr(self, f'{prefix}_attrib{i}')
            if not attr:
                break
            param_1, param_2 = getattr(self, f'{prefix}_value{i}_a'), getattr(self, f'{prefix}_value{i}_b')
            attr_type = ATTRIBUTE_TYPE[camel_to_capital(attr[2:])]
            if not attr_type:
                continue
            if attr_type == ATTRIBUTE_TYPE.SET_TALENT_RECIPE:
                result["recipes"].append([int(param_1), int(param_2)])
            else:
                result["attributes"].append((attr_type.name, int(param_1), int(param_2)))
        return {k: v for k, v in result.items() if v}


    def to_asset(self):
        if self.buff_level:
            setting_row = self.setting_rows[self.setting_rows["Level"] == self.buff_level].iloc[0]
            for k, v in setting_row.items():
                setattr(self, k, v)
            return {
                "name": self.get_name(buff_txts, "BuffID", self.buff_id, self.buff_level),
                "interval": int(self.interval),
                "max_stack": int(self.max_stack),
                "max_tick": int(self.max_tick),
                **self.get_attributes("begin")
            }
        else:
            return {}
