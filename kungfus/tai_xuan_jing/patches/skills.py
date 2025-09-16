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
    })
}
