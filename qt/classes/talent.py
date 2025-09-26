class Talent:
    def __init__(
            self, skill_id: int,
            dots: dict[int, tuple[list[int], list[int]]] = None,
            buffs: list[int] = None,
            skills: list[int] = None,
            recipes: list[int] = None
    ):
        self.skill_id = skill_id
        self.dots = dots or {}
        self.buffs = buffs or []
        self.skills = skills or []
        self.recipes = recipes or []
