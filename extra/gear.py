import json
from collections import Counter, defaultdict

from base.constant import *

ARMORS = json.load(open("assets/json/armors.json", encoding="utf-8"))
TRINKETS = json.load(open("assets/json/trinkets.json", encoding="utf-8"))
WEAPONS = json.load(open("assets/json/weapons.json", encoding="utf-8"))
EQUIPMENTS = {
    6: WEAPONS,
    7: ARMORS,
    8: TRINKETS
}
ENCHANTS = json.load(open("assets/json/enchants.json", encoding="utf-8"))
STONES = json.load(open("assets/json/stones.json", encoding="utf-8"))

SLOT_MAPPING = {
    **{24442 + i: i + 1 for i in range(8)},
    **{24423 + i: i + 1 for i in range(8)},
}
FLOAT_ATTRS = {
    "atMeleeWeaponDamageBase": "atMeleeWeaponDamageRand",
    "atRangeWeaponDamageBase": "atRangeWeaponDamageRand"
}
BINARY_ATTRS = ["atMeleeWeaponAttackSpeedBase", "atRangeWeaponAttackSpeedBase"]
STONE_POSITIONS = ["primary_weapon"]


def is_attribute(attr):
    if not attr['attr_type']:
        return False
    if attr['attr_type'] in ['recipe', 'event']:
        return False
    return True


class Equipment:
    id: int = 0

    name: str
    school: str
    kind: str

    position: str
    desc: str

    tags: list[str]

    base: list[dict]
    magic: list[dict]
    embed: list[dict]

    set_id: int
    sets: dict[int, list[dict]]

    max_strength: int

    strength_level: int
    embed_levels: list[int]

    level: int
    score: int

    def __init__(self, tab_id, equipment_id, strength_level, embed_levels):
        equipment_data = EQUIPMENTS[tab_id].get(str(equipment_id), {})
        if not equipment_data:
            return

        for k, v in equipment_data.items():
            setattr(self, k, v)
        self.strength_level = min(self.max_strength, strength_level)
        self.embed_levels = [0] * len(self.embed)
        for i, embed_level in enumerate(embed_levels):
            self.embed_levels[i] = embed_level

    def __bool__(self):
        return bool(self.id)

    @property
    def base_attributes(self):
        attributes = defaultdict(int)
        for attr in self.base:
            if not is_attribute(attr):
                continue
            attributes[attr['attr_type']] += int(attr['value'])
        return attributes

    @property
    def base_desc(self):
        desc_list = []
        for attr in self.base:
            if float_attr := FLOAT_ATTRS.get(attr['attr']):
                min_value = int(attr['value'])
                max_value = min_value
                for sub_attr in self.base:
                    if sub_attr['attr'] == float_attr:
                        max_value += int(sub_attr['value'])
                        break
                desc_list.append(attr['desc'].format(f"{min_value} - {max_value}"))
            elif attr['attr'] in BINARY_ATTRS:
                value = round(int(attr['value']) / FRAME_PER_SECOND, 1)
                desc_list.append(attr['desc'].format(value))
            elif attr['desc']:
                desc_list.append(attr['desc'].format(int(attr['value'])))
        return desc_list

    @property
    def magic_attributes(self):
        attributes = defaultdict(int)
        for attr in self.magic:
            if not is_attribute(attr):
                continue
            elif not self.strength_level:
                value = int(attr['value'])
            else:
                value = int(attr['value'])
                value += ROUND(value * STRENGTH_COF(self.strength_level))
            attributes[attr['attr_type']] += value
        return attributes

    @property
    def magic_desc(self):
        desc_list = []
        for attr in self.magic:
            if self.strength_level:
                if attr['attr_type'] in ['recipe', 'event']:
                    desc_list.append(attr['desc'])
                else:
                    value = int(attr['value'])
                    extra_value = ROUND(value * STRENGTH_COF(self.strength_level))
                    desc_list.append(attr['desc'].format(f"{value}(+{extra_value})"))
            else:
                desc_list.append(attr['desc'].format(attr['value']))
        return desc_list

    @property
    def embed_attributes(self):
        attributes = defaultdict(int)
        for attr, embed_level in zip(self.embed, self.embed_levels):
            if not is_attribute(attr):
                continue
            value = int(attr['value'])
            value = int(value * EMBED_COF(embed_level))
            attributes[attr['attr_type']] += value
        return attributes

    @property
    def embed_desc(self):
        desc_list = []
        for attr, embed_level in zip(self.embed, self.embed_levels):
            value = int(attr['value'])
            value = int(value * EMBED_COF(embed_level))
            desc_list.append(attr['desc'].format(value))
        return desc_list

    @property
    def content(self):
        attributes = Counter()
        attributes += self.base_attributes
        attributes += self.magic_attributes
        attributes += self.embed_attributes
        return attributes

    @property
    def desc_list(self):
        return [self.desc] + self.base_desc + self.magic_desc + self.embed_desc


