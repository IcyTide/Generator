SKILLS = {
    32738: dict(comments={i + 1: "" for i in range(3, 8)}),
    **{skill_id: dict(comments={1: ""}) for skill_id in [14311, 14312]},
    40293: dict(comments={i + 1: f"{i + 1}段蓄力({delay}帧)" for i, delay in enumerate([0, 16, 32])}),
    14494: dict(comments={1: "原始"}), 30762: dict(comments={1: "50%血量以下"}),
    **{skill_id: dict(comment="影子") for skill_id in [15076, 18663]},
    40815: dict(comments={
        1: "羽",
        2: "剑·羽"
    }),
    21267: dict(comments={1: "1段", 2: "2段"}),
    29077: dict(comments={1: "", 2: "高血量"})
}
