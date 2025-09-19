SKILLS = {
    32886: dict(comments={
        1: "兵主逆",
        3: "天斗旋"
    }),
    **{
        skill_id: dict(comment=comment)
        for skill_ids in [[24558, 24675, 24676, 24677], [24811, 24812, 24813, 24814], [24824, 24822, 24823, 24821]]
        for skill_id, comment in zip(skill_ids, ["原始", "水坎", "山艮", "火离"])
    },
    25233: dict(comments={
        18: "原始",
        **{19 + i: f"擎羊{i + 1}灯魂" for i in range(3)}
    }),
    33588: dict(comments={
        1: "兵主逆",
        2: "天斗旋"
    }),
    42423: dict(comments={
        1: "",
        2: "踏斗",
        3: "踏斗12尺"
    }),
    42509: dict(comments={i + 1: f"{i + 1}段" for i in range(2)}),
    42456: dict(comments={i + 1: f"{i + 1}层" for i in range(7)}),
    28815: dict(comments={
        1: "连极阵",
        2: "踏斗连极阵",
        3: "踏斗12尺连极阵"
    }),
25031: dict(comment="焚如")

}
