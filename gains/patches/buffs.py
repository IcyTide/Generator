BUFFS = {
    # Gears
    29524: dict(comment="{}"),
    29526: dict(comment="{}"),
    30748: dict(comment="{}"),
    30749: dict(comment="{}"),
    30743: dict(comment="{}"),
    30742: dict(comment="{}"),
    29519: dict(comment="{}"),
    29537: dict(comment="{}"),
    29536: dict(comment="{}"),
    30950: dict(comment="{}"),
    30757: dict(comment="{}"),
    30755: dict(comment="{}"),
    30756: dict(comment="{}"),
    29529: dict(comment="{}"),
    29528: dict(comment="{}"),
    29608: dict(comment="{}"),
    4761: {i - 7: {} for i in range(8)},
    29268: {i - 15: {} for i in range(16)},
    15455: dict(comment="{}"),
    15436: dict(comment="{}"),
    # Consumables
    **{buff_id: dict(comment="{}") for buff_id in [29274, 29276, 29284, 29285, 29288, 29289]},
    17365: {i - 4: {} for i in range(5)},
    # Teams
    23573: dict(name="泠风解怀"),
    6363: {1: {}},
    661: dict(on_target=1),
    12717: dict(on_target=1),
    3465: dict(on_target=1),
    566: dict(on_target=1),
    378: {7: {}},
    375: {5: {}},
    29354: dict(comment="{}"),
    4246: dict(comment="{}"),
    4058: {1: dict(on_target=1)},
    8248: dict(on_target=1),
    70021: {1: dict(comment="奇卷"), 2: dict(comment="战锋")},
    # formations
    **{
        buff_id: {6: {}} for buff_id in [
            919, 938, 947, 934, 930, 952, 1924, 2512, 3306, 3307, 4579, 6342, 10954, 14074, 15957, 18335,
            21035, 24578, 27236, 29481, 31962
        ]
    },
    18336: dict(comment="{}")
}
