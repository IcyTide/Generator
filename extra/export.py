import copy
import json
import luadata

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


def convert2jx3api(equips: list[dict]):
    result = []
    for e in equips:
        if e.get("nPos") in {1}:
            continue
        data = copy.copy(e)
        data["aSlotItem"] = [[-1, x] for x in e.get("aDiamondEnchant", [])]
        color_stone = e.get("dwItemFEAEnchantID")
        color_stone = {"0": [-1, color_stone]}
        data["ColorInfo"] = color_stone
        result.append(data)
    return result


def run_by_plugin_data(data: str):
    import base64
    import zlib

    decoded_data = base64.urlsafe_b64decode(data + "=" * (-len(data) % 4))
    decompressed_data = zlib.decompress(decoded_data).decode("utf-8")
    equips = luadata.unserialize(decompressed_data, encoding="utf-8", multival=False)
    equips = convert2jx3api(equips)
    attribute = main({"equip_data": equips})
    return attribute


if __name__ == "__main__":
    main(json.load(open("", encoding="utf-8")))
