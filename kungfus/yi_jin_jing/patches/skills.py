SKILLS = {
    11: dict(channel_interval=27),
    19090: dict(comment="武伤{}"),
    32887: {
        1: dict(comment="韦陀献杵"),
        2: dict(comment="拿云式"),
        3: dict(comment="贪破")
    },
    17641: dict(comment="1段"), 17642: dict(comment="2段"),
    3830: {
        0.5: dict(comment="原始"),
        0: dict(comment="我闻")
    },
    43073: {
        0.5: dict(comment="原始"),
        0: dict(comment="我闻")
    },
    **{skill_id: dict(comment=f"{i + 1}豆") for i, skill_id in enumerate([3849, 3850, 3848])},
    **{skill_id: dict(comment=f"原始{i + 1}豆") for i, skill_id in enumerate([13682, 13684, 13686])},

    28539: {
        0.5: dict(comment="无诤"),
        0: dict(comment="无诤(我闻)")
    },
    **{skill_id: dict(comment=f"六度{i + 4}豆") for i, skill_id in enumerate([44416, 44417, 44418])},
    **{skill_id: dict(comment=f"六度原始{i + 4}豆") for i, skill_id in enumerate([44421, 44422, 44423])},
    43592: {1: {}}, 42407: dict(comment="{level-1}层藏识"),
    **{skill_id: dict(comment=f"净果{i + 1}豆") for i, skill_id in enumerate([13681, 13683, 13685])},
    **{skill_id: dict(comment=f"净果{i + 1}豆斩杀") for i, skill_id in enumerate([36049, 36050, 36051])},
    44394: dict(comment="收缩{}次"),
    271: {
        1: dict(comment="韦陀献杵"),
        5: dict(comment="拿云式"),
    },
    38615: dict(max_level=6, comment="{}层贪破")
}
