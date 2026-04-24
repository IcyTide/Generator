from base.expression import Variable

DIVINE_WEAPON_GAINS: dict[int, dict] = {
    # divine strain
    39088: dict(name="橙武无双", buffs={29608: dict(comment="{}")}),

    # kungfu
    25794: dict(buffs={1920: {}}, skills={25794: {}}),
    25766: dict(buffs={1919: {}}, skills={25766: {}}),
    25770: dict(buffs={1916: {}}, skills={25770: {}}),
    25771: dict(buffs={1915: {}}, skills={25771: {}}),
    25768: dict(
        dots={
            666: dict(levels=[29], skills={13849: {}}),
            714: dict(levels=[24], skills={13847: {}}),
            711: dict(levels=[19], skills={13848: {}})
        },
        skills={25768: {}}
    ),
    25772: dict(skills={25772: {}, 31031: {}}),
    25795: dict(skills={25795: {}}),
    25769: dict(dots={18512: dict(skills={25757: {}})}, skills={25769: {}}),
    25785: dict(skills={25785: {}, 6954: {}}),
    25776: dict(skills={
        25776: {},
        35051: {
            1: dict(comment="夕照雷峰"),
            2: dict(comment="云飞玉皇")
        }
    }),
    25773: dict(skills={25773: {}, 39036: {}}),
    25775: dict(skills={25775: {}, 43208: {}}),
    25774: dict(skills={25774: {}, 3480: {}}),
    25777: dict(skills={25777: {}, 35065: dict(levels=[1])}),
    25796: dict(skills={25796: {}, 35065: dict(levels=[2])}),
    25779: dict(skills={25779: {}, 32898: dict(levels=[4])}),
    25797: dict(buffs={8474: {}}, skills={25797: {}}),
    25780: dict(buffs={8474: {}}, skills={25780: {}}),
    25781: dict(
        dots={23187: {
            1: dict(levels=[1], skills={40815: dict(levels=[1])}),
            2: dict(levels=[2], skills={40815: dict(levels=[2])}),
        }},
        skills={25781: {}, 43294: dict(levels=[1, 2])}
    ),
    25782: dict(skills={25782: {}, 39106: {}}),
    25783: dict(dots={19557: dict(skills={26935: {}})}, skills={25783: {}}),
    25784: dict(dots={19626: dict(skills={26980: {}})}, skills={25784: {}}),
    25837: dict(skills={
        25837: {},
        33588: {
            1: dict(comment="兵主逆"),
            2: dict(comment="天斗旋")
        }
    }),
    29698: dict(skills={29698: {}, 29695: {}}),
    33239: dict(buffs={32797: dict(name="橙武增伤")}, skills={33239: {}}),
    36579: dict(skills={36579: {}, 36580: {}}),
    39081: dict(skills={39081: {}}),
    43086: dict(dots={32145: dict(skills={43082: {}})}, skills={43086: {}, 43081: {}})
}
SPECIAL_GEAR_GAINS: dict[int, dict] = {
    # dps wrist
    40788: dict(name="输出护手特效", skills={40789: dict(levels=[1, 2, 3], custom_damage_source=40788)}),
    # tank wrist
    41062: dict(name="防御护手特效", skills={41069: dict(levels=[1], custom_damage_source=41062)}),
    42895: dict(
        name="防御护手特效", buffs={32019: {}},
        skills={42898: dict(levels=[1, 2], custom_damage_source=42897)}
    ),

    # dps bottom
    40793: dict(name="单属性下装特效", buffs={30748: dict(levels=[1, 2, 3], name="单属性下装特效")}),
    40794: dict(name="多属性下装特效", buffs={
        30749: {
            level: dict(name="多属性下装特效", comment='无双' if level % 2 else '破防')
            for level in [1, 2, 3, 4, 5, 6]
        },
        30770: {
            level: dict(name="多属性下装特效", comment='无双' if level % 2 else '会心')
            for level in [1, 2, 3, 4, 5, 6]
        }
    }),
    # tank bottom
    41064: dict(
        name="防御下装特效", buffs={30948: dict(levels=[1, 2, 3])},
        skills={41073: dict(levels=[1, 2, 3], custom_damage_base=Variable("max_life") * 0.065)}
    ),

    # dps belt
    40790: dict(name="多属性腰带特效", buffs={30742: dict(levels=[1, 2, 3], name="多属性腰带特效")}),
    40791: dict(
        name="单属性腰带特效",
        buffs={
            30743: {
                **{
                    level: dict(name="单属性腰带特效", comment=["破招", "会心", "破防"][level % 3])
                    for level in [1, 2, 3, 4, 5, 6]
                },
                **{
                    level: dict(name="单属性腰带特效", comment=["破防", "会心"][level % 2])
                    for level in [7, 8]
                }
            }
        }
    ),
    42767: dict(name="加速腰带特效", skills={42837: dict(levels=[1, 2], custom_damage_source=42768)}),
    # tank belt
    41063: dict(name="防御腰带特效", buffs={30946: dict(levels=[1, 2, 3], name="防御腰带特效")}),

    # dps ring
    40802: dict(name="破防戒指特效", buffs={30755: dict(levels=[1, 3, 5], name="破防戒指特效")}),
    40803: dict(name="会心戒指特效", buffs={30756: dict(levels=[1, 3, 5], name="会心戒指特效")}),
    40804: dict(name="破招戒指特效", buffs={30757: dict(levels=[1, 3, 5], name="破招戒指特效")}),
    # tank ring
    41065: dict(name="防御戒指特效", buffs={30950: dict(levels=[1, 3, 5], name="防御戒指特效")}),

    # dps hat
    38934: dict(
        name="帽子特效",
        buffs={
            29519: {
                level: dict(name="帽子特效", comment=["破招", "破防", "会心"][level % 3])
                for level in [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
            }
        }
    ),

    # dps shoes
    38939: dict(name="会心鞋子特效", buffs={29524: dict(levels=[4, 5, 6, 7, 8], name="会心鞋子特效")}),
    38944: dict(name="破防鞋子特效", buffs={29526: dict(levels=[4, 5, 6, 7, 8], name="破防鞋子特效")}),

    # dps necklace
    38945: dict(name="会心项链特效", buffs={29528: dict(levels=[4, 5, 6, 7, 8], name="会心项链特效")}),
    38946: dict(name="破防项链特效", buffs={29529: dict(levels=[4, 5, 6, 7, 8], name="破防项链特效")}),
    # dps pendant
    38948: dict(name="会心腰坠特效", buffs={29536: dict(levels=[4, 5, 6, 7, 8], name="会心腰坠特效")}),
    38949: dict(name="破防腰坠特效", buffs={29537: dict(levels=[4, 5, 6, 7, 8], name="破防腰坠特效")}),
    # dps tertiary_weapon
    38950: dict(name="暗器特效", skills={38966: dict(levels=[4, 5, 6, 7, 8], custom_damage_source=38950)}),
}
SPECIAL_WEAPON_GAINS: dict[int, dict] = {
}
ELEMENT_GAINS = {
    # weapon
    4877: dict(name="水特效", buffs={4761: dict(levels=[74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85])}),
    # pendant
    38578: dict(name="输出风特效", buffs={29268: dict(levels=[12, 13, 20, 21, 28, 29])}),
    38786: dict(
        name="防御风特效",
        skills={
            38787: {
                level: dict(comment='精准反击' if level % 2 else '', custom_damage_source=38787)
                for level in [3, 4, 5, 6, 7, 8]
            }
        }
    ),
}
SPECIAL_ENCHANT_GAINS = {
    # dps
    10106: dict(name="输出头大附魔", buffs={15436: dict(name="输出头大附魔", levels=[15, 16, 17])}),
    38984: dict(name="输出手大附魔", skills={37562: dict(levels=[3, 4, 5], custom_damage_source=38984)}),
    38985: dict(name="输出脚大附魔", skills={37561: dict(levels=[3, 4, 5], custom_damage_source=38985)}),
    22151: dict(skills={22151: dict(levels=[15, 16, 17])}),
    22169: dict(name="输出腰大附魔", buffs={
        15455: {1: dict(name="输出腰大附魔", comment="1%"), 2: dict(name="输出腰大附魔", comment="5%")}
    }),

    # tank
    22129: {},
    33249: dict(name="防御手大附魔", buffs={24767: {}}),
    22128: {},
    22122: {},
    40512: {}

}
GAINS: dict[int, dict] = {
    **DIVINE_WEAPON_GAINS,
    **SPECIAL_GEAR_GAINS,
    **SPECIAL_WEAPON_GAINS,
    **ELEMENT_GAINS,
    **SPECIAL_ENCHANT_GAINS,
}
