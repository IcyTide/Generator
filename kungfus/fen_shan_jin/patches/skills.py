SKILLS = {
    13039: dict(channel_interval=24),
    32745: {
        2: dict(comment="斩刀"),
        7: dict(comment="惊涌斩刀"),
        9: dict(comment="阵云结晦")
    },
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([13044, 13244, 13060])},
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([13106, 13160, 13161])},
    38889: {
        i + 1: dict(comment=f"额外{(i + 1) * 10}怒气绝刀") for i in range(5)
    },
    38890: {
        i + 1: dict(comment=f"额外{(i + 1) * 10}怒气惊涌绝刀") for i in range(5)
    },
    38971: {
        1: dict(comment="原始盾舞"),
        2: dict(comment="惊涌盾舞")
    },
    36065: {1: {}},
    13143: dict(comment="流血"), 13144: dict(comment="原始"),
    41737: dict(comment="登锋"), 41738: dict(comment="崩血+登锋"),
    **{skill_id: {1: dict(comment=f"{i + 1}段")} for i, skill_id in enumerate([30925, 30926, 30857])}
}
