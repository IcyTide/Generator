SKILLS = {
    **{
        skill_id: dict(comment=comment, channel_interval=24)
        for skill_id, comment in zip([16419, 16820, 16822], ["双刀", "大刀", "鞘刀"])
    },
    32823: {
        1: dict(comment="破釜沉舟"),
        2: dict(comment="刀啸风吟"),
        3: dict(comment="擒龙六斩"),
        4: dict(comment="化蛟"),
    },
    16097: dict(comment="双刀"), 16774: dict(comment="大刀1段"), 16775: dict(comment="大刀2段"),
    16599: dict(comment="双刀"), 16600: dict(comment="双刀打断"),
    16631: dict(comment="大刀"), 16632: dict(comment="大刀打断"),
    17006: {
        1: dict(comment="原始"),
        2: dict(comment="疏狂")
    },
    16758: dict(comment="1段"), 16759: dict(comment="2段"), 16760: dict(comment="3段"), 16382: dict(comment="风车"),
    16992: dict(comment="1段"), 16994: dict(comment="2段"), 16996: dict(comment="3段"),
    **{
        skill_id: dict(comment=f"{1 + i % 2}段") for i, skill_id in
        enumerate([16933, 16934, 16935, 16936, 16937, 16938, 16939, 16940, 16941, 16942, 16943, 16944])
    },
    **{
        skill_id: dict(comment=f"{100 - i * 20}血量以下")
        for skill_ids in [
            [16610, 16611, 16612, 16613, 16614],
            [16615, 16616, 16617, 16618, 16619],
            [16787, 16788, 16789, 16790, 16791]
        ]
        for i, skill_id in enumerate(skill_ids)
    },
    16794: dict(comment="后续伤害"),
    40210: dict(comment="一段"),
    40188: dict(comment="三段"),
    38537: {3: {}},
    36311: {i + 1: dict(comment=f"蓄力{i + 1}段({delay}帧)") for i, delay in enumerate([0, 8, 16, 21])},
    25262: {
        1: dict(comment="一段"),
        2: dict(comment="二段"),
        4: dict(comment="击落")
    },
    **{
        skill_id: dict(comment=f"阳关{i}层") for i, skill_id in
        enumerate([16803, 16802, 16801, 16800, 17043, 19423, 19424])
    }
}
