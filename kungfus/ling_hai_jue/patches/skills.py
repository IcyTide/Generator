SKILLS = {
    19712: dict(channel_interval=24),
    32815: {
        5: dict(comment="跃潮斩波"),
        6: dict(comment="木落雁归")
    },
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([19766, 19767, 20014])},
    20684: dict(comment="8尺内"), 20685: dict(comment="4尺内"),
    20840: dict(comment="水龙卷{level-1}层增伤"),
    25299: {
        1: dict(comment="浮空"),
        2: dict(comment="")
    },
    30503: {i + 1: dict(comment=f"{i + 1}段") for i in range(2)},
    20605: dict(comment="1段"),
    20632: dict(comment="2段"),
    36417: {
        1: dict(comment="3段原始"),
        2: dict(comment="3段击倒")
    },
    41836: dict(comment="九溟"),
    34728: {
        1: dict(comment="1段"),
        **{i + 2: dict(comment=f"2段({height}尺以上)") for i, height in enumerate([0, 15, 20, 25])}
    }
}
