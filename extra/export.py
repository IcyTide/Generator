import json

from extra.attribute import Attribute
from extra.gear import Gears


def main(info: dict):
    gears = Gears(info)
    if kungfu_info := gears.kungfu_info:
        attribute = Attribute(*kungfu_info)
        for k, v in gears.content.items():
            attribute[k] += v
        return attribute
    else:
        return None


if __name__ == '__main__':
    main(json.load(open("d.txt", encoding="utf-8")))
