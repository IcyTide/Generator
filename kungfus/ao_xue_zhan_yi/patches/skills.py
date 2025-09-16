SKILLS = {
    12: dict(channel_interval=27),
    431: dict(comment="原始"),
    701: dict(comment="自身50%血量以下"),
    702: dict(comment="原始"),
    14882: dict(comment="8尺外"),
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([18207, 18208])},
    32820: dict(
        comments={
            1: "龙牙/灭",
            2: "振甲",
        }
    )
}
