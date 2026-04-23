from gains import consumables, formations, gears, teams
from kungfus import Kungfu


class Gain:
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
