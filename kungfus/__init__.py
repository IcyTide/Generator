from assets.raw.attributes import ATTRIBUTES
from assets.raw.buffs import BUFFS
from assets.raw.dots import DOTS
from assets.raw.skills import SKILLS
from assets.raw.talents import TALENTS
from kungfus import ao_xue_zhan_yi, bei_ao_jue, gu_feng_jue, jing_yu_jue, xiao_chen_jue
from kungfus import bing_xin_jue, du_jing, mo_wen, wu_fang, you_luo_yin, zi_xia_gong
from kungfus import fen_shan_jing, ling_hai_jue, shan_hai_xin_jue, shan_ju_jian_yi, tai_xu_jian_yi, wen_shui_jue, \
    yin_long_jue
from kungfus import fen_ying_sheng_jue, hua_jian_you, tai_xuan_jing, tian_luo_gui_dao, yi_jin_jing, zhou_tian_gong

BUFF_PATCHES = {}
SKILL_PATCHES = {}


class Kungfu:
    def __init__(self, kungfu):
        BUFF_PATCHES.update(kungfu.BUFF_PATCHES)
        SKILL_PATCHES.update(kungfu.SKILL_PATCHES)
        self.kungfu_id = self.attribute = kungfu.ATTRIBUTE
        self.buffs = kungfu.BUFFS
        self.dots = kungfu.DOTS
        self.recipes = kungfu.RECIPES
        self.skills = kungfu.SKILLS
        self.talents = kungfu.TALENTS


class DisplayKungfu:
    def __init__(self, kungfu: Kungfu):
        self.kungfu_id = kungfu.attribute
        self.attribute = ATTRIBUTES[self.kungfu_id]
        buffs, dots, skills = kungfu.buffs, kungfu.dots, kungfu.skills
        self.talents = {}
        for talents in kungfu.talents:
            for talent_id, params in talents.items():
                talent = self.talents[talent_id] = TALENTS[self.kungfu_id][talent_id]
                talent_name = talent["name"]
                if talent_buffs := talent.get("buffs"):
                    buffs[talent_name] = talent_buffs
                if talent_dots := talent.get("dots"):
                    dots[talent_name] = talent_dots
                if talent_skills := talent.get("skills"):
                    skills[talent_name] = talent_skills
        self.buffs = {
            belong: {buff_id: BUFFS[self.kungfu_id][buff_id] for buff_id in buff_ids}
            for belong, buff_ids in buffs.items()
        }
        self.skills = {
            belong: {skill_id: SKILLS[self.kungfu_id][skill_id] for skill_id in skill_ids}
            for belong, skill_ids in skills.items()
        }
        self.dots = {
            belong: {dot_id: DOTS[self.kungfu_id][dot_id] for dot_id in dot_ids}
            for belong, dot_ids in dots.items()
        }


SUPPORT_KUNGFUS: list[Kungfu] = [
    Kungfu(yi_jin_jing),
    Kungfu(zi_xia_gong),
    Kungfu(tai_xu_jian_yi),
    Kungfu(hua_jian_you),
    # Kungfu(ao_xue_zhan_yi),
    # Kungfu(bing_xin_jue),
    # Kungfu(wen_shui_jue),
    # Kungfu(shan_ju_jian_yi),
    Kungfu(du_jing),
    # Kungfu(jing_yu_jue),
    # Kungfu(tian_luo_gui_dao),
    # Kungfu(fen_ying_sheng_jue),
    Kungfu(xiao_chen_jue),
    Kungfu(fen_shan_jing),
    # Kungfu(mo_wen),
    Kungfu(bei_ao_jue),
    Kungfu(ling_hai_jue),
    # Kungfu(yin_long_jue),
    Kungfu(tai_xuan_jing),
    Kungfu(wu_fang),
    Kungfu(shan_hai_xin_jue),
    Kungfu(gu_feng_jue),
    Kungfu(zhou_tian_gong),
    Kungfu(you_luo_yin)
]
