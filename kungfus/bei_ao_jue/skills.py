SKILLS: dict[int, dict[int, dict]] = {
    10464: {
        16820: dict(channel_interval=24, comment="松烟竹雾"),
        16419: dict(channel_interval=24, comment="秀明尘身"),
        16822: dict(channel_interval=24, comment="雪絮金屏")
    },
    16028: {
        16097: dict(comment="松烟竹雾"),
        16774: dict(comment="秀明尘身1段"),
        16775: dict(comment="秀明尘身2段")
    },
    16460: {
        17053: {}
    },
    16599: {
        16599: dict(comment="松烟竹雾"),
        16600: dict(comment="松烟竹雾打断"),
        16631: dict(comment="秀明尘身"),
        16632: dict(comment="秀明尘身打断"),
    },
    16454: {
        17006: dict(levels=[1])
    },
    16601: {
        16758: dict(comment="1段"),
        16759: dict(comment="2段"),
        16760: dict(comment="3段"),
        16382: dict(comment="3段后续")
    },
    16602: {
        20991: {},
        32823: dict(levels=[1])
    },
    16627: {
        skill_id: dict(comment=f"连续命中{i}次") for i, skill_id in
        enumerate([16803, 16802, 16801, 16800, 17043])
    },
    16479: {
        16992: dict(comment="1段"),
        16994: dict(comment="2段"),
        16996: dict(comment="3段")
    },
    42428: {
        42677: {}
    },
    16304: {
        17092: {}
    },
    16870: {
        **{
            skill_id: dict(comment=f"{1 + i % 2}段") for i, skill_id in
            enumerate([16933, 16934, 16935, 16936, 16937, 16938, 16939, 16940, 16941, 16942, 16943, 16944])
        },
        32823: dict(levels=[3])
    },
    16027: {
        **{
            skill_id: dict(comment=f"<{100 - i * 20}血量")
            for i, skill_id in enumerate([16610, 16611, 16612, 16613, 16614])
        },
        32823: dict(levels=[2])
    },
    16085: {
        skill_id: dict(comment=f"<{100 - i * 20}血量")
        for i, skill_id in enumerate([16615, 16616, 16617, 16618, 16619])
    },
    16621: {
        **{
            skill_id: dict(comment=f"<{100 - i * 20}血量")
            for i, skill_id in enumerate([16787, 16788, 16789, 16790, 16791])
        },
        16794: dict(comment="后续")
    }
}
