from base.expression import Variable

BUFFS: dict[int, dict] = {
    28355: dict(name="烈日", comment="自身"),
    33107: dict(name="日月连璧", attributes=[("coming_damage_cof", -921.6)],
                skills=[4028, 4029, 4030, 4024, 4025, 4026]),
    31456: dict(comment="常驻"), 6277: dict(comment="背后"),
    1: dict(name="斩杀", comment="<30%血量", attributes=[("coming_damage_cof", 512)], skills=[44463]),
    2: dict(name="净体不畏", attributes=[("coming_damage_cof", 512)], skills=[40088, 40089]),
    12575: {
        "name": "用晦而明",
        1: dict(comment="原始"),
        2: dict(comment="强化")
    },
    4754: {1: {}}
}
