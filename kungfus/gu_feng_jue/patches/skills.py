SKILLS = {
    **{
        skill_id: dict(comment=comment, channel_interval=24)
        for skill_id, comment in zip([32974, 32975], ["单持", "双持"])
    },
    32167: dict(comment="原始"), 32348: dict(comment="额外"),
    32178: {3: {}},
    32510: {
        1: dict(comment="原始"),
        **{i + 1: dict(comment=f"斩颓{i + 1}层破绽") for i in range(1, 6)}
    },
    40828: dict(comment="击破破绽"),
    **{skill_id: dict(comment=f"{i + 1}层流血") for i, skill_id in enumerate([32372, 32371, 32370, 32369])},
    32235: dict(comment="原始"),
    **{skill_id: dict(comment=f"{i + 1}层破绽") for i, skill_id in enumerate([32236, 33237, 33238, 33239])},
    32766: {
        1: dict(comment="原始"),
        2: dict(comment="伏瀑")
    },
    **{skill_id: dict(comment=f"{i + 5}层破绽") for i, skill_id in enumerate([32891, 32892])},
    34724: dict(comment="{}层流血"),
    36118: {1: {}},
    32591: {
        1: dict(comment="初始"),
        2: dict(comment="引爆")
    },
    32616: dict(comment="单持"), 33163: dict(comment="双持"),
    38645: {3: {}},

}
