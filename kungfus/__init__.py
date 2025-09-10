from kungfus import fen_shan_jing
from kungfus import ao_xue_zhan_yi, bei_ao_jue
from kungfus import bing_xin_jue, du_jing, you_luo_yin
from kungfus import fen_ying_sheng_jue


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
    Kungfu(bing_xin_jue),
    Kungfu(du_jing),
    Kungfu(fen_ying_sheng_jue),
    Kungfu(fen_shan_jing),
    Kungfu(bei_ao_jue),
    Kungfu(you_luo_yin)
]
