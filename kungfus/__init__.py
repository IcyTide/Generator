from kungfus import ao_xue_zhan_yi
from kungfus import fen_ying_sheng_jue
from kungfus import you_luo_yin


class Kungfu:
    def __init__(self, kungfu):
        self.attribute = kungfu.ATTRIBUTE
        self.buffs = kungfu.BUFFS
        self.dots = kungfu.DOTS
        self.recipes = kungfu.RECIPES
        self.skills = kungfu.SKILLS
        self.talents = kungfu.TALENTS


SUPPORT_KUNGFUS: list[Kungfu] = [
    Kungfu(ao_xue_zhan_yi),
    Kungfu(fen_ying_sheng_jue),
    Kungfu(you_luo_yin)
]
