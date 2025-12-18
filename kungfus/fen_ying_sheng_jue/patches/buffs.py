from ....base.expression import Ceil, Variable

BUFFS: dict[int, dict] = {
    28355: dict(name="烈日", comment="自身"),
    28142: dict(name="无往不复", comment="自身"),
    31456: dict(comment="常驻"), 6277: dict(comment="背后"),
    30644: {
        "name": "净体不畏",
        1: dict(comment="烈日斩"),
        2: dict(comment="银月斩")
    },
    4754: {1: {}},
    25716: {
        1: dict(
            name="明赦尊谕缩放",
            attributes=[(
                "global_damage_factor",
                (-1 << 20) * (1 - 0.84 * Variable("buff_key"))
            )],
            skills=[19055, 35065, 34985]
        )
    },
    12575: {
        "name": "用晦而明",
        1: dict(comment="原始"),
        2: dict(comment="强化")
    },
    25758: dict(name="明光恒照", comment="月"), 25759: dict(name="明光恒照", comment="日")
}
