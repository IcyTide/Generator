BUFFS: dict[int, dict] = {
    9052: {
        "name": "绝刀增伤",
        **{
            **{i + 1: dict(name=f"额外{(i + 1) * 10}怒气") for i in range(4)},
        },
        8: dict(name="吓魂"),
        9: dict(name="嗜血")
    },
    8244: {1: {}},
    8474: {
        -1: dict(comment="DPS"),
        0: dict(comment="Tank")
    },
    31385: {
        1: dict(comment="崩血"),
        2: dict(comment="崩血+登锋")
    }
}
