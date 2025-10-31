from assets.raw.belongs import BELONGS
from gains.teams import GAINS as RAW_TEAMS
from qt.classes.attribute import Attribute

TEAMS = {
    BELONGS[0][k]["name"]: v for k, v in list(RAW_TEAMS.items())
}

ATTRIBUTE_FUNCS = {
}

class TeamGain:
    buffs: list[int]
    skills: list[int]

    def __init__(self, name: str):
        self.name = name
        self.buffs, self.skills = [], []
        for k, v in TEAMS[name].items():
            setattr(self, k, v)

    def set_attribute(self, attribute: Attribute):
        ...