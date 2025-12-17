from extra.attribute import Attribute
from tools.lua.enums import ATTRIBUTE_TYPE
from tools.utils import camel_to_capital


def main(attributes: dict[str, int], school: str, kind: str):
    attribute = Attribute(school, kind)
    for attr, value in attributes.items():
        cap_attr = camel_to_capital(attr[2:])
        attr_type = ATTRIBUTE_TYPE[cap_attr]  # noqa
        attribute[attr_type] += value
    return attribute


if __name__ == '__main__':
    main({}, "", "")
