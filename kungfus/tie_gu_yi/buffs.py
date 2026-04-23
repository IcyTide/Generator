BUFFS: dict[int, dict[int, dict]] = {
    10389: {
        17885: dict(levels=[5], comment="主T"),
        29938: dict(levels=[5], comment="副T"),
    },
    13055: {
        9052: {
            **dict(name="绝刀增伤"),
            **{
                **{i + 1: dict(name=f"额外{(i + 1) * 10}怒气") for i in range(4)},
            },
        }
    },
    13391: {
        8499: {}
    }
}
