SKILLS = {
    19055: dict(comments={}),
    32816: dict(comments={
        1: "阳性/降灵尊",
        2: "阴性",
        3: "阳性+用晦而明",
        4: "阴性+用晦而明",
        5: "崇光斩恶"
    }),
    35065: dict(comments={
        1: "DPS",
        2: "Tank"
    }),
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([4024, 4025, 4026])},
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([4028, 4029, 4030])},
    4480: dict(comments={
        29: "原始",
        58: "背后"
    }),
    37336: dict(comments={
        **{i + 1: f"{i + 1}段" for i in range(3)},
        **{i + 4: f"{i + 1}段高血量" for i in range(3)}
    }),
    41763: dict(comments={1: ""}),
    41765: dict(comments={
        i + 1: f"{i + 1}秒" for i in range(120)
    }),
    26916: dict(comments={
        1: "净世破魔击日+净世破魔击月",
        2: "净世破魔击日+明赦尊谕/生死劫月",
        3: "明赦尊谕/生死劫日+净世破魔击月",
        4: "明赦尊谕/生死劫日+明赦尊谕/生死劫月"
    }),
    26708: dict(comments={}),
    40209: dict(comments={
        **{i + 1: f"{15 * i}最大气血" for i in range(10)},
        **{i + 11: f"{15 * i}最大气血(范围外)" for i in range(10)},
    }),
    34510: dict(comments={
        i + 1: f"命中{i}次" for i in range(11)
    }),
    **{
        skill_id: dict(comments={i + 1: f"第{i + 1}次" for i in range(6)})
        for skill_id in [34353, 34354, 34355, 34356, 34359, 34361, 34362, 34363]
    }
}
