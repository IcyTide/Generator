SKILLS = {
    **{
        skill_id: dict(comment=comment, channel_interval=24)
        for skill_id, comment in zip([16419, 16820, 16822], ["双刀", "大刀", "鞘刀"])
    },
    32823: dict(comments={
        1: "破釜沉舟",
        2: "刀啸风吟",
        3: "擒龙六斩",
        4: "化蛟",
        5: "临江"
    }),
    16097: dict(comment="双刀"),
    **{skill_id: dict(comment=f"大刀{i + 1}段") for i, skill_id in enumerate([16774, 16775])},
    16599: dict(comment="双刀"), 16600: dict(comment="双刀打断"),
    16631: dict(comment="大刀"), 16632: dict(comment="大刀打断"),
    17006: dict(comments={
        1: "原始",
        2: "疏狂"
    }),
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([16758, 16759, 16760])},
    16382: dict(comment="风车"),
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([16992, 16994, 16996])},
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
}
