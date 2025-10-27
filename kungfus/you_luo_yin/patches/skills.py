SKILLS = {
    42021: dict(comment="{level-1}层缠绞(5帧-10帧-15帧)"),
    42084: {1: {}},
    41486: dict(comment="递增{level-1}跳"),
    41994: {1: {}},
    42098: {1: {}},
    42115: dict(dest_rollback_attributes=[("coming_damage_cof", 1024)], dest_rollback_skills=[42098]),
    42260: dict(comment="{}跳"),
    42267: dict(comment="{level-1}层缠绞"),
    42128: dict(dest_rollback_attributes=[("coming_damage_cof", 205)], dest_rollback_skills=[42265]),
    42335: dict(comment="{level-1}根丝线"),
    42033: {1: dict(comment="持续")}, 42247: {1: dict(comment="终结")},
    42976: {i + 1: dict(comment=f"{energy}点心络") for i, energy in enumerate([20, 30, 40])}
}
