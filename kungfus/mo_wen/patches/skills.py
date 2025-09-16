SKILLS = {
    **{
        skill_id: dict(comments={
            1: "原始",
            2: "觅音100%",
            3: "觅音200%"
        }) for skill_id in [14311, 14312]
    },
    14494: dict(comments={1: "原始"}),
    **{skill_id: dict(comment="影子") for skill_id in [15076, 18663]},
    30762: dict(comments={1: "50%血量以下"}),
    31005: dict(comment="宫"),
    32738: dict(comments={
        **{i + 1: f"曲动九州{i + 1}段" for i in range(3)},
        4: "流照",
        5: "争鸣",
        6: "不愧君",
        7: "崭芒",
    }),
    40815: dict(comment="剑·羽"),
}
