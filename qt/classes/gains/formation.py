from assets.raw.belongs import BELONGS
from assets.raw.buffs import BUFFS
from gains.formations import FORMATIONS as RAW_FORMATIONS
from qt.classes.attribute import Attribute
from qt.classes.buff import Buff, BuffType
from qt.classes.record import Record


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
    buff_id: int
    rate: float = 0.

    average: bool = True

    def __init__(self, buff_id, rate):
        self.buff_id = buff_id
        self.rate = rate

    def set_attribute(self, attribute: Attribute):
        if self.average:
            ATTRIBUTE_FUNCS.get(self.buff_id, default_attribute)(self, attribute)

    def set_record(self, record: Record):
        ...


class FormationGains:
    formation: str = ""
    rates: dict[str, list[float]]

    def __init__(self, formation: str = "", rates: dict = None):
        self.formation = formation
        if not rates:
            self.rates = {}
        else:
            self.rates = rates

    def __bool__(self):
        return bool(self.formation)

    def get(self, formation: str):
        if formation not in self.rates:
            self.rates[formation] = [0, 0, 0]
        return self.rates[formation]

    @property
    def content(self):
        if self.formation:
            buffs, rates = FORMATIONS[self.formation], self.rates[self.formation]
            gains = dict(
                前三重=FormationGain(buffs[0], 1),
            )
            for name, buff_id, rate in zip(["四重", "五重", "六重"], buffs[1:], rates):
                if not buff_id:
                    continue
                gains[name] = FormationGain(buff_id, rate)
            return gains
        else:
            return {}

    def to_dict(self):
        return dict(
            formation=self.formation,
            rates=self.rates
        )

    @classmethod
    def from_dict(cls, json):
        if not json:
            return FormationGains()
        return FormationGains(**json)
