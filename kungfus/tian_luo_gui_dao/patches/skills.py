from ....base.expression import Variable

SKILLS = {
    3126: {
        1: dict(comment="原始"),
        2: dict(comment="千秋万劫"),
        3: dict(comment="尽刑彻毒"),
        4: dict(comment="千秋万劫+尽刑彻毒")
    },
    3313: dict(dest_rollback_attributes=[("coming_damage_cof", 0.5 ** Variable("buff_31800_1") - 1)]),
    3480: dict(comment="橙武特效"),
    3401: {1: {}}, 3404: {1: dict(comment="鬼斧弹药")},
    3819: {1: {}}, 3824: {1: dict(comment="鬼斧弹药")},
    26900: dict(comment="连弩"), 26901: dict(comment="重弩"),
    31027: dict(comment="鬼斧弹药"),
    42664: {
        1: {},
        2: dict(dest_rollback_attributes=[("coming_damage_cof", 1024)])
    }
}
