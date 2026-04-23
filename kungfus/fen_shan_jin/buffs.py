BUFFS: dict[int, dict[int, dict]] = {
    13055: {
        9052: {
            **dict(name="绝刀增伤"),
            **{
                **{i + 1: dict(name=f"额外{(i + 1) * 10}怒气") for i in range(4)},
            },
        }
    },
    13040: {
        8244: dict(levels=[1])
    }

}
