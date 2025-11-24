from assets.raw.belongs import BELONGS
from assets.raw.buffs import BUFFS
from assets.raw.skills import SKILLS
from base.constant import BINARY_SCALE
from gains.gears import GAINS
from qt.classes.attribute import Attribute
from qt.classes.buff import Buff, BuffType
from qt.classes.record import Record
from qt.classes.skill import Skill

"""
Buff to Attribute Funcs
"""


def add_buff_to_attribute(buff_id: int, buff_level: int, attribute: Attribute, weight: float = 1.):
    buff = Buff("装备", buff_id, buff_level, BuffType.Both, weight, **BUFFS[0][buff_id][buff_level])
    buff.stack = buff.max_stack * weight
    attribute.add_buff(buff)


def default_attribute(self: "GearGain", attribute: Attribute):
    for buff_id in self.buffs:
        add_buff_to_attribute(buff_id, self.gain_level, attribute, self.weight)


def tank_wrist_attribute(self: "GearGain", attribute: Attribute):
    self.weight = 5 / 30
    default_attribute(self, attribute)


def shoes_attribute(self: "GearGain", attribute: Attribute):
    self.weight = 10 / 20
    default_attribute(self, attribute)


def bottom_attribute(self: "GearGain", attribute: Attribute):
    buff_id = self.buffs[(self.gain_level - 1) % 2]
    buff_level = (self.gain_level - 1) // 2 * 2 + 1
    strain_buff = Buff("装备", buff_id, buff_level, BuffType.Both, 1, **BUFFS[0][buff_id][buff_level])
    threshold = strain_buff.attributes["strain_rate"] / BINARY_SCALE
    if attribute.strain <= 0.9 + threshold:
        add_buff_to_attribute(buff_id, buff_level, attribute)
    else:
        add_buff_to_attribute(buff_id, buff_level + 1, attribute)


def belt_attribute(self: "GearGain", attribute: Attribute):
    buff_id = self.buffs[0]
    buff_level_bias = (self.gain_level - 1) * 3
    add_buff_to_attribute(buff_id, 1 + buff_level_bias, attribute, 1 / 3)
    add_buff_to_attribute(buff_id, 2 + buff_level_bias, attribute, 1 / 3)
    add_buff_to_attribute(buff_id, 3 + buff_level_bias, attribute, 1 / 3)


def hat_attribute(self: "GearGain", attribute: Attribute):
    buff_id = self.buffs[0]
    buff_level_bias = (self.gain_level - 1) * 3
    overcome, critical_strike, surplus = attribute.overcome_base, attribute.critical_strike_base, attribute.surplus_base
    max_value = max(overcome, critical_strike, surplus)
    if max_value == overcome:
        add_buff_to_attribute(buff_id, 1 + buff_level_bias, attribute)
    elif max_value == critical_strike:
        add_buff_to_attribute(buff_id, 2 + buff_level_bias, attribute)
    else:
        add_buff_to_attribute(buff_id, 3 + buff_level_bias, attribute)


def ring_attribute(self: "GearGain", attribute: Attribute):
    buff_id = self.buffs[0]
    buff_level_bias = (self.gain_level - 1) * 2
    add_buff_to_attribute(buff_id, 1 + buff_level_bias, attribute)


def necklace_attribute(target: str, thresholds: list[int]):
    def inner(self: "GearGain", attribute: Attribute):
        threshold = thresholds[self.gain_level - 1]
        stack = min(int(attribute[f"{target}_base"] / threshold), 10)
        self.weight = stack / 10
        default_attribute(self, attribute)
    return inner


def wind_attribute(self: "GearGain", attribute: Attribute):
    self.weight = 15 / 180
    default_attribute(self, attribute)


def dps_special_enchant_belt(self: "GearGain", attribute: Attribute):
    buff_id = self.buffs[0]
    rate = 8 / 32
    add_buff_to_attribute(buff_id, 1, attribute, 0.3 * rate)
    add_buff_to_attribute(buff_id, 2, attribute, 0.7 * rate)


def dps_special_enchant_jacket(self: "GearGain", attribute: Attribute):
    skill_id = self.gain_id
    skill = SKILLS[0][skill_id][self.gain_level]
    for k, v in skill["attributes"].items():
        attribute[k] += v


def tank_special_enchant_wrist(self: "GearGain", attribute: Attribute):
    self.weight = 5 / 30
    default_attribute(self, attribute)


ATTRIBUTE_FUNCS = {
    42895: tank_wrist_attribute,
    38939: shoes_attribute,
    38944: shoes_attribute,
    40794: bottom_attribute,
    40791: belt_attribute,
    38934: hat_attribute,
    41065: ring_attribute,
    40804: ring_attribute,
    40802: ring_attribute,
    40803: ring_attribute,
    38946: necklace_attribute(target="overcome", thresholds=[5427, 5648, 6060, 6496, 6864, 7456]),
    38945: necklace_attribute(target="critical_strike", thresholds=[4748, 4942, 5302, 5683, 6006, 6526]),
    38578: wind_attribute,
    22169: dps_special_enchant_belt,
    22151: dps_special_enchant_jacket,
    33249: tank_special_enchant_wrist
}

"""
Add Skill to Record Funcs
"""

SKILL_FREQ = {
    40789: 10,
    38966: 10,
    37562: 15,
    37561: 10,
    42898: 30,
    41069: 30,
    41073: 20,
    38787: 30
}


def add_skill_to_record(skill_id: int, skill_level: int, record: Record, count: float = 1.):
    skill = Skill("装备", skill_id, skill_level, count, **SKILLS[0][skill_id][skill_level])
    record.skills.append(skill)


def default_record(self: "GearGain", record: Record):
    for skill_id in self.skills:
        if skill_id not in SKILL_FREQ:
            return
        count = record.duration / SKILL_FREQ[skill_id]
        add_skill_to_record(skill_id, self.gain_level, record, count)


def wind_record(self: "GearGain", record: Record):
    add_skill_to_record(self.gain_id, self.gain_level * 2, record)


RECORD_FUNCS = {
    38786: wind_record
}


class GearGain:
    skills: list[int]
    buffs: list[int]
    dots: dict[int, list[int]]

    weight: float = 1.

    name: str
    average: bool = True

    def __init__(self, gain_str: str):
        _, self.gain_id, self.gain_level = gain_str.split("_")
        self.gain_id = int(self.gain_id)
        self.gain_level = int(self.gain_level)
        self.buffs, self.skills, self.dots = [], [], {}
        for k, v in GAINS.get(self.gain_id, {}).items():
            setattr(self, k, v)
        self.skills = [skill_id for skill_id in self.skills if skill_id != self.gain_id]

        self.name = BELONGS[0].get(self.gain_id, {}).get("name")

    def set_attribute(self, attribute: Attribute):
        if self.average:
            ATTRIBUTE_FUNCS.get(self.gain_id, default_attribute)(self, attribute)

    def set_record(self, record: Record):
        if self.average:
            RECORD_FUNCS.get(self.gain_id, default_record)(self, record)
