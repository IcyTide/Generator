from assets.raw.buffs import BUFFS
from gains.consumables import GAINS as CONSUMABLE_GAINS
from gains.gears import GAINS as GEAR_GAINS
from gains.teams import GAINS as TEAM_GAINS


def add_buff_to_attributes(buff_id: int, buff_level: int, attributes: dict, weight: float = 1.):
    if buff_id not in BUFFS:
        return
    buffs = BUFFS[buff_id]
    if buff_level not in buffs:
        return
    buff = buffs[buff_level]
    if "attributes" not in buff:
        return
    stack = buff["max_stack"]
    for k, v in buff["attributes"]:
        if k not in attributes:
            attributes[k] = 0
        attributes[k] += v * stack * weight


ATTRIBUTE_FUNCS = {

}


class Gain:
    skills: list[int]
    buffs: list[int]

    weight: float = 1.
    weights: dict = None
    attributes: dict = None

    def __init__(self, gain_str: str):
        _, self.gain_id, self.gain_level = gain_str.split("_")
        self.gain_id = int(self.gain_id)
        self.gain_level = int(self.gain_level)
        self.skills, self.buffs = [], []
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
        self.attributes = {}
        for buff_id in self.buffs:
            if self.weights:
                for level, weight in self.weights.items():
                    add_buff_to_attributes(buff_id, level, self.attributes, weight)
            else:
                add_buff_to_attributes(buff_id, self.gain_level, self.attributes, self.weight)
