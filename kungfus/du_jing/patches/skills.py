SKILLS = {
    32818: {
        1: dict(comment="荒息"),
        5: dict(comment="虫魄")
    },
    18590: dict(comment="灵蛊"),
    **{
        skill_id: dict(comment=comment)
        for skill_id, comment in zip([2470, 2471, 2472, 2473, 2474], ["圣蝎", "玉蟾", "灵蛇", "风蜈", "天蛛"])
    },
    25044: dict(comment="持续"), 30918: dict(comment="结算{level-1}层增伤"),
    30090: dict(comment="嗜蛊"),
    25019: {1: {}},
    # **{
    #     skill_id: dict(comment=prefix + "({}跳)")
    #     for skill_id, prefix in zip(
    #         [37357, 37358, 37361, 37362, 37363, 37364, 37365, 37366],
    #         ["", "", "", "", "固灵", "不僵", "不僵+固灵", ""]
    #     )
    # },
    37363: dict(comment="固灵"),
    37364: dict(comment="不僵"),
    37365: dict(comment="不僵+固灵"),
    37358: dict(comment="腾影"),
    **{skill_id: dict(comment="{}层") for skill_id in [42295, 42296]},
    36044: dict(comment="{(level-1)*4}尺")
}
