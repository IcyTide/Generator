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
    43592: {1: {}}, 42407: dict(comment="{level-1}层众境"),
    3814: dict(comment="众嗔"),
    37376: dict(comment="{(level-1)*3000}体质"),
    **{skill_id: dict(comment=f"净果{i + 1}豆") for i, skill_id in enumerate([13681, 13683, 13685])},
    **{skill_id: dict(comment=f"净果{i + 1}豆斩杀") for i, skill_id in enumerate([36049, 36050, 36051])},
    3808: {
        0.5: dict(comment="幻身多目标"),
        0: dict(comment="幻身多目标(我闻)")
    },
    3810: {
        0.5: dict(comment="幻身单目标"),
        0: dict(comment="幻身单目标(我闻)")
    },
    43136: {
        0.5: dict(comment="幻身"),
        0: dict(comment="幻身(我闻)")
    },
    271: {
        1: dict(comment="韦陀献杵"),
        5: dict(comment="拿云式"),
    }
}
