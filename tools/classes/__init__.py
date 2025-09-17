from tools.utils import camel_to_snake


class AliasBase:
    _aliases = {}
    zero: int = 0

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

    @staticmethod
    def get_name(txt, id_column, id_value, level):
        txt_rows = txt[txt[id_column] == id_value]
        default_row = txt_rows[txt_rows['Level'] == 0]
        default_name = default_row.iloc[0]['Name'] if not default_row.empty else ""
        txt_row = txt_rows[txt_rows['Level'] == level]
        name = txt_row.iloc[0]['Name'] if not txt_row.empty else default_name
        return name

    def to_dict(self):
        return {}
