SKILLS = {
    11: dict(channel_interval=27),
    19090: dict(comment="武伤{}"),
    32887: {
        1: dict(comment="韦陀献杵"),
        2: dict(comment="拿云式")
    },
    17641: dict(comment="1段"), 17642: dict(comment="2段"),
    3830: {0.5: dict(comment="原始")},
    43073: {0.5: dict(comment="原始")},
    **{skill_id: dict(comment=f"{i + 1}豆") for i, skill_id in enumerate([3849, 3850, 3848])},
    **{skill_id: dict(comment=f"原始{i + 1}豆") for i, skill_id in enumerate([13682, 13684, 13686])},
    **{skill_id: dict(comment=f"七宝{i + 1}豆") for i, skill_id in enumerate([13681, 13683, 13685])},
    3812: {0.5: dict(comment="幻身")}
}
