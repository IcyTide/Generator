from base.expression import Variable

SKILLS = {
    22126: dict(channel_interval=24),
    **{skill_id: dict(comment=f"{i + 1}段") for i, skill_id in enumerate([22170, 22550, 22551])},
    22298: dict(comment="链接"),
    22328: dict(comment="原始"), 22329: dict(comment="双持"),
    22489: dict(comment="原始"), 22490: dict(comment="双持"),
    22610: dict(comment="原始"), 22611: dict(comment="双持"),
    32822: {
        1: dict(comment="原始"),
        2: dict(comment="双持")
    },
    24165: {
        1: dict(comment="1段"), 
        2: dict(comment="2段"), 
        3: dict(comment="4段")
    },
    24166: dict(comment="3段"),
    25311: dict(comment="1段"), 25312: dict(comment="2段"),
    **{
        skill_id: dict(dest_rollback_attributes=[("coming_damage_cof", 205 * Variable("talent_42128"))])
        for skill_id in [22489, 22490]
    }
}
