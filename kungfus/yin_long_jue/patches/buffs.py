BUFFS: dict[int, dict] = {
    16596: dict(name="崔嵬鬼步"),
    **{
        buff_id: dict(name=f"百节", comment=f"{i + 1}层")
        for i, buff_id in enumerate([15927, 15928, 15929])
    },
    15896: dict(name="飞琼"),
    21588: dict(name="孤路", comments={i + 1: f"{i + 1}次递增" for i in range(10)})

}
