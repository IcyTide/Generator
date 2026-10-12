from assets.raw.belongs import BELONGS
from assets.raw.buffs import BUFFS
from assets.raw.skills import SKILLS
from base.constant import BINARY_SCALE
from gains.gears import GAINS, KUNGFU_GAINS
from qt.classes.attribute import Attribute
from qt.classes.buff import Buff, BuffType
from qt.classes.record import Record
from qt.classes.skill import Skill

"""
Buff to Attribute Funcs
"""


def add_buff_to_attribute(gain_id: int, buff_id: int, buff_level: int, attribute: Attribute, weight: float = 1.):
    buff = Buff(gain_id, buff_id, buff_level, BuffType.Both, weight, **BUFFS[0][gain_id][buff_id][buff_level])
    buff.stack = buff.max_stack * weight
    attribute.add_buff(buff)


def default_attribute(self: "GearGain", attribute: Attribute):
    for buff_id in self.buffs:
        add_buff_to_attribute(self.gain_id, buff_id, self.gain_level, attribute, self.weight)


def empty_attribute(self: "GearGain", attribute: Attribute):
    pass


def shoes_attribute(self: "GearGain", attribute: Attribute):
    self.weight = 10 / 20
    default_attribute(self, attribute)


def belt_attribute(self: "GearGain", attribute: Attribute):
    buff_id = list(self.buffs)[0]
    buff_level_bias = self.gain_level * 2
    if attribute.overcome_base >= attribute.critical_strike_base:
        add_buff_to_attribute(self.gain_id, buff_id, 1 + buff_level_bias, attribute)
    else:
        add_buff_to_attribute(self.gain_id, buff_id, 2 + buff_level_bias, attribute)


def hat_attribute(self: "GearGain", attribute: Attribute):
    buff_id = list(self.buffs)[0]
    buff_level_bias = self.gain_level * 3
    if attribute.overcome_base >= attribute.critical_strike_base:
        add_buff_to_attribute(self.gain_id, buff_id, buff_level_bias - 2, attribute)
    else:
        add_buff_to_attribute(self.gain_id, buff_id, buff_level_bias - 1, attribute)


def ring_attribute(self: "GearGain", attribute: Attribute):
    buff_id = list(self.buffs)[0]
    buff_level_bias = self.gain_level * 2
    add_buff_to_attribute(self.gain_id, buff_id, buff_level_bias - 1, attribute)


def necklace_attribute(target: str, thresholds: list[int]):
    def inner(self: "GearGain", attribute: Attribute):
        threshold = thresholds[self.gain_level - 1]
        buff_id, buff_level = list(self.buffs)[0], self.gain_level
        buff = Buff(self.gain_id, buff_id, buff_level, "", 1, **BUFFS[0][self.gain_id][buff_id][buff_level])
        self.weight = int(attribute[f"{target}_base"] / threshold) / buff.max_stack
        self.weight = min(self.weight, 1.)
        default_attribute(self, attribute)

    return inner


def wind_attribute(self: "GearGain", attribute: Attribute):
    self.weight = 15 / 180
    default_attribute(self, attribute)


def special_enchant_belt(self: "GearGain", attribute: Attribute):
    buff_id = list(self.buffs)[0]
    rate = 8 / 32
    add_buff_to_attribute(self.gain_id, buff_id, 1, attribute, 0.3 * rate)
    add_buff_to_attribute(self.gain_id, buff_id, 2, attribute, 0.7 * rate)


def special_enchant_jacket(self: "GearGain", attribute: Attribute):
    skill_id = self.gain_id
    skill = SKILLS[0][self.gain_id][skill_id][self.gain_level]
    for k, v in skill["attributes"].items():
        attribute[k] += v


ATTRIBUTE_FUNCS = {
    38939: shoes_attribute,
    38944: shoes_attribute,
    40791: belt_attribute,
    38934: hat_attribute,
    41065: ring_attribute,
    40802: ring_attribute,
    40803: ring_attribute,
    38946: necklace_attribute(target="overcome", thresholds=[0] * 8 + [2649] * 5),
    38945: necklace_attribute(target="critical_strike", thresholds=[0] * 8 + [1756] * 2),

    38578: wind_attribute,
    22169: special_enchant_belt,
    22151: special_enchant_jacket,
    **{k: empty_attribute for gain in KUNGFU_GAINS.values() for k in gain}
}

"""
Add Skill to Record Funcs
"""

SKILL_FREQ = {
    42837: 40,
    40789: 10,
    38966: 10,

    37562: 15,
    37561: 10,
    41073: 20,
    38787: 30
}


def add_skill_to_record(gain_id: int, skill_id: int, skill_level: int, record: Record, count: float = 1.):
    skill = Skill(gain_id, skill_id, skill_level, count, **SKILLS[0][gain_id][skill_id][skill_level])
    record.skills.append(skill)


def default_record(self: "GearGain", record: Record, attribute: Attribute):
    for skill_id in self.skills:
        if skill_id not in SKILL_FREQ:
            return
        count = record.duration / SKILL_FREQ[skill_id]
        add_skill_to_record(self.gain_id, skill_id, self.gain_level, record, count)


def wrist_record(self: "GearGain", record: Record, attribute: Attribute):
    haste, segments = attribute.haste_base, [
        (0, 12),
        (444, 15),
        (928, 17),
        (1451, 20),
        (2024, 22),
    ]

    for i, (cur_haste, cur_times) in enumerate(segments[1:]):
        prev_haste, prev_times = segments[i]
        if haste <= cur_haste:
            ratio = (haste - prev_haste) / (cur_haste - prev_haste)
            times = int(prev_times + ratio * (cur_times - prev_times))
            break
    else:
        _, times = segments[-1]

    for _ in range(times):
        default_record(self, record, attribute)


RECORD_FUNCS = {
    42767: wrist_record
}

"""
Filter Level Funcs
"""


class GearGain:
    skills: dict[int, dict]
    buffs: dict[int, dict]

    weight: float = 1.

    name: str
    average: bool = True

    def __init__(self, gain_str: str):
        if not gain_str:
            return
        _, self.gain_id, self.gain_level = gain_str.split("_")
        self.gain_id = int(self.gain_id)
        self.gain_level = int(self.gain_level)
        self.buffs, self.skills, self.dots = {}, {}, {}
        for k, v in GAINS.get(self.gain_id, {}).items():
            setattr(self, k, v)
        self.skills = {k: v for k, v in self.skills.items() if k != self.gain_id}

        self.name = BELONGS[0].get(self.gain_id, {}).get("name")

    def set_attribute(self, attribute: Attribute):
        if self.average:
            ATTRIBUTE_FUNCS.get(self.gain_id, default_attribute)(self, attribute)

    def set_record(self, record: Record, attribute: Attribute):
        if self.average:
            RECORD_FUNCS.get(self.gain_id, default_record)(self, record, attribute)
