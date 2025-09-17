SKILLS = {
    19712: dict(channel_interval=24),
    32815: dict(comments={
        5: "跃潮斩波",
        6: "木落雁归"
    }),
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([19766, 19767, 20014])},
    20684: dict(comment="8尺内"),
    20685: dict(comment="4尺内"),
    20840: dict(comment="水龙卷", comments={
        i + 1: f"{i}层增伤" for i in range(3)
    }),
    25299: dict(comments={
        1: "浮空",
        2: ""
    }),
    30503: dict(comments={i + 1: f"{i + 1}段" for i in range(2)}),
    20605: dict(comment="1段"),
    20632: dict(comment="2段"),
    36417: dict(comment="3段", comments={
        1: "原始", 2: "击倒"
    }),
    34728: dict(comments={
        1: "1段",
        **{i + 2: f"2段({height}尺以上)" for i, height in enumerate([0, 15, 20, 25])}
    })
}
