from base.constant import STONE_POSITIONS
from extra.settings import *
from qt.classes.gear import Enchant, Gear, Gears, Stone
from tools.generate import *


def get_row_from_reader(table_name: str, row_id: int):
    rows = Tool.READER.query(table_name, dict(ID=row_id))
    if not rows:
        return None
    return rows[0]


class ExtraGear(Gear):
    id: int = 0
    temp_enchant: Enchant = None

    def __init__(self, gear_id: int, strength_level: int, embed_levels: list[int], position_id: int = None, tab_id: int = None):
        if tab_id in EQUIPMENT_BY_TABS:
            row = get_row_from_reader(EQUIPMENT_BY_TABS[tab_id], gear_id)
        elif position_id in EQUIPMENT_BY_POSITIONS:
            row = get_row_from_reader(EQUIPMENT_BY_POSITIONS[position_id], gear_id)
        else:
            raise KeyError('Not Passing Any ID')
        if row and row['SubType'] in POSITION_MAP:
            detail = get_equip_code(get_equip_detail(row))
            super().__init__(detail['school'], detail['kind'], detail['name'], detail)
            self.strength_level = strength_level
            self.embed_levels = {i: level for i, level in enumerate(embed_levels)}
        else:
            super().__init__('', '', '', {})

    def __bool__(self):
        return bool(self.id)

    @property
    def attributes(self):
        attributes = super().attributes
        if self.temp_enchant:
            for k, v in self.temp_enchant.attributes.items():
                if k not in attributes:
                    attributes[k] = 0
                attributes[k] += v
        return attributes

    @property
    def is_primary_weapon(self):
        return self.position in STONE_POSITIONS


class ExtraEnchant(Enchant):
    id: int = 0

    def __init__(self, enchant_id: int):
        if row := get_row_from_reader(ENCHANTS, enchant_id):
            detail = get_enchant_code(get_enchant_detail(row))
            super().__init__(detail['name'], detail)
        else:
            super().__init__('', {})

    def __bool__(self):
        return bool(self.id)


class ExtraStone(Stone):
    enchant_id: int = 0

    def __init__(self, item_id: int = None, enchant_id: int = None):
        if item_id:
            detail = get_stone_code(STONE_BY_ITEM_IDS[item_id].copy())
            super().__init__(detail)
        elif enchant_id:
            detail = get_stone_code(STONE_BY_ENCHANT_IDS[enchant_id].copy())
            super().__init__(detail)
        else:
            raise KeyError('Not Passing Any ID')

    def __bool__(self):
        return bool(self.enchant_id)


class ExtraGears(Gears):
    gears: dict[str, ExtraGear]

    @classmethod
    def from_enchant(cls, data: list):
        gears = {}
        for equip_data in data:
            position_id, gear_id = equip_data['nPos'], equip_data['dwTabIndex']
            if position_id not in EQUIPMENT_BY_POSITIONS:
                continue
            strength_level = equip_data['nStrengthLevel']
            embed_levels = [EMBED_BY_ENCHANT_IDS.get(slot, 0) for slot in equip_data['aDiamondEnchant']]
            if gear := ExtraGear(gear_id, strength_level, embed_levels, position_id=position_id):
                gears[gear.position] = gear
            else:
                continue
            if enchant := ExtraEnchant(equip_data['dwPermanentEnchantID']):
                gear.enchant = enchant
            if temp_enchant := ExtraEnchant(equip_data['dwTemporaryEnchantID']):
                gear.temp_enchant = temp_enchant
            if not gear.is_primary_weapon:
                continue
            if stone := ExtraStone(enchant_id=equip_data['dwItemFEAEnchantID']):
                gear.stone = stone
        return cls(gears)

    @classmethod
    def from_item(cls, data: dict):
        gears = {}
        for equip_data in data['equip_data']:
            tab_id, gear_id = equip_data['dwTabType'], equip_data['dwTabIndex']
            if tab_id not in EQUIPMENT_BY_TABS:
                continue
            strength_level = equip_data['nStrengthLevel']
            embed_levels = [EMBED_BY_ITEM_IDS.get(slot, 0) for _, slot in equip_data['aSlotItem']]
            if gear := ExtraGear(gear_id, strength_level, embed_levels, tab_id=tab_id):
                gears[gear.position] = gear
            else:
                continue
            if enchant := ExtraEnchant(equip_data['dwPermanentEnchantID']):
                gear.enchant = enchant
            if temp_enchant := ExtraEnchant(equip_data['dwTemporaryEnchantID']):
                gear.temp_enchant = temp_enchant
            if not gear.is_primary_weapon:
                continue
            _, stone_id = equip_data['ColorInfo']['0']
            gear.stone = ExtraStone(item_id=stone_id)
        return cls(gears)

    @property
    def kungfu_info(self):
        for gear in self.gears.values():
            if gear.is_primary_weapon:
                return gear.school, gear.kind
        return None
