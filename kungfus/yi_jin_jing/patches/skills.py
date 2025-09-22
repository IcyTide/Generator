SKILLS = {
    11: dict(channel_interval=27),
    19090: dict(comment="武伤", comments={}),
    3830: dict(comments={
        29: "",
        58: "我闻"
    }),
    3816: dict(comment="原始"),
    **{skill_id: dict(comment=f"{i + 1}豆") for i, skill_id in enumerate([3849, 3850, 3848])},
    **{skill_id: dict(comment=f"原始{i + 1}豆") for i, skill_id in enumerate([13682, 13684, 13686])},
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([17641, 17642])},
    32887: dict(comments={
        1: "韦陀献杵",
        2: "拿云式",
        3: "贪破"
    }),
    28539: dict(comment="无诤"),
    42407: dict(comments={i + 1: f"{i}层" for i in range(3)}),
    3814: dict(comment="众嗔"),
    37376: dict(comments={i + 1: f"{i * 3000}体质" for i in range(5)}),
    **{skill_id: dict(comment=f"净果{i + 1}豆") for i, skill_id in enumerate([13681, 13683, 13685])},
    **{skill_id: dict(comment=f"净果{i + 1}豆斩杀") for i, skill_id in enumerate([36049, 36050, 36051])},
    3808: dict(comment="幻身多目标", comments={
        29: "",
        58: "(我闻)"
    }),
    3810: dict(comment="幻身单目标", comments={
        29: "",
        58: "(我闻)"
    }),
    271: dict(comments={
        1: "韦陀献杵",
        5: "拿云式",
    })

}
