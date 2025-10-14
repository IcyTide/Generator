BUFFS: dict[int, dict] = {
    375: {
        5: dict(comment="小队"),
        11: dict(comment="自身"),
        12: dict(comment="抱阳"),
        13: dict(comment="归元"),
        14: dict(comment="抱阳+归元")
    },
    1908: {1: {}},
    2757: {
        1: dict(comment="原始"),
        2: dict(comment="若水"),
        3: dict(comment="固本"),
        4: dict(comment="无为"),
        5: dict(comment="无欲")
    },
    30137: {1: {}},
    31729: dict(name="洞渊", comment="{}"),
    9966: dict(name="同尘", comment="{}"),
    **{
        buff_id: dict(name="跬步", comment=comment)
        for buff_id, comment in zip([12550, 12551, 31669], ["四象轮回", "两仪化形", "万世不竭"])
    }
}
