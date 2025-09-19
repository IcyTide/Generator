SKILLS = {
    **{
        skill_id: dict(comment=f"{i + 1}豆")
        for i, skill_id in enumerate([386, 387, 388, 389, 390, 391, 392, 393, 394])
    },
    4954: dict(
        comments={
            1: "原始",
            2: "50%血量以下",
            3: "20%血量以下"
        }
    ),
    17689: dict(
        comment="1段"
    ),
    17690: dict(
        comment="2段"
    ),
    18121: dict(channel_interval=21),
    18528: dict(comments={}),
    21979: dict(comments={}),
    32814: dict(
        comments={
            1: "三环套月",
            2: "无我无剑6-8豆",
            3: "无我无剑9-10豆"
        }
    ),
    40752: dict(comments={}),
    42061: dict(comments={i + 1: f"{i + 1}层叠刃" for i in range(7)}),
    30828: dict(comments={i + 1: f"{i + 1}层" for i in range(3)}),

}
