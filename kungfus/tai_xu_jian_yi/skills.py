SKILLS: dict[int, dict[int, dict]] = {
    10015: {
        18121: dict(channel_interval=21)
    },
    362: {
        21979: dict(levels=[2])
    },
    363: {
        21979: dict(levels=[3])
    },
    364: {
        17689: dict(comment="1段"),
        17690: dict(comment="2段"),
        32814: dict(levels=[1])
    },
    311: {
        14975: {}
    },
    365: {
        **{
            skill_id: dict(comment=f"{i + 1}豆")
            for i, skill_id in enumerate([386, 387, 388, 389, 390, 391, 392, 393, 394])
        },
        32814: {
            2: dict(comment="6-8豆"),
            3: dict(comment="9-10豆")
        }
    },
    2699: {
        4954: {
            1: dict(comment="100%血量"),
            2: dict(comment="50%血量以下"),
            3: dict(comment="20%血量以下")
        }
    },
    588: {
        38534: {}
    },
    2690: {
        21431: {},
        18528: dict(levels=[2])
    }
}
