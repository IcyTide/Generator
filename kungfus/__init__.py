from kungfus import ao_xue_zhan_yi, bei_ao_jue, gu_feng_jue, jing_yu_jue, xiao_chen_jue
from kungfus import fen_shan_jing, ling_hai_jue, shan_hai_xin_jue, tai_xu_jian_yi, wen_shui_jue, yin_long_jue
from kungfus import bing_xin_jue, du_jing, mo_wen, wu_fang, you_luo_yin, zi_xia_gong
from kungfus import fen_ying_sheng_jue, hua_jian_you, tai_xuan_jing, tian_luo_gui_dao, yi_jin_jing, zhou_tian_gong

from kungfus import you_luo_yin_mobile
from kungfus import zhou_tian_gong_mobile
BUFF_PATCHES = {}
SKILL_PATCHES = {}


class Kungfu:
    def __init__(self, kungfu):
        self.buff_patches = kungfu.BUFF_PATCHES
        self.skill_patches = kungfu.SKILL_PATCHES
        self.kungfu_id = self.attribute = kungfu.ATTRIBUTE
        self.kind = kungfu.KIND
        self.major = kungfu.MAJOR
        self.school = kungfu.SCHOOL
        self.buffs = kungfu.BUFFS
        self.dots = kungfu.DOTS
        self.skills = kungfu.SKILLS
        self.recipes = kungfu.RECIPES
        self.talents = kungfu.TALENTS


SUPPORT_KUNGFUS: list[Kungfu] = [
    Kungfu(yi_jin_jing),
    Kungfu(zi_xia_gong),
    Kungfu(tai_xu_jian_yi),
    Kungfu(hua_jian_you),
    Kungfu(ao_xue_zhan_yi),
    Kungfu(bing_xin_jue),
    Kungfu(wen_shui_jue),
    Kungfu(du_jing),
    Kungfu(jing_yu_jue),
    Kungfu(tian_luo_gui_dao),
    Kungfu(fen_ying_sheng_jue),
    Kungfu(xiao_chen_jue),
    Kungfu(fen_shan_jing),
    Kungfu(mo_wen),
    Kungfu(bei_ao_jue),
    Kungfu(ling_hai_jue),
    Kungfu(yin_long_jue),
    Kungfu(tai_xuan_jing),
    Kungfu(wu_fang),
    Kungfu(shan_hai_xin_jue),
    Kungfu(gu_feng_jue),
    Kungfu(zhou_tian_gong),
    Kungfu(you_luo_yin),

    Kungfu(zhou_tian_gong_mobile),
    Kungfu(you_luo_yin_mobile)
]
