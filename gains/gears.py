KUNGFU_GAINS: dict[int, dict[int, dict]] = {
    10002: {
        1855: dict(buffs={1920: {}}),
        25794: dict(skills={25794: {}})
    },
    10003: {
        1854: dict(buffs={1919: {}}),
        25766: dict(skills={25766: {}})
    },
    10014: {
        1853: dict(buffs={1916: {}}),
        25770: dict(skills={25770: {}})
    },
    10015: {
        1852: dict(buffs={1915: {}}),
        25771: dict(skills={25771: {}})
    },
    10021: {
        1856: dict(dots={
            666: dict(levels=[29], skills={13849: {}}),
            714: dict(levels=[24], skills={13847: {}}),
            711: dict(levels=[19], skills={13848: {}})
        }),
        25768: dict(skills={25768: {}})
    },
    10026: {
        1850: dict(buffs={1911: {}}, skills={31031: {}}),
        25772: dict(skills={25772: {}})
    },
    10062: {
        1851: dict(skills={31031: {}}),
        25795: dict(skills={25795: {}})
    },
    10081: {
        1858: dict(dots={18512: dict(skills={25757: {}})}),
        25769: dict(skills={25769: {}})
    },
    10144: {
        18881: dict(skills={6954: {}}),
        25785: dict(skills={25785: {}}),
        1882: dict(skills={35051: {1: dict(comment="夕照雷峰"), 2: dict(comment="云飞玉皇")}}),
        25776: dict(skills={25776: {}})
    },
    10175: {
        3065: dict(skills={39036: {}}),
        25773: dict(skills={25773: {}})
    },
    10224: {
        3477: dict(skills={43208: {}}),
        25775: dict(skills={25775: {}})
    },
    10225: {
        3476: dict(skills={3480: {}}),
        25774: dict(skills={25774: {}}),
    },
    10242: {
        4940: dict(skills={35065: dict(levels=[1])}),
        25777: dict(skills={25777: {}})
    },
    10243: {
        4941: dict(skills={35065: dict(levels=[2])}),
        25796: dict(skills={25796: {}})
    },
    10268: {
        6950: dict(buffs={6466: {}}, skills={32898: dict(levels=[4])}),
        25779: dict(skills={25779: {}})
    },
    10389: {
        13410: dict(buffs={8474: {}}),
        25797: dict(skills={25797: {}})
    },
    10390: {
        13410: dict(buffs={8474: {}}, dots={34108: dict(skills={45677: {}})}),
        25780: dict(skills={25780: {}})
    },
    10447: {
        15183: dict(skills={43294: dict(comment="{}")}),
        25781: dict(skills={25781: {}})
    },
    10464: {
        16984: dict(buffs={11376: {}}, dots={34119: dict(skills={45704: {}})}, skills={39106: {}}),
        25782: dict(skills={25782: {}})
    },
    10533: {
        21185: dict(dots={19557: dict(skills={26935: {}})}),
        25783: dict(skills={25783: {}})
    },
    10585: {
        23396: dict(dots={19626: dict(skills={26980: {}})}),
        25784: dict(skills={25784: {}})
    },
    10615: {
        25831: dict(skills={33588: {1: dict(comment="兵主逆"), 2: dict(comment="天斗旋")}}),
        25837: dict(skills={25837: {}, }),
    },
    10626: {
        29694: dict(skills={29695: {}}),
        29698: dict(skills={29698: {}})
    },
    10698: {
        33238: dict(buffs={32797: dict(name="橙武增伤")}),
        33239: dict(skills={33239: {}})
    },
    10756: {
        36578: dict(skills={36580: {}}),
        36579: dict(skills={36579: {}})
    },
    10786: {
        39078: {},
        39081: dict(skills={39081: {}})
    },
    10821: {
        43080: dict(dots={32145: dict(skills={43082: {}})}, skills={43081: {}}),
        43086: dict(skills={43086: {}})
    }
}

