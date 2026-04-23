TALENTS: list[dict[int, dict]] = [
    {
        44370: dict(skills={32659: {}}),
        32649: dict(skills={28542: {}}, dots={743: dict(levels=[29], skills={28539: dict(levels=[29])}), }),
        44405: dict(skills={
            **{skill_id: dict(comment=f"{i + 4}豆") for i, skill_id in enumerate([44416, 44417, 44418])},
            **{skill_id: dict(comment=f"{i + 4}豆") for i, skill_id in enumerate([44421, 44422, 44423])}
        }),
        42405: dict(skills={43592: {}, 42407: {}})
    },
    {
        44994: dict(buffs={33522: dict(name="众嗔")}),
        6595: {},
        37369: dict(skills={37374: {}}),
        240: {}
    },
    {
        6590: dict(
            buffs={1: dict(
                name="六度净果斩杀", comment="<30%血量",
                attributes=[("coming_damage_cof", 154)],
                skills=[44421, 44422, 44423]
            )},
            skills={
                **{skill_id: dict(comment=f"净果{i + 1}豆") for i, skill_id in enumerate([13681, 13683, 13685])},
                **{skill_id: dict(comment=f"净果{i + 1}豆斩杀") for i, skill_id in enumerate([36049, 36050, 36051])}
            }
        ),
        42406: dict(buffs={31804: {}}),
        14758: {},
        18623: {},
    },
    {
        17730: dict(buffs={11979: {}}),
        14750: dict(buffs={2686: dict(levels=[3])}),
        38621: dict(skills={38622: {}}),
        259: {}
    },
    {
        45103: dict(buffs={33672: {}}),
        44441: dict(skills={44449: {}}),
        32647: {},
        38623: dict(buffs={29304: {}})
    },
    {
        32648: dict(skills={32656: {}}),
        21703: dict(buffs={14916: dict(name="缘觉", levels=[1])}),
        21697: dict(skills={21700: {}}),
        14752: dict(buffs={9809: dict(levels=[1]), 11981: dict(comment="金刚怒目+五识")})
    },
    {
        44399: dict(skills={44394: dict(comment="增伤{level-1}次")}),
        14793: {},
        14795: {},
        6580: {},
        5915: dict(buffs={21859: {}}),
        16886: {},
        5913: dict(skills={271: {
            1: dict(comment="韦陀献杵"),
            5: dict(comment="拿云式"),
        }}),
        24884: dict(
            dots={743: dict(levels=[58], skills={43073: dict(levels=[58])}),},
            skills={3830: {58: {}}}
        ),
        44365: dict(
            buffs={2: dict(
                name="布泽斩杀", comment="<30%血量",
                attributes=[("coming_damage_cof", 512)],
                skills=[38615]
            )},
            skills={38615: dict(max_level=6, comment="{}层贪破")}
        ),
        6587: {},
        37370: {},
        42920: {}
    }
]
