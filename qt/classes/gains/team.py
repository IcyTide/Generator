from assets.raw.belongs import BELONGS
from assets.raw.buffs import BUFFS
from gains.teams import GAINS as RAW_TEAMS
from qt.classes.attribute import Attribute


def add_buff_to_attributes(buff_id: int, attribute: Attribute, weight: float = 1.):
    for buff in BUFFS[0][buff_id].values():
        for k, v in buff["attributes"].items():
            attribute[k] += int(v * weight)


TEAMS = {
    BELONGS[0][k]["name"]: v for k, v in list(RAW_TEAMS.items())
}

ATTRIBUTE_FUNCS = {
}


class TeamGain:
    buffs: list[int]
    skills: list[int]

    buff_id: int
    buff_name: str
    buff_stack: int = 0

    stack: int = 0
    rate: float = 0.

    def __init__(self, name: str, stack: int, rate: float):
        self.name = name
        self.stack = stack
        self.rate = rate
        self.buffs, self.skills = [], []
        for k, v in TEAMS[name].items():
            setattr(self, k, v)

    def post_init(self):
        self.buff_id = self.buffs[0]
        self.buff_name = BUFFS[0][self.buff_id]

    def set_attribute(self, attribute: Attribute):
        buff_id = self.buffs[0]
        if buff_id in ATTRIBUTE_FUNCS:
            ATTRIBUTE_FUNCS[buff_id](buff_id, attribute, self.stack * self.rate)
        else:
            add_buff_to_attributes(buff_id, attribute, self.stack * self.rate)


class TeamGains:
    team_gains: dict[str, TeamGain]

    def __init__(self, team_gains: dict = None):
        if not team_gains:
            self.team_gains = {}
        else:
            self.team_gains = team_gains

    @property
    def content(self):
        return self.team_gains

    def to_dict(self):
        return

    @classmethod
    def from_dict(cls, team_gains: dict):
        return TeamGains(team_gains)
