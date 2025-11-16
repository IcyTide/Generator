from assets.raw.belongs import BELONGS
from assets.raw.buffs import BUFFS
from gains.formations import FORMATIONS as RAW_FORMATIONS
from qt.classes.attribute import Attribute
from qt.classes.buff import Buff, BuffType


def add_buff_to_attributes(buff_id: int, buff_level: int, attribute: Attribute, weight: float = 1.):
    buff = Buff("阵眼", buff_id, buff_level, BuffType.Both, weight, **BUFFS[0][buff_id][buff_level])
    buff.stack *= buff.max_stack
    attribute.add_buff(buff)


def default_attribute(self: "FormationGain", attribute: Attribute):
    buff_level = list(BUFFS[0][self.buff_id])[0]
    add_buff_to_attributes(self.buff_id, buff_level, attribute, self.rate)


def buff_18336(self: "FormationGain", attribute: Attribute):
    buff_levels = list(BUFFS[0][self.buff_id])
    for buff_level in buff_levels:
        add_buff_to_attributes(self.buff_id, buff_level, attribute, self.rate / len(buff_levels))


def buff_18337(self: "FormationGain", attribute: Attribute):
    buff_level = list(BUFFS[0][self.buff_id])[0]
    add_buff_to_attributes(self.buff_id, buff_level, attribute, self.rate / 2)


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

    buff_id: int
    rate: float = 0.

    def __init__(self, name: str, level_4_rate: float, level_5_rate: float, level_6_rate: float):
        self.name = name
        self.rates = [1, level_4_rate, level_5_rate, level_6_rate]
        self.buffs = FORMATIONS[name]

    def set_attribute(self, attribute: Attribute):
        for buff_id, rate in zip(self.buffs, self.rates):
            if not buff_id:
                continue
            self.buff_id, self.rate = buff_id, rate
            ATTRIBUTE_FUNCS.get(buff_id, default_attribute)(self, attribute)


class Formation:
    def __init__(self, name: str = "", level_4_rate: float = 0., level_5_rate: float = 0., level_6_rate: float = 0.):
        if name:
            self.gain = FormationGain(name, level_4_rate, level_5_rate, level_6_rate)
        else:
            self.gain = None

    def __bool__(self):
        return self.gain is not None

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
