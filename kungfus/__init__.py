from kungfus import ao_xue_zhan_yi, bei_ao_jue, gu_feng_jue, jing_yu_jue, xiao_chen_jue
from kungfus import bei_ao_jue_mobile
from kungfus import bing_xin_jue, du_jing, mo_wen, wu_fang, you_luo_yin, zi_xia_gong
from kungfus import bu_tian_jue, li_jing_yi_dao, ling_su, xiang_zhi, yun_chang_xin_jing
from kungfus import fen_shan_jin, ling_hai_jue, shan_hai_xin_jue, tai_xu_jian_yi, wen_shui_jue, yin_long_jue
from kungfus import fen_ying_sheng_jue, hua_jian_you, tai_xuan_jing, tian_luo_gui_dao, yi_jin_jing, zhou_tian_gong
from kungfus import ming_zun_liu_li_ti, tie_gu_yi, tie_lao_lv, xi_sui_jing
from kungfus import tai_xuan_jing_mobile, zhou_tian_gong_mobile
from kungfus import wu_fang_mobile, you_luo_yin_mobile, zi_xia_gong_mobile


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
    Kungfu(xi_sui_jing),
    Kungfu(yi_jin_jing),
    Kungfu(zi_xia_gong),
    Kungfu(tai_xu_jian_yi),
    Kungfu(hua_jian_you),
    Kungfu(ao_xue_zhan_yi),
    Kungfu(li_jing_yi_dao),
    Kungfu(tie_lao_lv),
    Kungfu(yun_chang_xin_jing),
    Kungfu(bing_xin_jue),
    Kungfu(wen_shui_jue),
    Kungfu(du_jing),
    Kungfu(bu_tian_jue),
    Kungfu(jing_yu_jue),
    Kungfu(tian_luo_gui_dao),
    Kungfu(fen_ying_sheng_jue),
    Kungfu(ming_zun_liu_li_ti),
    Kungfu(xiao_chen_jue),
    Kungfu(tie_gu_yi),
    Kungfu(fen_shan_jin),
    Kungfu(mo_wen),
    Kungfu(xiang_zhi),
    Kungfu(bei_ao_jue),
    Kungfu(ling_hai_jue),
    Kungfu(yin_long_jue),
    Kungfu(tai_xuan_jing),
    Kungfu(ling_su),
    Kungfu(wu_fang),
    Kungfu(shan_hai_xin_jue),
    Kungfu(gu_feng_jue),
    Kungfu(zhou_tian_gong),
    Kungfu(you_luo_yin),

    Kungfu(zi_xia_gong_mobile),
    Kungfu(bei_ao_jue_mobile),
    Kungfu(wu_fang_mobile),
    Kungfu(tai_xuan_jing_mobile),
    Kungfu(zhou_tian_gong_mobile),
    Kungfu(you_luo_yin_mobile)
]
