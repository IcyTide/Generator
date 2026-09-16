from base.expression import Expression


class Damage:
    name: str

    total_damage: int | Expression
    total_count: int = 0

    def __init__(self, name: str):
        self.name = name
        self.total_damage = 0

    def add_damage(self, damage: int | Expression, count: float):
        self.total_damage += damage * count
        self.total_count += count