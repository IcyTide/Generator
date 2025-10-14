SKILLS = {
    18121: dict(channel_interval=21),
    32813: {
        1: dict(comment="两仪化形6-7豆"),
        2: dict(comment="两仪化形8豆"),
        3: dict(comment="两仪化形9-10豆"),
        4: dict(comment="万世不竭"),
        5: dict(comment="两仪化形11-12豆"),
        6: dict(comment="两仪化形13-15豆"),
        7: dict(comment="两仪化形16豆")
    },
    **{
        skill_id: dict(comment=f"{i + 1}豆")
        for i, skill_id in enumerate([327, 328, 329, 330, 331, 461, 462, 463, 464, 465])
    },
    **{
        skill_id: dict(comment=f"{i + 1}豆")
        for i, skill_id in enumerate([3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448])
    },
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([18649, 18650, 18651, 18652, 18653])},
    22014: {
        1: dict(comment="原始"),
        2: dict(comment="万物")
    },
    40158: dict(comment="{level+10}豆"),
    28590: {
        1: dict(comment="连续命中"),
        2: dict(comment="首次")
    },
    21860: dict(comment="自化"),
    36102: {
        1: dict(comment="原始"),
        2: dict(comment="70%血量以上")
    }
}
