BUFFS: dict[int, dict] = {
    17885: {5: dict(comment="主T")}, 29938: {5: dict(comment="副T")},
    9052: {
        "name": "绝刀增伤",
        **{
            **{i + 1: dict(name=f"额外{(i + 1) * 10}怒气") for i in range(4)},
        },
    },
    8249: {
        22: dict(comment=""),
        50: dict(comment="炼狱")
    },
    8271: dict(comment="150"), 17772: dict(name="寒甲", comment="15000"),
    18222: {4: {}}
}
