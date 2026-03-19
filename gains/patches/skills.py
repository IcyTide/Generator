from base.expression import Variable


def get_damage():
    equip_score, buff_key = Variable("equip_score"), Variable("buff_20854_1")
    damage_base = equip_score * 0.0080170644 - 1388.323959
    # damage_base = max(damage_base, 1300)
    # buff_key = max(buff_key, 1)
    return damage_base * buff_key * 1.25 * 1.3 * 1.15 * 0.5


SKILLS = {
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
    40789: dict(levels=[1, 2, 3], custom_damage_source=40788),
    41069: dict(levels=[1], custom_damage_source=41062),
    42898: dict(levels=[1, 2], custom_damage_source=42897),

    41073: dict(levels=[1, 2, 3], custom_damage_base=Variable("max_life") * 0.065),

    42837: dict(levels=[1, 2], custom_damage_source=42768),
    38966: dict(levels=[4, 5, 6, 7, 8], custom_damage_source=38950),
    37562: dict(levels=[3, 4, 5], custom_damage_source=38984),
    37561: dict(levels=[3, 4, 5], custom_damage_source=38985),
    22151: dict(levels=[15, 16, 17]),
    38787: dict(
        levels=[3, 4, 5, 6, 7, 8], comment="{(level+1)//2}级{'精准反击'if level%2 else ''}",
        custom_damage_source=38787
    ),
    29532: dict(levels=[1], custom_damage_base=get_damage(), custom_damage_type="poison"),

    23104: {24: {}},
    23107: {24: {}},
    23177: {4: {}},
    21933: {5: {}},
    **{
        skill_id: {1: {}}
        for skill_id in [42801, 42841, 42817, 42840, 42842, 42839] +
                        [42800, 42844, 42846, 42848, 42845, 42849] +
                        [42802, 43720, 43721, 43722, 43724, 43901, 43902] +
                        [42803, 43756] +
                        [42711, 43757, 43758]},
    42846: {
        1: dict(comment="0-2秒"),
        2: dict(comment="2-6秒"),
        3: dict(comment="大于6秒"),
    }
}
