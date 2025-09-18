BUFFS: dict[int, dict] = {
    21168: dict(name="苍棘缚地增伤", comments={
        1: "温性",
        2: "灵荆"
    }),
    20718: dict(name="炮阳"),
    21856: dict(name="荆障"),
    21610: dict(name="茎蹊", comments={}),
    20707: dict(name="滞眠", comments={
        i + 2: f"递增{i + 1}次" for i in range(4)
    }),
    20699: dict(name="养荣")
}
