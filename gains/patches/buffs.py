BUFFS = {
    # Gears
    30748: dict(levels=[1, 2, 3], comment="{alias}"),
    30749: dict(levels=[1, 2, 3, 4, 5, 6], comment="{alias}"),
    30770: dict(levels=[1, 2, 3, 4, 5, 6], comment="{alias}"),
    30948: dict(levels=[1, 2, 3], comment="{alias}"),
    30742: dict(levels=[1, 2, 3], comment="{alias}"),
    30743: dict(levels=[1, 2, 3, 4, 5, 6, 7, 8], comment="{alias}"),
    30946: dict(levels=[1, 2, 3], comment="{alias}"),
    30755: dict(levels=[1, 3, 5], comment="{alias}"),
    30756: dict(levels=[1, 3, 5], comment="{alias}"),
    30757: dict(levels=[1, 3, 5], comment="{alias}"),
    30950: dict(levels=[1, 3, 5], comment="{alias}"),
    29519: dict(levels=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], comment="{alias}"),
    29524: dict(levels=[4, 5, 6, 7, 8], comment="{alias}"),
    29526: dict(levels=[4, 5, 6, 7, 8], comment="{alias}"),
    29528: dict(levels=[4, 5, 6, 7, 8], comment="{alias}"),
    29529: dict(levels=[4, 5, 6, 7, 8], comment="{alias}"),
    29536: dict(levels=[4, 5, 6, 7, 8], comment="{alias}"),
    29537: dict(levels=[4, 5, 6, 7, 8], comment="{alias}"),
    29608: dict(comment="{alias}"),
    4761: {-i: dict(comment="{alias}") for i in range(3 * 4)},
    29268: {-i: dict(comment="{alias}") for i in range(3 * 8)},
    15455: {1: dict(comment="1%"), 2: dict(comment="5%")},
    15436: dict(levels=[15, 16, 17]),
    # Consumables
    **{buff_id: dict(comment="{}") for buff_id in [29274, 29276, 29284, 29285, 29288, 29289]},
    17365: {-i: {} for i in range(5)},
    # Teams
    23573: dict(name="泠风解怀"),
    6363: {1: {}},
    661: dict(on_target=1),
    12717: dict(on_target=1),
    3465: dict(on_target=1),
    566: dict(on_target=1),
    378: {7: {}},
    375: {5: {}},
    29354: {1: {}},
    4246: dict(comment="{}"),
    4058: {1: dict(on_target=1)},
    8248: dict(comment="{}", on_target=1),
    70021: {1: dict(comment="《龙吟·悟》奇卷"), 2: dict(comment="战锋·悟")},
    70167: {2: dict(comment="无往不利·悟")},
    # formations
    **{
        buff_id: {6: {}} for buff_id in [
            919, 938, 947, 934, 930, 952, 1924, 2512, 3306, 3307, 4579, 6342, 10954, 14074, 15957, 18335,
            21035, 24578, 27236, 29481, 31962
        ]
    },
    18336: dict(comment="{}")
}
