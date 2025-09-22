SKILLS = {
    12: dict(channel_interval=27),
    431: dict(comment="原始"),
    701: dict(comment="自身50%血量以下"),
    702: dict(comment="原始"),
    6525: dict(comment="破楼兰(自身50%气血以下)"),
    6526: dict(comment="破楼兰"),
    14882: dict(comment="8尺外"),
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([18207, 18208])},
    32820: dict(comments={
        1: "龙牙/灭",
        2: "振甲",
    }),
    15163: dict(comments={i + 1: f"{i + 1}段({delay}帧)" for i, delay in enumerate([10, range(16, 27), 40])}),
    20778: dict(comments={i + 1: f"飞将{i + 1}段({delay}帧)" for i, delay in enumerate([10, range(16, 27), 40])}),
    24843: dict(comments={
        **{i + 1: f"蓄力{i + 1}段({delay}帧)" for i, delay in enumerate([0, 12, 23])},
        **{i + 4: f"高血量蓄力{i + 1}段({delay}帧)" for i, delay in enumerate([0, 12, 23])}
    }),
    36258: dict(comments={4: ""}),
}
