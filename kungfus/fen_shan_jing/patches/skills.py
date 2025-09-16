SKILLS = {
    13039: dict(channel_interval=24),
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([13044, 13244, 13060])},
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([13106, 13160, 13161])},
    32745: dict(comments={
        1: "铁骨衣斩刀",
        2: "分山劲斩刀",
        3: "铁骨衣绝刀",
        7: "惊涌斩刀",
        9: "阵云结晦"
    }),
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
    })
}
