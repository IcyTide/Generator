import pandas as pd

from tools.utils import camel_to_snake


class AliasBase:
    _aliases = {}
    zero: int = 0
    txt: pd.DataFrame
    setting: pd.DataFrame
    id_column: str = "ID"

    def __getattr__(self, item):
        if item in self._aliases:
            item = self._aliases[item]
        elif item.lower() != item:
            item = camel_to_snake(item)
        if item in dir(self):
            return getattr(self, item)
        else:
            return self.empty_func

    def __getitem__(self, item):
        return getattr(self, item)

    def __setattr__(self, key, value):
        if key in self._aliases:
            key = self._aliases[key]
        elif key.lower() != key:
            key = camel_to_snake(key)
        super().__setattr__(key, value)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    @staticmethod
    def empty_func(*args):
        return

    def get_name(self, id_value, level):
        return self.get_txt_field(id_value, level, "Name")

    def get_desc(self, id_value, level):
        return self.get_txt_field(id_value, level, "Desc")

    def get_txt_field(self, id_value, level, field):
        txt_rows = self.txt[self.txt[self.id_column] == id_value]
        default_row = txt_rows[txt_rows['Level'] == 0]
        if default_row.empty:
            default_row = txt_rows[txt_rows['Level'] == 1]
        default_field = default_row.iloc[0][field] if not default_row.empty else ""
        txt_row = txt_rows[txt_rows['Level'] == level]
        field = txt_row.iloc[0][field] if not txt_row.empty else default_field
        return field

    def to_dict(self):
        return {}
