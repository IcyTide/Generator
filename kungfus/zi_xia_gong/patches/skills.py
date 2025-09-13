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
    **{
        skill_id: dict(comments={4: "30700品"}) for skill_id in [23104, 23107]
    },
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
}
