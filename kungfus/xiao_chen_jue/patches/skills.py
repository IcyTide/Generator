from base.expression import Variable


def get_comments():
    levels = [1, 5, 6, 7, 8, 9, 12]
    combos = [0, 3, 8, 12, 15, 18, 20]
    comments = {}
    for level, combo in zip(levels, combos):
        for i in range(4):
            k = level + i
            if k not in comments:
                comments[k] = []
            comments[k].append(f"{i + 1}段({combo}连击)")
    return {k: dict(comment="/".join(v)) for k, v in comments.items()}


SKILLS = {
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([6377, 6378])},
    **{
        skill_id: dict(comment=f"蓄力1段(0帧)伤害{i + 1}段({delay}帧)")
        for i, (skill_id, delay) in enumerate(zip([13503, 6382], [1, 5]))
    },
    **{
        skill_id: dict(comment=f"蓄力2段(12帧)伤害{i + 1}段({delay}帧)")
        for i, (skill_id, delay) in enumerate(zip([13504, 6384, 6385, 6386], [1, 4, 8, 11]))
    },
    **{
        skill_id: dict(comment=f"蓄力3段(24帧)伤害{i + 1}段({delay}帧)")
        for i, (skill_id, delay) in enumerate(zip([13505, 6388, 6389, 6390, 6391], [0, 4, 7, 11, 15]))
    },
    **{
        skill_id: dict(comment=f"{i + 1}段({delay}帧)")
        for i, (skill_id, delay) in enumerate(zip([6379, 6380], [4, 6]))
    },
    **{
        skill_id: dict(comment=f"{i + 1}段({delay}帧)")
        for i, (skill_id, delay) in enumerate(zip([6353, 6351, 6352, 6354], [1, 3, 6, 10]))
    },
    **{
        skill_id: dict(comment=f"{i + 1}段({delay}帧)")
        for i, (skill_id, delay) in enumerate(zip([6358, 6359, 13526], [1, 2, 3]))
    },
    **{
        skill_id: dict(comment=f"{i + 1}段({delay}帧)")
        for i, (skill_id, delay) in enumerate(zip([6362, 6363, 13528], [1, 2, 3]))
    },
    **{
        skill_id: dict(comment=f"{i + 1}段")
        for i, skill_id in enumerate([6369, 6370, 6371, 6372, 6373])
    },
    6374: {1: dict(comment="6段")},
    **{
        skill_id: dict(comment=f"{i + 1}段")
        for i, skill_id in enumerate([6366, 6367, 6368])
    },
    **{
        skill_id: dict(comment=f"{i + 1}段")
        for i, skill_id in enumerate([6355, 6356, 6357])
    },

    **{
        skill_id: dict(comment=f"{i + 1}段({delay}帧)")
        for i, (skill_id, delay) in enumerate(zip([6582, 13512, 6584, 6585, ], [13, 16, 19, 22]))
    },
    13527: dict(comment="1帧"),
    13529: dict(comment="1帧"),
    32898: {
        1: dict(comment="原始"),
        2: dict(comment="酩酊"),
        3: {},
        4: {},
        5: {}
    },
    **{
        skill_id: dict(
            comment=comment, dest_rollback_attributes=[("coming_damage_cof", 308 * Variable("belong_6824"))]
        ) for skill_id, comment in zip([19435, 8491], ["1-2段", "3段"])
    },
    14633: dict(comment="{}0%内力"),
    41057: {
        i + 1: dict(comment=f"{i + 1}段({delay}帧)") for i, delay in enumerate([0, 9, 12, 23])
    },
    37397: {1: {}},
    40299: dict(comment="{}目标"),
    25201: dict(comment="持续"), 25202: dict(comment="触发"),
    14927: dict(comment="1段"), 14928: dict(comment="2段"),
    28952: get_comments(),
    36255: dict(comment="持续"),
    32770: dict(comment="结算{}秒")
}
