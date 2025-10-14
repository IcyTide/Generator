SKILLS = {
    18121: dict(channel_interval=21),
    32814: {
        1: dict(comment="三环套月"),
        2: dict(comment="无我无剑6-8豆"),
        3: dict(comment="无我无剑9-10豆")
    },
    600: {
        1: dict(comment="原始"),
        2: dict(comment="裂云"),
    },
    17689: dict(comment="1段"), 17690: dict(comment="2段"),
    **{
        skill_id: dict(comment=f"{i + 1}豆")
        for i, skill_id in enumerate([386, 387, 388, 389, 390, 391, 392, 393, 394])
    },
    4954: {
        1: dict(comment="原始"),
        2: dict(comment="50%血量以下"),
        3: dict(comment="20%血量以下")
    },
    18528: dict(comment="{}"),
    21979: dict(comment="{}"),
    40752: {1: {}, 2: {}},
    42061: dict(comment="{}层叠刃"),
    30828: dict(comment="{}层"),
}
