TALENTS: list[dict[int, dict]] = [
    {
        13090: {},
        41740: dict(skills={41739: {}}, dots={31385: dict(levels=[1], skills={41738: {}})}),
        18354: {},
        30769: dict(
            skills={
                skill_id: dict(comment=f"{i + 1}段", levels=[1])
                for i, skill_id in enumerate([30925, 30926, 30857])
            }
        )
    },
    {
        37559: {},
        46014: {},
        38969: {},
        13418: dict(skills={21431: {}})
    },
    {
        36205: dict(buffs={27161: {}}),
        41982: {},
        13152: dict(skills={13286: {}}),
        13153: dict(skills={13144: {}, 13143: dict(comment="流血")})
    },
    {
        46682: dict(
            skills={
                skill_id: dict(comment=f"{i + 1}段100怒气", levels=[2])
                for i, skill_id in enumerate([30925, 30926, 30857])
            }
        ),
        13086: {},
        13111: {},
        13304: dict(buffs={33520: {}})
    },
    {
        21281: dict(buffs={17176: {}, 9052: {
            **dict(name="绝刀增伤"),
            **{
                **{i + 1: dict(name=f"额外{(i + 1) * 10}怒气") for i in range(4)},
            },
        }}),
        13073: {},
        37558: dict(dots={31385: dict(levels=[2], skills={41737: {}})}),
        20984: dict(buffs={14319: {}})
    },
    {
        46020: {},
        15196: dict(buffs={31536: {}}),
        25213: dict(skills={25215: {}}),
        29066: {}
    },
    {
        37239: dict(skills={37253: {}}),
        13414: {},
        25212: {},
        37240: {},
        45804: dict(buffs={17056: dict(skill_damage_cof=307.2, skills={13099: {}})}),
        21282: {},
        41834: dict(skills={43458: {}}),
        14838: {},
        22897: dict(buffs={14309: {}}),
        46079: {},
        13395: {},
        34540: {}
    }
]
