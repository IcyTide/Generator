TALENTS: list[dict[int, dict]] = [
    {
        6818: dict(dots={6401: dict(skills={6867: {}})}),
        6824: dict(skills={19435: dict(comment="1-2段"), 8491: dict(comment="3段")}),
        14633: dict(skills={18913: {
            1: dict(comment="0-50%蓝量"),
            **{i + 1: dict(comment=f"{(i + 6) * 10}%蓝量") for i in range(5)}
        }}),
        40646: dict(skills={32898: dict(levels=[5])})
    },
    {
        6822: {},
        43059: {},
        42099: {},
        38878: dict(skills={38891: {}})
    },
    {
        15211: {},
        44204: {},
        44205: {},
        6832: dict(buffs={5994: {}})
    },
    {
        15212: {},
        43206: {},
        6830: {},
        6845: {}
    },
    {
        41993: {},
        44282: dict(skills={32898: dict(levels=[6])}),
        40331: dict(skills={40335: {}}),
        37385: dict(skills={37397: {}, 28819: {}})
    },
    {
        44317: {},
        25197: dict(skills={25201: dict(comment="持续"), 25202: dict(comment="触发")}),
        14927: dict(
            dots={32041: dict(skills={42918: {}})},
            skills={43085: dict(comment="1段"), 42917: dict(comment="2段")}
        ),
        28989: dict(skills={28952: {
            12: dict(comment="1段"),
            13: dict(comment="2段"),
            14: dict(comment="3段"),
            15: dict(comment="4段")
        }})
    },
    {
        6337: {},
        21284: {},
        6833: {},
        6810: dict(skills={32898: dict(levels=[3])}),
        6813: {},
        6842: {},
        6834: dict(skills={30300: {}}),
        32725: dict(skills={32898: dict(levels=[2])}),
        26701: dict(skills={41057: {
            1: dict(comment="延迟0帧1段"),
            2: dict(comment="延迟9帧2段"),
            3: dict(comment="延迟12帧3段"),
            4: dict(comment="延迟23帧4段")
        }}),
        32731: dict(skills={36255: dict(comment="持续"), 32770: dict(comment="结算{}秒")}),
        14626: {},
        26702: dict(skills={26703: {}})
    }
]
