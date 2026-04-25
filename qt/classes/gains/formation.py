from assets.raw.belongs import BELONGS
from assets.raw.buffs import BUFFS
from gains.formations import FORMATIONS as RAW_FORMATIONS
from qt.classes.attribute import Attribute
from qt.classes.buff import Buff, BuffType
from qt.classes.record import Record

FORMATIONS = {
    BELONGS[0][k]["name"]: v for k, v in RAW_FORMATIONS.items()
}
BELONG2ID = {BELONGS[0][k]["name"]: k for k in RAW_FORMATIONS}


def add_buff_to_attributes(belong_id: int, buff_id: int, buff_level: int, attribute: Attribute, weight: float = 1.):
    buff = Buff(belong_id, buff_id, buff_level, BuffType.Both, weight, **BUFFS[0][belong_id][buff_id][buff_level])
    buff.stack *= buff.max_stack
    attribute.add_buff(buff)


def default_attribute(self: "FormationGains", buff_id: int, rate: float, attribute: Attribute):
    buff_level = list(BUFFS[0][self.belong_id][buff_id])[0]
    add_buff_to_attributes(self.belong_id, buff_id, buff_level, attribute, rate)


def buff_18336(self: "FormationGains", buff_id: int, rate: float, attribute: Attribute):
    buff_levels = list(BUFFS[0][self.belong_id][buff_id])
    for buff_level in buff_levels:
        add_buff_to_attributes(self.belong_id, buff_id, buff_level, attribute, rate / len(buff_levels))


def buff_18337(self: "FormationGains", buff_id: int, rate: float, attribute: Attribute):
    buff_level = list(BUFFS[0][self.belong_id][buff_id])[0]
    add_buff_to_attributes(self.belong_id, buff_id, buff_level, attribute, rate / 2)


ATTRIBUTE_FUNCS = {
    18336: buff_18336,
    18337: buff_18337
}


class FormationGains:
    name: str = ""
    rates: dict[str, list[float]]

    average: bool = True

    def __init__(self, name: str = "", rates: dict = None):
        self.name = name
        if not rates:
            self.rates = {}
        else:
            self.rates = rates

    def __bool__(self):
        return bool(self.name)

    def get(self, name: str):
        if name not in self.rates:
            self.rates[name] = [0, 0, 0]
        return self.rates[name]

    @property
    def belong_id(self):
        return BELONG2ID[self.name]

    @property
    def buffs(self):
        return [buff_id for buff_id in FORMATIONS[self.name][1:] if buff_id]

    @property
    def skills(self):
        return []

    @property
    def content(self):
        if self.name:
            return {self.name: self}
        else:
            return {}

    def set_attribute(self, attribute: Attribute):
        buffs = self.buffs
        default_attribute(self, buffs[0], 1, attribute)
        if not self.average:
            return
        for buff_id, rate in zip(buffs[1:], self.rates[self.name]):
            if not buff_id:
                continue
            ATTRIBUTE_FUNCS.get(buff_id, default_attribute)(self, buff_id, rate, attribute)

    def set_record(self, record: Record):
        ...

    def to_dict(self):
        return dict(
            name=self.name,
            rates=self.rates
        )

    @classmethod
    def from_dict(cls, json):
        if not json:
            return FormationGains()
        return FormationGains(**json)
