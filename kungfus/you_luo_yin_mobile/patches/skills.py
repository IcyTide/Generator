from ....base.expression import Int, Variable

SKILLS = {
    102401: dict(dest_rollback_attributes=[(
        "coming_damage_cof", 256 * Int(Variable("buff_71590_1") / 6) * Variable("recipe_17527_1")
    )]),
    102443: dict(dest_rollback_attributes=[(
        "coming_damage_cof", 153.6 * Variable("buff_71590_1")
    )]),
    102413: dict(dest_rollback_attributes=[(
        "coming_damage_cof", 153.6 * Variable("buff_71590_1")
    )]),
    102422: dict(comment="秘章")
}
