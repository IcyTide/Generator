SKILLS = {
    13039: dict(channel_interval=24),
    32745: {
        1: dict(comment="斩刀"),
        3: dict(comment="绝刀")
    },
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([13044, 13244, 13060])},
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([13106, 13160, 13161])},
    38889: {
        i + 1: dict(comment=f"额外{(i + 1) * 10}怒气绝刀") for i in range(5)
    },
    38971: {
        1: dict(comment="原始盾舞")
    },
    25208: dict(comment="冲锋"), 25205: dict(comment="终点"),
    13308: dict(comment="闪刀割裂"), 20989: dict(comment="闪刀割裂+炼狱"),
    29185: dict(comment="斩刀割裂+炼狱"), 29186: dict(comment="斩刀割裂"), 29187: dict(comment="斩刀炼狱")
}
