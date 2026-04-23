TALENTS: list[dict[int, dict]] = [
    {
        24896: dict(buffs={21638: dict(attributes=[("coming_damage_cof", 460.8)], skills=[18773])}),
        30654: dict(skills={
            30800: {}, 30808: {}
        }),
        15158: dict(skills={
            15163: {i + 1: dict(comment=f"{i + 1}段({delay}帧)") for i, delay in enumerate([10, *range(16, 27), 40])}
        }),
        18226: dict(
            dots={12461: dict(skills={401: {}})},
            skills={36568: {}}
        )
    },
    {
        6524: dict(skills={
            6525: dict(comment="自身<50%血量"),
            6526: dict(comment="自身>50%血量"),
            32820: dict(levels=[1])
        }),
        6514: {},
        28442: {},
        44374: {}
    },
    {
        38671: dict(skills={38673: {}}),
        5673: {},
        44373: {},
        37338: dict(skills={37350: dict(comment="{}目标")})
    },
    {
        23997: {},
        6530: dict(skills={32909: {}}),
        44372: {},
        6511: dict(buffs={7671: dict(levels=[1])})
    },
    {
        5669: {},
        24841: dict(skills={24843: {
                **{i + 1: dict(comment=f"蓄力{delay}帧") for i, delay in enumerate([0, 12, 23])},
                **{i + 4: dict(comment=f"蓄力{delay}帧(<80%血量)") for i, delay in enumerate([0, 12, 23])}
            }
        }),
        14824: {},
        30653: dict(skills={24894: {}})
    },
    {
        6806: {},
        5678: {},
        42672: {},
        24899: {}
    },
    {
        18557: dict(skills={32979: {}, 32980: {}}),
        42670: dict(skills={36258: {}}),
        6781: dict(buffs={26008: dict(name="战心")}),
        42671: {},
        15001: dict(skills={15002: {}}),
        14821: dict(dots={19317: dict(comment="击水+牙璋", skills={26773: {}})}),
        28564: {},
        42273: dict(skills={42274: {}}),
        18487: {},
        5666: dict(buffs={12608: dict(name="风虎", comment="{}")}),
        2628: {},
        44401: {}
    }
]
