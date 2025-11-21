SKILLS = {
    19055: dict(comment="{}"),
    32816: {
        1: dict(comment="阳性"),
        2: dict(comment="阴性"),
        6: dict(comment="无量妙境阳性"),
        7: dict(comment="无量妙境阴性")
    },
    35065: {2: {}},
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([4024, 4025, 4026])},
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([4028, 4029, 4030])},
    26708: dict(comment="{}"),
}