class Enchant:
    id: int = 0
    name: str
    desc: str
    attributes: list[dict]
    score: int

    def __init__(self, enchant_id: int):
        for k, v in ENCHANTS.get(str(enchant_id), {}).items():
            setattr(self, k, v)

    def __bool__(self):
        return bool(self.id)

    @property
    def content(self):
        attributes = defaultdict(int)
        for attr in self.attributes:
            if not is_attribute(attr):
                continue
            attributes[attr['attr_type']] += int(attr['value'])
        return attributes


class Stone:
    enchant_id: int = 0
    item_ids: list[int]

    name: int

    attributes: list[dict]

    def __init__(self, item_id):
        for k, v in STONES.get(str(item_id), {}).items():
            setattr(self, k, v)

    def __bool__(self):
        return bool(self.item_ids)

    @property
    def content(self):
        attributes = defaultdict(int)
        for attr in self.attributes:
            if not is_attribute(attr):
                continue
            attributes[attr['attr_type']] += int(attr['value'])
        return attributes


class Gear:
    equipment: Equipment

    temporary_enchant: Enchant
    permanent_enchant: Enchant

    stone: Stone

    def __init__(self, equip_data: dict):
        tab_id, equipment_id = equip_data['dwTabType'], equip_data['dwTabIndex']
        strength_level = equip_data['nStrengthLevel']
        embed_levels = [SLOT_MAPPING.get(slot, 0) for _, slot in equip_data['aSlotItem']]
        self.equipment = Equipment(tab_id, equipment_id, strength_level, embed_levels)
        self.temporary_enchant = Enchant(equip_data['dwTemporaryEnchantID'])
        self.permanent_enchant = Enchant(equip_data['dwPermanentEnchantID'])
        _, stone_id = equip_data["ColorInfo"]["0"]
        self.stone = Stone(stone_id)

    def __bool__(self):
        return bool(self.equipment)

    @property
    def is_primary_weapon(self):
        if not self:
            return False
        return self.equipment.position in STONE_POSITIONS

    @property
    def content(self):
        attributes = Counter()
        if self.equipment:
            attributes += self.equipment.content
        if self.temporary_enchant:
            attributes += self.temporary_enchant.content
        if self.permanent_enchant:
            attributes += self.permanent_enchant.content
        if self.stone and self.equipment.position in STONE_POSITIONS:
            attributes += self.stone.content
        return attributes


class Gears:
    gears: list[Gear]

    def __init__(self, info: dict):
        self.gears = []
        for equip_data in info['equip_data']:
            if gear := Gear(equip_data):
                self.gears.append(gear)

    @property
    def content(self):
        attributes = Counter()
        set_counts, set_attrs = defaultdict(int), {}
        for gear in self.gears:
            attributes += gear.content
            if set_id := gear.equipment.set_id:
                set_counts[set_id] += 1
                set_attrs[set_id] = {int(k): v for k, v in gear.equipment.sets.items()}

        set_attributes = defaultdict(int)
        for set_id, count in set_counts.items():
            for need_count, attrs in set_attrs.items():
                if count >= need_count:
                    for attr in attrs:
                        if not attr['attr_type']:
                            continue
                        set_attributes[attr['attr']] += int(attr['value'])
        attributes += set_attributes

        return attributes

    @property
    def kungfu_info(self):
        for gear in self.gears:
            if gear.is_primary_weapon:
                return gear.equipment.school, gear.equipment.kind
        return None