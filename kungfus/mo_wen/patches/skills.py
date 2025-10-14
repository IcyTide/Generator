SKILLS = {
    32738: {i + 1: {} for i in range(3, 8)},
    40815: {
        1: dict(comment="羽"),
        2: dict(comment="剑·羽")
    },
    **{skill_id: {1: {}} for skill_id in [14311, 14312]},
    40293: {i + 1: dict(comment=f"{i + 1}段蓄力({delay}帧)") for i, delay in enumerate([0, 16, 32])},
    14494: {1: dict(comment="原始")}, 30762: {1: dict(comment="50%血量以下")},
    **{skill_id: dict(comment="影子") for skill_id in [15076, 18663]},
    43043: {
        3: dict(comment="1段"),
        4: dict(comment="2段")
    },
    21267: dict(comment="{}段"),
    29077: {
        1: {},
        2: dict(comment="高血量")
    }
}
