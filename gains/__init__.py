from gains import consumables, gears, patches, teams
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
    TALENTS: dict = [consumables.GAINS, teams.GAINS, gears.GAINS]


gain = Kungfu(Gain)
