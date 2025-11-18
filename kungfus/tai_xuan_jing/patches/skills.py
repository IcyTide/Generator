SKILLS = {
    32886: {
        1: dict(comment="兵主逆"),
        3: dict(comment="天斗旋")
    },
    33588: {
        1: dict(comment="兵主逆"),
        2: dict(comment="天斗旋")
    },
    **{
        skill_id: dict(comment=comment)
        for skill_ids in [[24558, 24675, 24676, 24677], [24811, 24812, 24813, 24814], [24824, 24822, 24823, 24821]]
        for skill_id, comment in zip(skill_ids, ["原始", "水坎", "山艮", "火离"])
    },
    25233: {
        -3: {},
        **{i - 2: dict(comment=f"擎羊{i + 1}灯魂") for i in range(3)},
    },
    42423: {
        2: dict(comment="主动"),
        3: dict(comment="主动12尺")
    },
    42509: {
        1: dict(comment="1段"),
        2: dict(comment="2段(PVE)"),
        3: dict(comment="2段(PVP)")
    },
    42456: dict(comment="{}层"),
    42520: {
        1: dict(comment="PVP"), 
        2: dict(comment="PVE")
    },
    28815: {
        2: dict(comment="连极阵"),
        3: dict(comment="12尺连极阵")
    },
    25031: dict(comment="焚如")

}
