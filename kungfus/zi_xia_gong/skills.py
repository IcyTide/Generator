SKILLS: dict[int, dict[int, dict]] = {
    10014: {
        18121: dict(channel_interval=21)
    },
    367: {
        896: {}
    },
    301: {
        **{
            skill_id: dict(comment=f"{i + 1}豆")
            for i, skill_id in enumerate([3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448])
        },
        32813: {
            1: dict(comment="6-7豆"),
            2: dict(comment="8豆"),
            3: dict(comment="9-10豆")
        }
    },
    306: {
        2329: {}
    },
    303: {
        303: {}
    },
    368: {
        15209: {}
    },
    18640: {
        **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([18649, 18650, 18651, 18652, 18653])},
        22014: dict(levels=[1]),
        32813: dict(levels=[4])
    },
    2674: {
        **{
            skill_id: dict(comment=f"{i + 1}豆")
            for i, skill_id in enumerate([327, 328, 329, 330, 331, 461, 462, 463, 464, 465])
        },
    },
    305: {
        305: {}
    }
}
