SKILLS = {
    12: dict(channel_interval=27),
    32820: {
        1: dict(comment="龙牙/灭"),
        2: dict(comment="振甲"),
    },
    18207: dict(comment="1段"), 18208: dict(comment="2段"),
    431: dict(comment="原始"), 14882: dict(comment="8尺外"),
    701: dict(comment="自身50%血量以下"), 702: dict(comment="自身50%血量以上"),
    24843: {
        **{i + 1: dict(comment=f"蓄力{i + 1}段({delay}帧)") for i, delay in enumerate([0, 12, 23])},
        **{i + 4: dict(comment=f"高血量蓄力{i + 1}段({delay}帧)") for i, delay in enumerate([0, 12, 23])}
    },
    36258: {4: {}},
}
