from gains import consumables, formations, gears, patches, teams
from kungfus import Kungfu


class Gain:
    BUFF_PATCHES = patches.BUFF_PATCHES
    SKILL_PATCHES = patches.SKILL_PATCHES
    ATTRIBUTE: int = 0
    KIND: str = ""
    MAJOR: str = ""
    SCHOOL: str = ""
    BUFFS: dict = {}
    DOTS: dict = {}
    SKILLS: dict = {}
    RECIPES: dict = {}
    TALENTS: dict = [consumables.GAINS, teams.GAINS, formations.GAINS, gears.GAINS]


GAIN = Kungfu(Gain)
