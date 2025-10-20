from assets.raw.buffs import BUFFS
from assets.raw.skills import SKILLS
from gains.consumables import GAINS as CONSUMABLE_GAINS
from gains.gears import GAINS as GEAR_GAINS
from gains.teams import GAINS as TEAM_GAINS


def special_enchant_belt(self: "Gain"):
    buff_id = self.buffs[0]
    rate = 8 / 30
    add_buff_to_attributes(buff_id, 1, self.attributes, 0.3 * rate)
    add_buff_to_attributes(buff_id, 2, self.attributes, 0.7 * rate)


def special_enchant_jacket(self: "Gain"):
    skill_id = self.skills[0]
    skill = SKILLS[0][skill_id][self.gain_level]
    self.attributes = skill["attributes"]


ATTRIBUTE_FUNCS = {
    22169: special_enchant_belt,
    22151: special_enchant_jacket
}


def add_buff_to_attributes(buff_id: int, buff_level: int, attributes: dict, weight: float = 1.):
    buff = BUFFS[0][buff_id][buff_level]
    stack = buff["max_stack"]
    for k, v in buff["attributes"].items():
        if k not in attributes:
            attributes[k] = 0
        attributes[k] += int(v * stack * weight)


class Gain:
    skills: list[int]
    buffs: list[int]
    dots: dict[int, list[int]]

    weight: float = 1.
    weights: dict = {}
    attributes: dict = {}

    def __init__(self, gain_str: str):
        _, self.gain_id, self.gain_level = gain_str.split("_")
        self.gain_id = int(self.gain_id)
        self.gain_level = int(self.gain_level)
        self.attributes, self.buffs, self.skills, self.dots = {}, [], [], {}
        self.post_init()

    def post_init(self):
        if self.gain_id in GEAR_GAINS:
            attrs = GEAR_GAINS[self.gain_id]
        elif self.gain_id in CONSUMABLE_GAINS:
            attrs = CONSUMABLE_GAINS[self.gain_id]
        elif self.gain_id in TEAM_GAINS:
            attrs = TEAM_GAINS[self.gain_id]
        else:
            attrs = {}
        for k, v in attrs.items():
            setattr(self, k, v)
        if self.gain_id in ATTRIBUTE_FUNCS:
            ATTRIBUTE_FUNCS[self.gain_id](self)
        else:
            self.set_attributes()

    def set_attributes(self):
        for buff_id in self.buffs:
            add_buff_to_attributes(buff_id, self.gain_level, self.attributes, self.weight)
