BUFFS: dict[int, dict] = {
    7659: {
        1: dict(comment="千里无痕"),
        2: dict(comment="原始")
    },
    17103: dict(name="追命无声"),
    12663: dict(comment="摧心"),
    **{
        buff_id: dict(name=f"蹑景", comment=f"{i + 1}层")
        for i, buff_id in enumerate([28225, 28226, 28227])
    },
    18036: {2: {}},
    10169: dict(name="空山独立"),
    3223: {3: {}},
    31825: dict(name="追锋断念"),
    8210: dict(comment="聚精凝神")
}
