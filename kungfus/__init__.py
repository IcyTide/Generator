from kungfus import ao_xue_zhan_yi
from kungfus import fen_ying_sheng_jue


class Kungfu:
    def __init__(self, kungfu):
        self.attribute = kungfu.ATTRIBUTE
        self.buffs = kungfu.BUFFS
        self.skills = kungfu.SKILLS
        self.dots = kungfu.DOTS
        self.talents = kungfu.TALENTS


SUPPORT_KUNGFUS: list[Kungfu] = [
    Kungfu(fen_ying_sheng_jue),
    Kungfu(ao_xue_zhan_yi)
]
