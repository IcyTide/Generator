from base.expression import Variable


def get_damage():
    equip_score, buff_key = Variable("equip_score"), Variable("buff_20854_1")
    damage_base = equip_score * 0.0080170644 - 1388.323959
    # damage_base = max(damage_base, 1300)
    # buff_key = max(buff_key, 1)
    return damage_base * buff_key * 1.25 * 1.3 * 1.15 * 0.5


SKILLS = {
    # Belongs
    # Gear
    40788: dict(name="输出护手特效"),
    42895: dict(name="英雄防御护手特效"),
    41062: dict(name="普通防御护手特效"),

    40794: dict(name="单属性下装特效"),
    40793: dict(name="多属性下装特效"),
    41064: dict(name="防御下装特效"),

    40791: dict(name="单属性腰带特效"),
    40790: dict(name="多属性腰带特效"),
    42767: dict(name="加速腰带特效"),
    41063: dict(name="防御腰带特效"),

    40802: dict(name="破防戒指特效"),
    40803: dict(name="会心戒指特效"),
    40804: dict(name="破招戒指特效"),
    41065: dict(name="防御戒指特效"),

    38934: dict(name="帽子特效"),
    38939: dict(name="会心鞋子特效"),
    38944: dict(name="破防鞋子特效"),
    38945: dict(name="会心项链特效"),
    38946: dict(name="破防项链特效"),
    38949: dict(name="会心腰坠特效"),
    38948: dict(name="破防腰坠特效"),
    38950: dict(name="暗器特效"),

    39088: dict(name="橙武无双"),
    4877: dict(name="水特效"),
    38578: dict(name="风特效"),
    38786: dict(name="防御风特效"),

    22169: dict(name="输出头大附魔"),
    38984: dict(name="输出手大附魔"),
    38985: dict(name="输出脚大附魔"),
    10106: dict(name="输出腰大附魔"),

    33249: dict(name="防御手大附魔"),

    # Formation
    102268: dict(name="江湖行侠阵"),

    # Damages
    40789: {
        1: dict(custom_damage_base=403200),
        2: dict(custom_damage_base=601965)
    },
    42898: {
        1: dict(custom_damage_base=458640)
    },
    41069: {
        1: dict(custom_damage_base=352800)
    },
    41073: {
        1: dict(custom_damage_base=Variable("max_life") * 0.065)
    },
    42837: {
        # 12跳(9232)15跳(19285)17跳(30158)22跳(42057)
        1: dict(custom_damage_base=141600),
    },
    38966: {
        1: dict(custom_damage_base=86500),
        2: dict(custom_damage_base=90000),
        3: dict(custom_damage_base=320423),
        4: dict(custom_damage_base=345600),
        5: dict(custom_damage_base=475043),
        6: dict(custom_damage_base=515970),
    },
    37562: {
        1: dict(custom_damage_base=244355),
        2: dict(custom_damage_base=281280),
        3: dict(custom_damage_base=748100),
        4: dict(custom_damage_base=1276500)
    },
    37561: {
        1: dict(custom_damage_base=162903),
        2: dict(custom_damage_base=187520),
        3: dict(custom_damage_base=498800),
        4: dict(custom_damage_base=851000)
    },
    22151: dict(comment="{}"),
    38787: {
        1: dict(custom_damage_base=800000),
        2: dict(custom_damage_base=400000),
        3: dict(custom_damage_base=920000),
        4: dict(custom_damage_base=460000),
        5: dict(custom_damage_base=1104000),
        6: dict(custom_damage_base=552000)
    },
    29532: {
        1: dict(custom_damage_base=get_damage(), custom_damage_type="poison")
    },
    23104: {24: {}},
    23107: {24: {}},
    23177: {4: {}},
    21933: {5: {}}
}
