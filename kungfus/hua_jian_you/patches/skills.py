SKILLS = {
    16: dict(channel_interval=16),
    3808: dict(
        comments={
            29: "原始",
            58: "我闻"
        }
    ),
    **{skill_id: dict(comment="芙蓉并蒂") for skill_id in [6134, 6135, 6136]},
    **{
        skill_id: dict(comments={4: "30700品"}) for skill_id in [23402, 22075, 21309, 22047]
    },
    **{skill_id: dict(comment="乱洒青荷") for skill_id in [39906, 39907]},
    32467: dict(
        comments={
            **{i + 1: f"吞噬{i + 1}跳" for i in range(7)},
            8: "墨海临源",
            9: "快雪时晴"
        }
    )
}
