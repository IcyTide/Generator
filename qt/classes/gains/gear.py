from assets.raw.buffs import BUFFS
from assets.raw.skills import SKILLS
from base.constant import BINARY_SCALE
from gains.gears import GAINS
from qt.classes.attribute import Attribute


def default(self: "GearGain", attribute: Attribute):
    for buff_id in self.buffs:
        add_buff_to_attributes(buff_id, self.gain_level, attribute, self.weight)


def shoes(self: "GearGain", attribute: Attribute):
    self.weight = 10 / 20
    default(self, attribute)


def bottom(self: "GearGain", attribute: Attribute):
    thresholds = [93 / BINARY_SCALE, 135 / BINARY_SCALE]
    buff_id_bias = (self.gain_level - 1) % 2
    buff_level_bias = (self.gain_level - 1) // 2
    if attribute.strain <= 0.9 + thresholds[buff_id_bias]:
        add_buff_to_attributes(self.buffs[buff_id_bias], 1 + buff_level_bias, attribute)
    else:
        add_buff_to_attributes(self.buffs[buff_id_bias], 2 + buff_level_bias, attribute)


def belt(self: "GearGain", attribute: Attribute):
    buff_id = self.buffs[0]
    buff_level_bias = (self.gain_level - 1) * 3
    add_buff_to_attributes(buff_id, 1 + buff_level_bias, attribute, 1 / 3)
    add_buff_to_attributes(buff_id, 2 + buff_level_bias, attribute, 1 / 3)
    add_buff_to_attributes(buff_id, 3 + buff_level_bias, attribute, 1 / 3)


def hat(self: "GearGain", attribute: Attribute):
    buff_id = self.buffs[0]
    buff_level_bias = (self.gain_level - 1) * 3
    overcome, critical_strike, surplus = attribute.overcome_base, attribute.critical_strike_base, attribute.surplus_base
    max_value = max(overcome, critical_strike, surplus)
    if max_value == overcome:
        add_buff_to_attributes(buff_id, 1 + buff_level_bias, attribute)
    elif max_value == critical_strike:
        add_buff_to_attributes(buff_id, 2 + buff_level_bias, attribute)
    else:
        add_buff_to_attributes(buff_id, 3 + buff_level_bias, attribute)


def ring(self: "GearGain", attribute: Attribute):
    buff_id = self.buffs[0]
    buff_level_bias = (self.gain_level - 1) * 2
    add_buff_to_attributes(buff_id, 1 + buff_level_bias, attribute)


def necklace(target: str, thresholds: list[int]):
    def inner(self: "GearGain", attribute: Attribute):
        threshold = thresholds[self.gain_level - 1]
        stack = int(attribute[f"{target}_base"] / threshold)
        self.weight = stack * 1 / 10
        default(self, attribute)

    return inner


def wind(self: "GearGain", attribute: Attribute):
    self.weight = 15 / 180
    default(self, attribute)


def special_enchant_belt(self: "GearGain", attribute: Attribute):
    buff_id = self.buffs[0]
    rate = 8 / 30
    add_buff_to_attributes(buff_id, 1, attribute, 0.3 * rate)
    add_buff_to_attributes(buff_id, 2, attribute, 0.7 * rate)


def special_enchant_jacket(self: "GearGain", attribute: Attribute):
    skill_id = self.gain_id
    skill = SKILLS[0][skill_id][self.gain_level]
    for k, v in skill["attributes"].items():
        attribute[k] += v


ATTRIBUTE_FUNCS = {
    38939: shoes,
    38944: shoes,
    40794: bottom,
    40791: belt,
    38934: hat,
    41065: ring,
    40804: ring,
    40802: ring,
    40803: ring,
    38946: necklace(target="overcome", thresholds=[5427, 5648, 6060, 6496, 6864, 7456]),
    38945: necklace(target="critical_strike", thresholds=[4748, 4942, 5302, 5683, 6006, 6526]),
    38578: wind,
    22169: special_enchant_belt,
    22151: special_enchant_jacket,
}


def add_buff_to_attributes(buff_id: int, buff_level: int, attribute: Attribute, weight: float = 1.):
    buff = BUFFS[0][buff_id][buff_level]
    stack = buff["max_stack"]
    for k, v in buff["attributes"].items():
        attribute[k] += int(v * stack * weight)


class GearGain:
    skills: list[int]
    buffs: list[int]
    dots: dict[int, list[int]]

    weight: float = 1.

    def __init__(self, gain_str: str):
        _, self.gain_id, self.gain_level = gain_str.split("_")
        self.gain_id = int(self.gain_id)
        self.gain_level = int(self.gain_level)
        self.buffs, self.skills, self.dots = [], [], {}
        self.post_init()

    def post_init(self):
        for k, v in GAINS.get(self.gain_id, {}).items():
            setattr(self, k, v)
        self.skills = [skill_id for skill_id in self.skills if skill_id != self.gain_id]

    def set_attribute(self, attribute: Attribute):
        ATTRIBUTE_FUNCS.get(self.gain_id, default)(self, attribute)
