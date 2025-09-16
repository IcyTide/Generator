SKILLS = {
    38093: dict(comments={
        **{i + 1: f"{i}点任脉能量" for i in range(51)},
        1: "0点任脉能量/劈风令",
        25: "24点任脉能量/神门"
    }),
    38438: dict(comments={
        **{i + 1: f"{i}点任脉能量" for i in range(51)},
    }),
    37804: dict(comments={}),
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([38016, 38075, 38076, 38077])}
}
