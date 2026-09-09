TALENTS: list[dict[int, dict]] = [
    {
        41988: dict(skills={
            **{
                skill_id: dict(max_level=4, comment="减弱{level-1}次")
                for skill_id in [34353, 34354, 34355, 34356, 34359, 34361, 34362, 34363]
            },
            35056: {}, 35057: {}, 19055: dict(levels=[10, 11])
        }),
        40190: dict(
            buffs={
                30349: dict(levels=[1], coming_damage_cof=204.8, skills=[4480, 14701, 4476]),
                30350: dict(name="寂灭劫灰", comment="生死劫·月", levels=[3])
            }
        ),
        44446: {},
        46194: {}
    },
    {
        5985: {},
        5967: {},
        5989: {},
        37337: dict(skills={37336: {1: dict(comment="PVP"), 2: dict(comment="PVE")}})
    },
    {
        22888: dict(skills={26916: {
            1: dict(comment="净世破魔击日+净世破魔击月"),
            2: dict(comment="净世破魔击日+生死劫月"),
            3: dict(comment="生死劫日+净世破魔击月"),
            4: dict(comment="生死劫日+生死劫月")
        }}),
        41889: {},
        6727: dict(skills={13851: {}, 13852: {}}),
        6717: dict(buffs={6277: {}})
    },
    {
        25166: dict(
            buffs={1: dict(name="净体不畏", coming_damage_cof=512, skills=[40088, 40089])},
            skills={26708: {}, 26709: {}}
        ),
        34372: dict(dots={25725: dict(skills={34373: {}}), 25726: dict(skills={34374: {}})}),
        21174: dict(skills={40209: {
            **{i + 1: dict(comment=f"{15 * i}%血量(圣裁庭内)") for i in range(10)},
            **{i + 11: dict(comment=f"{15 * i}%血量") for i in range(10)},
        }}),
        32622: {}
    },
    {
        25160: dict(buffs={33108: {}}),
        46263: {},
        32661: dict(buffs={2: dict(name="30%斩杀", coming_damage_cof=512, skills=[44463])},skills={44463: {}}),
        18629: dict(skills={44488: {}})
    },
    {
        28593: dict(skills={30321: {}, 30322: {}, 29932: {}}),
        46264: dict(buffs={34405: {}, 34406: {}, 34407: {}}),
        41762: dict(
            skills={43410: {}, 41765: dict(max_level=6, comment="{}秒")}
        ),
        18626: {}
    },
    {
        3961: dict(skills={3961: {}}),
        5974: {},
        18279: dict(skills={40931: {}, 40932: {}}),
        6718: {},
        46265: {},
        6893: {},
        36093: {},
        41888: {},
        34511: dict(skills={34510: dict(comment="命中{level-1}次")}),
        34383: dict(buffs={25758: {}, 25759: {}}),
        46195: {},
        46269: {}
    }
]
