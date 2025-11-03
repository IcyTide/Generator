from base.expression import Variable

SKILLS = {
    **{
        skill_id: dict(comment=comment, channel_interval=24)
        for skill_id, comment in zip([16419, 16820, 16822], ["双刀", "大刀", "鞘刀"])
    },
    100999: dict(comment="1段"), 101000: dict(comment="2段"), 101001: dict(comment="3段"), 101050: dict(comment="风车"),
    101002: dict(self_rollback_attributes=[
        ("physical_critical_strike_rate", 1000 * Variable("recipe_16966_1")),
        ("physical_critical_power_rate", 100 * Variable("recipe_16966_1"))
    ]),
    101003: dict(dest_rollback_attributes=[("coming_damage_cof", 512 * Variable("recipe_16969_1"))]),
    101068: dict(dest_rollback_attributes=[("coming_damage_cof", 512 * Variable("recipe_16970_1"))]),
    101006: dict(self_rollback_attributes=[
        ("physical_critical_strike_rate", 2000 * Variable("recipe_16974_1")),
        ("physical_critical_power_rate", 200 * Variable("recipe_16974_1"))
    ]),
    101108: dict(comment="1段"), 101109: dict(comment="2段"), 101110: dict(comment="3段"),
    **{
        skill_id: dict(comment=f"{i + 1}段")
        for i, skill_id in enumerate([101118, 101119, 101120, 101121, 101122, 101123])
    },
    101200: dict(comment="直接伤害"), 101198: dict(comment="后续伤害"),
    101296: dict(
        dest_rollback_attributes=[("coming_damage_cof", 153.6)],
        dest_rollback_skills=[
            100999, 101000, 101001, 101050,
            101003, 101006,
            101108, 101109, 101110,
            101256, 101257, 101258, 101259, 101260
        ]
    ),
    101297: dict(
        dest_rollback_attributes=[("coming_damage_cof", 307.2)],
        dest_rollback_skills=[101002, 101080, 101200, 101198]
    ),
    **{
        skill_id: dict(comment=f"{i + 1}段")
        for i, skill_id in enumerate([101256, 101257, 101258, 101259, 101260])
    },
}
