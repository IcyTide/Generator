BUFFS: dict[int, dict] = {
    31782: {i + 1: dict(
        attributes=[("coming_damage_cof", damage_cof)],
        skills=[16933, 16934, 16935, 16936, 16937, 16938, 16939, 16940, 16941, 16942, 16943, 16944]
    ) for i, damage_cof in enumerate([153.6, 204.8])},
    11221: dict(name="化蛟", comment="递增{}次"),
    11222: dict(name="沧雪", comment="递增{}次"),
    19499: dict(name="砺锋"),
    11456: {1: {}},
}
