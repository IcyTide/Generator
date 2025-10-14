SKILLS = {
    35894: dict(channel_interval=24),
    36177: {1: {}},
    **{
        skill_id: dict(comment=f"{i + 1}段({delay})帧")
        for i, (skill_id, delay) in enumerate(zip([36022, 36023], [6, 22]))
    },
    36111: dict(comment="狼(x3)"),
    36056: dict(comment="大象"),
    36057: dict(comment="野猪"),
    36112: dict(comment="虎"),
    36113: dict(comment="鹰"),
    36114: dict(comment="熊"),
    36172: {
        i + 1: dict(comment=f"蓄力{i + 1}段({delay})帧") for i, delay in enumerate([0, 9, 17, 25])
    },
}
