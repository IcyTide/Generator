from ....base.expression import Variable

SKILLS = {
    18121: dict(channel_interval=21),
    **{skill_id: dict(comment=f"{i + 1}把") for i, skill_id in enumerate([101613, 101614, 101615, 101616, 101617])},
    101665: dict(dest_rollback_attributes=[("coming_damage_cof", 307.2 * Variable("recipe_16679_1"))]),
    100558: dict(
        dest_rollback_attributes=[("coming_damage_cof", 512)],
        dest_rollback_skills=[101613, 101614, 101615, 101616, 101617]
    )
}
