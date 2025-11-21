SKILLS = {
    19055: dict(comment="{}"),
    32816: {
        1: dict(comment="阳性/降灵尊"),
        2: dict(comment="阴性"),
        3: dict(comment="阳性+用晦而明"),
        4: dict(comment="阴性+用晦而明"),
        5: dict(comment="崇光斩恶")
    },
    35065: {1: {}},
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([4024, 4025, 4026])},
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([4028, 4029, 4030])},
    4480: {
        29: dict(comment="原始"),
        58: dict(comment="背后")
    },
    37336: {
        **{i + 1: dict(comment=f"{i + 1}段") for i in range(3)},
        **{i + 4: dict(comment=f"{i + 1}段高血量") for i in range(3)}
    },
    41763: {1: {}},
    41765: dict(comment="{}秒"),
    26916: {
        1: dict(comment="净世破魔击日+净世破魔击月"),
        2: dict(comment="净世破魔击日+明赦尊谕/生死劫月"),
        3: dict(comment="明赦尊谕/生死劫日+净世破魔击月"),
        4: dict(comment="明赦尊谕/生死劫日+明赦尊谕/生死劫月")
    },
    26708: dict(comment="{}"),
    40209: {
        **{i + 1: dict(comment=f"{15 * i}最大气血") for i in range(10)},
        **{i + 11: dict(comment=f"{15 * i}最大气血(范围外)") for i in range(10)},
    },
    34510: dict(comment="命中{level-1}次"),
    **{
        skill_id: dict(comment="{}层影子")
        for skill_id in [34353, 34354, 34355, 34356, 34359, 34361, 34362, 34363]
    }
}
