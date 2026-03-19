from base.constant import BINARY_SCALE
from base.expression import Variable

SKILLS = {
    38093: {
        "comment": "{level-1}点任脉能量",
        1: dict(comment="劈风令"),
        25: dict(comment="神门")
    },
    38083: dict(dest_rollback_attributes=[(
        "coming_damage_cof",
        307.2 * Variable("buff_33157")
    )]),
    38438: dict(comment="{level-1}点任脉能量", dest_rollback_attributes=[(
        "coming_damage_cof",
        (1.4 * (1 + 0.03 * Variable("buff_29205")) * (1 + 0.3 * Variable("buff_33157")) - 1) * BINARY_SCALE
    )]),
    38085: dict(comment="{}层绝脉"),
    37804: dict(comment="{}"),
    37816: dict(comment="弹射{level-1}次"),
    38477: dict(comment="1段"), 38886: dict(comment="2段"),
    38982: dict(comment="1段"), 38983: dict(comment="2段"),
    38016: dict(comment="1段"),
    **{
        skill_id: {
            1: dict(comment=f"{i + 2}段"),
            2: dict(comment=f"滃从{i + 2}段"),
        }
        for i, skill_id in enumerate([38075, 38076, 38077])
    },
    38501: dict(dest_rollback_attributes=[("coming_damage_cof", 358)], dest_rollback_skills=[37804])
}
