from kungfus import first


class Kungfu:
    def __init__(self, kungfu_id, name, kungfu):
        self.kungfu_id = kungfu_id
        self.name = name

        self.buffs = kungfu.BUFFS
        self.skills = kungfu.SKILLS
        self.dots = kungfu.DOTS
        self.talents = kungfu.TALENTS


SUPPORT_KUNGFUS: dict[int, Kungfu] = {
    1: Kungfu(1, "first", first),
}
