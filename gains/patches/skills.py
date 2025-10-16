from base.expression import Variable


def get_damage():
    equip_score, buff_key = Variable("equip_score"), Variable("buff_20854_1")
    damage_base = equip_score * 0.0080170644 - 1388.323959
    # damage_base = max(damage_base, 1300)
    # buff_key = max(buff_key, 1)
    return damage_base * buff_key * 1.25 * 1.3 * 1.15 * 0.5


SKILLS = {
    42837: {
        # 12跳(9232)15跳(19285)17跳(30158)22跳(42057)
        1: dict(custom_damage_base=123300),
    },
    40789: {
        1: dict(custom_damage_base=403200),
        2: dict(custom_damage_base=524160)
    },
    38966: {
        1: dict(custom_damage_base=86500),
        2: dict(custom_damage_base=90000),
        3: dict(custom_damage_base=320423),
        4: dict(custom_damage_base=345600),
        5: dict(custom_damage_base=413600),
        6: dict(custom_damage_base=449280),
    },
    37562: {
        1: dict(custom_damage_base=244355),
        2: dict(custom_damage_base=281280),
        3: dict(custom_damage_base=748100),
        4: dict(custom_damage_base=1021200)
    },
    37561: {
        1: dict(custom_damage_base=162903),
        2: dict(custom_damage_base=187520),
        3: dict(custom_damage_base=498800),
        4: dict(custom_damage_base=680800)
    },
    22151: dict(comment="{}"),
    29532: {
        1: dict(custom_damage_base=get_damage(), custom_damage_type="poison")
    }
}
