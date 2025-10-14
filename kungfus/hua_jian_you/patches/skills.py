SKILLS = {
    16: dict(channel_interval=16),
    32467: {
        **{i + 1: dict(comment=f"吞噬{i + 1}跳") for i in range(7)},
        8: dict(comment="墨海临源"),
        9: dict(comment="快雪时晴")
    },
    **{skill_id: dict(comment="芙蓉并蒂") for skill_id in [6134, 6135, 6136]},
    **{skill_id: {1: dict(comment="乱洒青荷"), 2: dict(comment="渲青")} for skill_id in [39906, 39907]},
    **{skill_id: dict(comment="飞白1段") for skill_id in [34280, 34278, 34279]},
    **{skill_id: dict(comment="飞白2段") for skill_id in [40085, 40084, 40086]},
    32501: {
        1: dict(comment="钟林毓秀"),
        2: dict(comment="商阳指"),
        3: dict(comment="兰摧玉折"),
    },
    **{skill_id: dict(comment="风烟翠/随墨/流离") for skill_id in [13849, 13847, 13848]},
    38854: dict(comment="雪弃{}目标"),
    37270: {
        2: dict(comment="PVE"),
        4: dict(comment="PVP")
    }
}
