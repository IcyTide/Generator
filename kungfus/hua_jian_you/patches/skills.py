SKILLS = {
    16: dict(channel_interval=16),
    **{skill_id: dict(comment="芙蓉并蒂") for skill_id in [6134, 6135, 6136]},
    **{skill_id: dict(comment="乱洒青荷", comments={1: "原始", 2: "渲青"}) for skill_id in [39906, 39907]},
    32467: dict(
        comments={
            **{i + 1: f"吞噬{i + 1}跳" for i in range(7)},
            8: "墨海临源",
            9: "快雪时晴"
        }
    ),
    **{skill_id: dict(comment="飞白1段") for skill_id in [34280, 34278, 34279]},
    **{skill_id: dict(comment="飞白2段") for skill_id in [40085, 40084, 40086]},
    32501: dict(comments={
        1: "钟林毓秀",
        2: "商阳指",
        3: "兰摧玉折",
    }),
    **{skill_id: dict(comment="风烟翠/随墨/流离") for skill_id in [13849, 13847, 13848]},
    38854: dict(comment="雪弃", comments={i + 1: f"{i + 1}目标" for i in range(5)}),
    37270: dict(comments={2: "PVE", 4: "PVP"})
}
