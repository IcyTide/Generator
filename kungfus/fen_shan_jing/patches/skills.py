SKILLS = {
    13039: dict(channel_interval=24),
    32745: dict(comments={
        1: "铁骨衣斩刀",
        2: "分山劲斩刀",
        3: "铁骨衣绝刀",
        7: "惊涌斩刀",
        9: "阵云结晦"
    }),
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([13044, 13244, 13060])},
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([13106, 13160, 13161])},
    38889: dict(comments={
        1: "分山劲绝刀",
        **{i + 1: f"额外{(i + 1) * 10}怒气绝刀" for i in range(5)}
    }),
    38890: dict(comments={
        1: "惊涌绝刀",
        **{i + 1: f"额外{(i + 1) * 10}怒气绝刀" for i in range(5)}
    }),
    38971: dict(comments={
        1: "原始盾舞",
        2: "惊涌盾舞"
    }),
    41738: dict(comment="崩血+登锋"),
    36065: dict(comments={1: ""}),
    13143: dict(comment="流血"), 13144: dict(comment="原始"),
    41737: dict(comment="登锋"),
    **{skill_id: dict(comment=f"{i + 1}段", comments={1: ""}) for i, skill_id in enumerate([30925, 30926, 30857])}
}
