BUFFS: dict[int, dict] = {
    375: dict(
        comments={
            5: "小队",
            11: "自身",
            12: "抱阳",
            13: "归元",
            14: "抱阳+归元"
        }
    ),
    1908: dict(comments={1: ""}),
    2757: dict(
        comments={
            1: "原始",
            2: "若水",
            3: "固本",
            4: "无为",
            5: "无欲"
        }
    ),
    30137: dict(comments={1: ""}),
    31729: dict(name="洞渊"),
    9966: dict(name="同尘"),
    **{
        buff_id: dict(name="", comment=comment)
        for buff_id, comment in zip([12550, 12551, 31669], ["四象轮回", "两仪化形", "万世不竭"])
    },
    31701: dict(skills=[3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448, 40158])
}
