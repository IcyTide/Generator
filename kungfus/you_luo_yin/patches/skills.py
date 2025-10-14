from base.expression import Variable

SKILLS = {
    42021: dict(comment="{level-1}层缠绞(5帧-10帧-15帧)"),
    42084: {1: {}},
    42265: dict(dest_rollback_attributes=[("coming_damage_cof", 205 * Variable("talent_42128"))]),
    41486: dict(comment="递增{level-1}跳"),
    41994: {1: {}},
    42098: dict(comment="{level-1}层增伤"),
    42260: dict(comment="{}跳"),
    42267: dict(comment="{level-1}层缠绞"),
    42335: dict(comment="{level-1}根丝线"),
    42033: {1: dict(comment="持续")}, 42247: {1: dict(comment="终结")}
}
