from ....base.expression import Expression


class Damage:
    name: str

    formula: int | Expression
    count: int = 0

    def __init__(self, name: str):
        self.name = name
        self.formula = 0
