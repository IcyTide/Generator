import json

from extra.attribute import ExtraAttribute
from extra.gear import ExtraGears


def main(info):
    # gears = ExtraGears.from_item(info) # stone in item_id
    gears = ExtraGears.from_enchant(info) # stone in enchant_id
    if kungfu_info := gears.kungfu_info:
        attribute = ExtraAttribute(*kungfu_info)
        attributes, _, _ = gears.content
        for k, v in attributes.items():
            attribute[k] += v
        return attribute
    else:
        return None


if __name__ == '__main__':
    main(json.load(open("client.txt", encoding="utf-8")))
