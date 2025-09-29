from base.expression import Variable

SKILLS = {
    42021: dict(comment="5帧-10帧-15帧", comments={
        i + 1: f"{i}层缠绞" for i in range(20)
    }),
    42084: dict(comments={1: ""}),
    42265: dict(dest_rollback_attributes=[("coming_damage_cof", 205 * Variable("talent_42128"))]),
    41486: dict(comments={
        i + 1: f"递增{i}跳"
        for i in range(40)
    }),
    41994: dict(comments={1: ""}),
    42098: dict(comments={
        i + 1: f"{i}层增伤" for i in range(5)
    }),
    42260: dict(comments={
        i + 1: f"{i + 1}跳" for i in range(3)
    }),
    42267: dict(comments={
        **{i + 1: f"{i}层缠绞" for i in range(6)}
    }),
    42335: dict(comments={
        i + 1: f"{i}根丝线" for i in range(5)
    }),
    42033: dict(comments={1: "持续"}),
    42247: dict(comments={1: "终结"})
}
