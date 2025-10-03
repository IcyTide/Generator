BUFFS: dict[int, dict] = {
    9052: dict(name="绝刀增伤", comments={
        **{i + 1: f"额外{(i + 1) * 10}怒气" for i in range(4)},
        8: "吓魂",
        9: "嗜血"
    }),
    8244: dict(comments={1: ""}),
    8474: dict(comments={
        16: "DPS", 17: "Tank"
    }),
    31385: dict(comments={
        1: "崩血",
        2: "崩血+登锋"
    })
}
