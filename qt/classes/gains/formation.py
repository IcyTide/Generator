from assets.raw.belongs import BELONGS
from assets.raw.buffs import BUFFS
from gains.formations import FORMATIONS as RAW_FORMATIONS
from qt.classes.attribute import Attribute


def add_buff_to_attributes(buff_id: int, attribute: Attribute, weight: float = 1.):
    for buff in BUFFS[0][buff_id].values():
        stack = buff["max_stack"]
        for k, v in buff["attributes"].items():
            attribute[k] += int(v * stack * weight)


def buff_18336(buff_id: int, attribute: Attribute, weight: float = 1.):
    add_buff_to_attributes(buff_id, attribute, weight / len(BUFFS[0][buff_id]))


def buff_18337(buff_id: int, attribute: Attribute, weight: float = 1.):
    add_buff_to_attributes(buff_id, attribute, weight / 2)


FORMATIONS = {
    BELONGS[0][k]["name"]: v for k, v in RAW_FORMATIONS.items()
}

ATTRIBUTE_FUNCS = {
    18336: buff_18336,
    18337: buff_18337
}


class FormationGain:
    buffs: list[int]
    skills: list[int]

    def __init__(self, name: str, level_4_rate: float, level_5_rate: float, level_6_rate: float):
        self.name = name
        self.rates = [1, level_4_rate, level_5_rate, level_6_rate]
        self.buffs = FORMATIONS[name]

    def set_attribute(self, attribute: Attribute):
        for buff_id, rate in zip(self.buffs, self.rates):
            if not buff_id:
                continue
            if buff_id in ATTRIBUTE_FUNCS:
                ATTRIBUTE_FUNCS[buff_id](buff_id, attribute, rate)
            else:
                add_buff_to_attributes(buff_id, attribute, rate)


class Formation:
    def __init__(self, name: str = "", level_4_rate: float = 0., level_5_rate: float = 0., level_6_rate: float = 0.):
        if name:
            self.gain = FormationGain(name, level_4_rate, level_5_rate, level_6_rate)
        else:
            self.gain = None

    @property
    def content(self):
        if self.gain:
            return dict(formation=self.gain)
        else:
            return {}

    def to_dict(self):
        if self.gain:
            return dict(
                formation=self.gain.name,
                level_4_rate=self.gain.rates[1],
                level_5_rate=self.gain.rates[2],
                level_6_rate=self.gain.rates[3]
            )
        else:
            return {}

    @classmethod
    def from_dict(cls, json):
        if not json:
            return Formation()
        return Formation(json["formation"], json["level_4_rate"], json["level_5_rate"], json["level_6_rate"])