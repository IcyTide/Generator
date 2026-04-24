GAINS: dict[int, dict] = {
    10438: dict(buffs={10100: {}}),
    10179: dict(buffs={18428: {}, 2563: {}}),
    10067: dict(buffs={buff_id: dict(comment="{}") for buff_id in [29274, 29276, 29284, 29285]}),
    10071: dict(buffs={buff_id: dict(comment="{}") for buff_id in [29288, 29289]}),
    23768: dict(buffs={
        **{buff_id: {} for buff_id in [27784, 27785, 27786, 27787, 27788, 27792]},
        **{buff_id: {} for buff_id in [17349, 17352, 17355, 17358, 17361]},
        17365: dict(levels=[56, 57, 58, 59, 60])
    })
}
