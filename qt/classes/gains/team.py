from assets.raw.belongs import BELONGS
from assets.raw.buffs import BUFFS
from assets.raw.skills import SKILLS
from gains.teams import GAINS as RAW_TEAMS
from qt.classes.attribute import Attribute
from qt.classes.buff import Buff, BuffType
from qt.classes.record import Record
from qt.classes.skill import Skill

TEAM_GAINS = {
    BELONGS[0][k]["name"]: v for k, v in list(RAW_TEAMS.items())
}

GAIN_PRIORITY = dict(
    劲风=2,
    圣浴明心=2
)
"""
Buff to Attribute Funcs
"""


def add_buff_to_attributes(buff_id: int, buff_level: int, attribute: Attribute, weight: float = 1.):
    buff = Buff("团队", buff_id, buff_level, BuffType.Both, weight, **BUFFS[0][buff_id][buff_level])
    attribute.add_buff(buff)


def default_attribute(self: "TeamGain", attribute: Attribute):
    for buff_id in self.buffs:
        buff_level = list(BUFFS[0][buff_id])[0]
        add_buff_to_attributes(buff_id, buff_level, attribute, self.stack * self.rate)


def buff_23107(self: "TeamGain", attribute: Attribute):
    self.stack *= 0.75
    default_attribute(self, attribute)
    self.stack /= 0.75


def buff_4246_1(self: "TeamGain", attribute: Attribute):
    add_buff_to_attributes(self.buffs[0], 1, attribute, self.stack * self.rate)


def buff_4246_2(self: "TeamGain", attribute: Attribute):
    add_buff_to_attributes(self.buffs[0], 2, attribute, self.stack * self.rate)


ATTRIBUTE_FUNCS = dict(
    号令三军=buff_23107,
    朝圣言=buff_4246_1,
    圣浴明心=buff_4246_2
)

"""
Add Skill to Record Funcs
"""
SKILL_FREQ = {
    29532: 50 / 12
}


def add_skill_to_record(skill_id: int, skill_level: int, record: Record, count: float = 1.):
    skill = Skill("团队", skill_id, skill_level, count, **SKILLS[0][skill_id][skill_level])
    record.skills.append(skill)


def default_record(self: "TeamGain", record: Record):
    for skill_id in self.skills:
        if skill_id not in SKILL_FREQ:
            return
        count = record.duration / SKILL_FREQ[skill_id]
        add_skill_to_record(skill_id, 1, record, count)


RECORD_FUNCS = {}


class TeamGain:
    buffs: list[int]
    skills: list[int]

    max_stack: int = 0

    stack: int = 0
    rate: float = 0.

    def __init__(self, name: str, stack: int, rate: float):
        self.name = name
        self.stack = stack
        self.rate = rate
        self.buffs, self.skills = [], []
        for k, v in TEAM_GAINS[name].items():
            setattr(self, k, v)

        buff_id = self.buffs[0]
        buff_level = list(BUFFS[0][buff_id])[0]
        buff_kwargs = BUFFS[0][buff_id][buff_level]
        self.buff_name = buff_kwargs['name']
        self.max_stack = buff_kwargs['max_stack']

    def __bool__(self):
        return bool(self.stack and self.rate)

    def set_attribute(self, attribute: Attribute):
        ATTRIBUTE_FUNCS.get(self.name, default_attribute)(self, attribute)

    def set_record(self, record: Record):
        # RECORD_FUNCS.get(self.name, default_record)(self, record)
        ...

    def to_dict(self):
        return dict(
            name=self.name,
            stack=self.stack,
            rate=self.rate
        )

    @classmethod
    def from_dict(cls, json: dict):
        return TeamGain(**json)

class TeamGains:
    team_gains: dict[str, TeamGain]

    def __init__(self, team_gains: dict = None):
        if not team_gains:
            self.team_gains = {}
        else:
            self.team_gains = team_gains

    def get(self, gain_name: str):
        if gain_name not in self.team_gains:
            self.team_gains[gain_name] = TeamGain(gain_name, 0, 1)
        return self.team_gains[gain_name]

    @property
    def content(self):
        items = sorted(self.team_gains.items(), key=lambda x: GAIN_PRIORITY.get(x[0], 1))
        return {gain.buff_name: gain for gain_name, gain in items if gain}

    def to_dict(self):
        return {gain_name: gain.to_dict() for gain_name, gain in self.team_gains.items() if gain}

    @classmethod
    def from_dict(cls, json: dict):
        if not json:
            return TeamGains()
        return TeamGains({k: TeamGain.from_dict(v) for k, v in json.items()})