DIVINE_WEAPON_GAINS: dict[int, dict] = {
    # divine strain
    39088: dict(name="橙武无双", buffs={29608: dict(levels=list(range(18, 30)))}),
    **{k: v for gain in KUNGFU_GAINS.values() for k, v in gain.items()}
}
SPECIAL_GEAR_GAINS: dict[int, dict] = {
    # dps wrist
    42767: dict(name="加速护手特效",
                skills={42837: dict(levels=[3], custom_damage_source="tDPSJingJianYaoDaiData")}),
    40788: dict(
        name="输出护手特效",
        skills={40789: dict(levels=list(range(4, 8)), custom_damage_source="tDPSJingJianHuShouData")}
    ),

    # dps shoes
    38939: dict(name="会心鞋子特效", buffs={29524: dict(levels=list(range(9, 11)), name="会心鞋子特效")}),
    38944: dict(name="破防鞋子特效", buffs={29526: dict(levels=list(range(9, 11)), name="破防鞋子特效")}),

    # dps belt
    40790: dict(name="多属性腰带特效", buffs={30742: dict(levels=list(range(4, 7)), name="多属性腰带特效")}),
    40791: dict(
        name="单属性腰带特效",
        buffs={
            30743: {
                level: dict(name="单属性腰带特效", comment=["会心", "破防"][i % 2])
                for i, level in enumerate([9, 10])
            }
        }
    ),

    # dps hat
    38934: dict(
        name="帽子特效",
        buffs={
            29519: {
                level: dict(name="帽子特效", comment=["破防", "会心"][i % 2])
                for i, level in enumerate([25, 26, 28, 29])
            }
        }
    ),

    # dps ring
    41065: dict(name="加速戒指特效", buffs={30950: dict(levels=[7], name="加速戒指特效")}),
    40802: dict(name="破防戒指特效", buffs={30755: dict(levels=[7, 9], name="破防戒指特效")}),
    40803: dict(name="会心戒指特效", buffs={30756: dict(levels=[7, 9], name="会心戒指特效")}),

    # dps necklace
    38946: dict(name="破防项链特效", buffs={29529: dict(levels=list(range(9, 14)), name="破防项链特效")}),
    38945: dict(name="会心项链特效", buffs={29528: dict(levels=list(range(9, 11)), name="会心项链特效")}),

    # dps tertiary_weapon
    38950: dict(
        name="暗器特效", skills={38966: dict(levels=list(range(9, 15)), custom_damage_source="tDPSJingJianAnQiData")}
    ),
    34831: dict(name="暗器特效", buffs={34831: dict(levels=[1, 2], name="加速暗器特效")})
}
SPECIAL_WEAPON_GAINS: dict[int, dict] = {
}
ELEMENT_GAINS = {
    4877: dict(name="水特效", buffs={4761: dict(levels=[87, 88])}),
    # pendant
    38578: dict(name="风特效", buffs={29268: dict(levels=[36])}),
}
SPECIAL_ENCHANT_GAINS = {
    # dps
    10106: dict(name="头大附魔", buffs={15436: dict(name="头大附魔", levels=[18, 19])}),
    46463: dict(
        name="手大附魔", skills={37562: {
            1: dict(custom_damage_base=13524),
            2: dict(custom_damage_base=19745)
        }}),
    46464: dict(
        name="脚大附魔", skills={37561: {
            1: dict(custom_damage_base=9017),
            2: dict(custom_damage_base=13164)
        }}),
    22151: dict(skills={22151: dict(levels=[18, 19])}),
    22169: dict(name="腰大附魔", buffs={
        15455: {1: dict(name="腰大附魔", comment="1%"), 2: dict(name="腰大附魔", comment="5%")}
    })
}
GAINS: dict[int, dict] = {
    **DIVINE_WEAPON_GAINS,
    **SPECIAL_GEAR_GAINS,
    # **SPECIAL_WEAPON_GAINS,
    **ELEMENT_GAINS,
    **SPECIAL_ENCHANT_GAINS,
}
