SKILLS = {
    **{
        skill_id: dict(comment=f"{i + 1}豆")
        for i, skill_id in enumerate([327, 328, 329, 330, 331, 461, 462, 463, 464, 465])
    },
    **{
        skill_id: dict(comment=f"{i + 1}豆")
        for i, skill_id in enumerate([3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448])
    },
    18121: dict(channel_interval=21),
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([18649, 18650, 18651, 18652, 18653])},
    22014: dict(comments={
        1: "原始",
        2: "万物"
    }),
    32813: dict(
        comments={
            1: "两仪化形6-7豆",
            2: "两仪化形8豆",
            3: "两仪化形9-10豆",
            4: "万世不竭",
            5: "两仪化形11-12豆",
            6: "两仪化形13-15豆",
            7: "两仪化形16豆"
        }
    ),
    40158: dict(
        comments={i + 1: f"{11 + i}豆" for i in range(6)}
    ),
    28590: dict(
        comments={
            1: "连续命中",
            2: "首次"
        }
    ),
    21860: dict(comment="自化"),
    36102: dict(comments={
        1: "原始",
        2: "70%血量以上"
    })
}
