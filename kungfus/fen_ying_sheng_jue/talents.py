TALENTS: list[dict[int, dict]] = [
    {
        25160: dict(buffs={33108: {}}),
        44447: {},
        32661: dict(skills={44463: {}, 44464: {}}),
        18629: {}
    },
    {
        5985: {},
        5967: {},
        5989: {},
        38526: dict(skills={34985: {}, 32816: dict(levels=[2])})
    },
    {
        22888: dict(skills={26916: {
            1: dict(comment="净世破魔击日+净世破魔击月"),
            2: dict(comment="净世破魔击日+生死劫月"),
            3: dict(comment="生死劫日+净世破魔击月"),
            4: dict(comment="生死劫日+生死劫月")
        }}),
        41889: {},
        44487: dict(
            buffs={33518: {}},
            skills={44488: dict(comment="{}")}
        ),
        6717: dict(buffs={6277: {}})
    },
    {
        25166: dict(
            buffs={1: dict(name="净体不畏", attributes=[("coming_damage_cof", 512)], skills=[40088, 40089])},
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
        41988: dict(skills={
            skill_id: dict(max_level=4, comment="{}层影子")
            for skill_id in [34353, 34354, 34355, 34356, 34359, 34361, 34362, 34363]
        }),
        34511: dict(skills={34510: dict(comment="命中{level-1}次")}),
        44446: dict(buffs={33107: dict(
            name="日月连璧", attributes=[("coming_damage_cof", -921.6)], skills=[4028, 4029, 4030, 4024, 4025, 4026]
        )}),
        40190: {}
    },
    {
        28593: dict(skills={30321: {}, 30322: {}, 29932: {}}),
        37337: dict(skills={37336: {
            **{i + 1: dict(comment=f"连续施展{i}次") for i in range(3)},
            **{i + 4: dict(comment=f"连续施展{i}次高血量") for i in range(3)}
        }}),
        41762: dict(skills={43410: {}, 41765: dict(max_level=6, comment="{}秒")}),
        18626: {}
    },
    {
        3961: dict(skills={3961: {}}),
        5974: {},
        18279: dict(skills={40931: {}, 40932: {}}),
        6718: {},
        6727: dict(skills={13851: {}, 13852: {}}),
        6893: {},
        36093: {},
        41888: {},
        14695: {},
        34383: dict(buffs={25758: {}, 25759: {}}),
        5979: dict(buffs={4754: dict(levels=[1])}),
        17567: dict(buffs={12575: {
            **dict(name="用晦而明"),
            1: {},
            2: dict(comment="强化")
        }})
    }
]
