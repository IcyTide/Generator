SKILLS = {
    11: dict(channel_interval=27),
    19090: dict(
        comment="武伤",
        comments={}
    ),
    3808: dict(
        comments={
            29: "原始",
            58: "我闻"
        }
    ),
    3814: dict(comment="众嗔"),
    3816: dict(comment="原始"),
    **{skill_id: dict(comment=f"{i + 1}豆") for i, skill_id in enumerate([3849, 3850, 3848])},
    **{skill_id: dict(comment=f"净果{i + 1}豆") for i, skill_id in enumerate([13681, 13683, 13685])},
    **{skill_id: dict(comment=f"原始{i + 1}豆") for i, skill_id in enumerate([13682, 13684, 13686])},
    17641: dict(comment="1段"),
    17642: dict(comment="2段"),
    **{
        skill_id: dict(comments={4: "30700品"}) for skill_id in [23366, 23367, 23368, 23369, 23370]
    },
    32887: dict(
        comments={
            1: "韦陀献杵",
            2: "拿云式",
            3: "贪破"
        }
    ),
    **{skill_id: dict(comment=f"净果{i + 1}豆斩杀") for i, skill_id in enumerate([36049, 36050, 36051])}
}
