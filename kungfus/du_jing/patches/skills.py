SKILLS = {
    18590: dict(comment="灵蛊"),
    32818: dict(comments={
        1: "荒息",
        5: "虫魄"
    }),
    **{
        skill_id: dict(comment=comment)
        for skill_id, comment in zip([2470, 2471, 2472, 2473, 2474], ["圣蝎", "玉蟾", "灵蛇", "风蜈", "天蛛"])
    },
    25044: dict(comment="持续"), 30918: dict(comment="结算", comments={i + 1: f"{i}层增伤" for i in range(5)}),
    30090: dict(comment="嗜蛊"),
    25019: dict(comments={1: ""}),
    **{
        skill_id: dict(comment=comment, comments={i + 1: f"{i + 1}跳" for i in range(max_level)})
        for skill_id, comment, max_level in zip(
            [37357, 37358, 37361, 37362, 37363, 37364, 37365, 37366],
            ["", "", "", "", "固灵", "不僵", "不僵+固灵", ""],
            [12, 11, 11, 11, 11, 14, 11, 14]
        )
    },
    37363: dict(comment="固灵"),
    37364: dict(comment="不僵"),
    37365: dict(comment="不僵+固灵"),
    37358: dict(comment="腾影"),
    **{skill_id: dict(comments={i + 1: f"{i + 1}层" for i in range(6)}) for skill_id in [42295, 42296]},
    36044: dict(comments={i + 1: f"{i * 4}尺" for i in range(99)})
}
