SKILLS = {
    3480: dict(comment="橙武特效"),
    3401: dict(comments={1: "原始", **{i + 1: f"激射{i}层" for i in range(1, 31)}}),
    3404: dict(comments={1: "鬼斧弹药", **{i + 1: f"鬼斧弹药激射{i}层" for i in range(1, 31)}}),
    3819: dict(comments={
        1: "原始",
        2: "非侠士激射",
        3: "侠士激射"
    }),
    3824: dict(comments={
        1: "鬼斧弹药",
        2: "鬼斧弹药非侠士激射",
        3: "鬼斧弹药侠士激射"
    })
}
