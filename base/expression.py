class Expression:

    def __add__(self, other):
        return Add(self, other)

    def __radd__(self, other):
        return Add(other, self)

    def __sub__(self, other):
        return Sub(self, other)

    def __rsub__(self, other):
        return Sub(other, self)

    def __mul__(self, other):
        return Mul(self, other)

    def __rmul__(self, other):
        return Mul(other, self)

    def __truediv__(self, other):
        return Div(self, other)

    def __rtruediv__(self, other):
        return Div(other, self)

    def __neg__(self):
        return Neg(self)

    def __eq__(self, other):
        return str(other) == str(self)

    def evaluate(self, values=None):
        raise NotImplementedError("evaluate must be implemented by subclasses")

    def derivative(self, var):
        raise NotImplementedError("derivative must be implemented by subclasses")

    @property
    def terms(self):
        return set()


class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def evaluate(self, values=None):
        if values is None or self.name not in values:
            raise ValueError(f"Value for variable '{self.name}' not provided.")
        return values[self.name]

    def derivative(self, var):
        return Constant(1) if self == var else Constant(0)

    @property
    def terms(self):
        return {self.name}

class Constant(Expression):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return other == self.value

    def evaluate(self, values=None):
        return self.value

    def derivative(self, var):
        return Constant(0)

    def __bool__(self):
        return bool(self.value)


class UnaryOperator(Expression):
    operand: Expression

    def init(self, operand):
        self.operand = operand if isinstance(operand, Expression) else Constant(operand)
        return self

    @property
    def terms(self):
        return self.operand.terms


class Neg(UnaryOperator):
    def __new__(cls, operand):
        if isinstance(operand, Neg):
            return operand.operand
        if operand == 0:
            return operand
        if isinstance(operand, Constant):
            return Constant(-operand.value)
        return super().__new__(cls).init(operand)

    def __str__(self):
        return f"-{self.operand}"

    def evaluate(self, values=None):
        return -self.operand.evaluate(values)

    def derivative(self, var):
        return -self.operand.derivative(var)


class Int(UnaryOperator):
    def __new__(cls, operand):
        if isinstance(operand, (int, float)):
            return int(operand)
        if isinstance(operand, Constant):
            return Constant(int(operand.value))
        return super().__new__(cls).init(operand)

    def __str__(self):
        return f"int({self.operand})"

    def evaluate(self, values=None):
        return int(self.operand.evaluate(values))

    def derivative(self, var):
        return self.operand.derivative(var)


class BinaryOperator(Expression):
    left: Expression
    right: Expression

    def init(self, left, right):
        self.left = left if isinstance(left, Expression) else Constant(left)
        self.right = right if isinstance(right, Expression) else Constant(right)
        return self

    @property
    def terms(self):
        return self.left.terms | self.right.terms


class Add(BinaryOperator):
    def __new__(cls, left, right):
        if left == 0:
            return right
        if right == 0:
            return left
        if isinstance(left, Constant) and isinstance(right, Constant):
            return Constant(left.value + right.value)
        if isinstance(right, (int, float)) and right < 0:
            return Sub(left, -right)
        if isinstance(right, Constant) and right.value < 0:
            return Sub(left, -right.value)
        return super().__new__(cls).init(left, right)

    def __str__(self):
        return f"{self.left} + {self.right}"

    def evaluate(self, values=None):
        return self.left.evaluate(values) + self.right.evaluate(values)

    def derivative(self, var):
        return self.left.derivative(var) + self.right.derivative(var)


class Sub(BinaryOperator):
    def __new__(cls, left, right):
        if left == 0:
            return -right
        if right == 0:
            return left
        if left == right:
            return Constant(0)
        if isinstance(left, Constant) and isinstance(right, Constant):
            return Constant(left.value - right.value)
        if isinstance(right, Constant) and right.value < 0:
            return Add(left, -right.value)
        return super().__new__(cls).init(left, right)

    def __str__(self):
        return f"{self.left} - {self.right}"

    def evaluate(self, values=None):
        return self.left.evaluate(values) - self.right.evaluate(values)

    def derivative(self, var):
        return self.left.derivative(var) - self.right.derivative(var)


class Mul(BinaryOperator):
    def __new__(cls, left, right):
        if left == 0 or right == 0:
            return Constant(0)
        if left == 1:
            return right
        if right == 1:
            return left
        if isinstance(left, Constant) and isinstance(right, Constant):
            return Constant(left.value * right.value)
        if isinstance(left, Neg) and isinstance(right, Neg):
            left, right = left.operand, right.operand
        return super().__new__(cls).init(left, right)

    def __str__(self):
        left, right = self.left, self.right
        if isinstance(left, (Add, Sub)):
            left = f"({left})"
        if isinstance(right, (Add, Sub)):
            right = f"({right})"
        return f"{left} * {right}"

    def evaluate(self, values=None):
        return self.left.evaluate(values) * self.right.evaluate(values)

    def derivative(self, var):
        return self.left.derivative(var) * self.right + self.left * self.right.derivative(var)


class Div(BinaryOperator):
    def __new__(cls, left, right):
        if left == 0:
            return Constant(0)
        if right == 1:
            return left
        if left == right:
            return Constant(1)
        if isinstance(left, Constant) and isinstance(right, Constant):
            return Constant(left.value / right.value)
        if isinstance(left, Neg) and isinstance(right, Neg):
            left, right = left.operand, right.operand
        return super().__new__(cls).init(left, right)

    def __str__(self):
        left, right = self.left, self.right
        if isinstance(left, (Add, Sub)):
            left = f"({left})"
        if isinstance(right, BinaryOperator):
            right = f"({right})"
        return f"{left} / {right}"

    def evaluate(self, values=None):
        right = self.right.evaluate(values)
        if right == 0:
            raise ZeroDivisionError("Division by zero in expression.")
        return self.left.evaluate(values) / right

    def derivative(self, var):
        numerator = self.left.derivative(var) * self.right - self.left * self.right.derivative(var)
        denominator = self.right * self.right
        return numerator / denominator


def get_variables(formula: str) -> dict[str, Variable | type[UnaryOperator]]:
    variable = ""
    variables = {}

    for c in formula:
        if c.isalpha() or c == "_":
            variable += c
        elif variable:
            if c.isnumeric():
                variable += c
            else:
                variables[variable] = Variable(variable)
                variable = ""
    variables["int"] = Int
    return variables


def parse_expr(formula: str):
    variables = get_variables(formula)
    expr = eval(formula, variables)
    return expr

if __name__ == '__main__':
    x = Variable('x')
    y = Variable('y')
    z = Variable('z')
    r = Variable('_1334_1')

    f = -z + Int(x * (1 + y)) - Int(x * (1 + y + 0.5)) + r * x

    #f = "int(int(int(int(int(int(int(int(int(int(70 + rand * 10) + int(int((solar_attack_power_base + int(int(spunk_base * (1 + spunk_gain)) * 0.181)) * (1 + (solar_attack_power_gain + 246 * _3223_1 + 246 * _3224_1) / 1024)) * 5.535337500000001)) * (1 + magical_damage_addition / 1024)) * (1 + move_state_damage_addition / 1024)) * (1 + int(int((solar_overcome_base + int(int(spunk_base * (1 + spunk_gain)) * 0.3)) * (1 + solar_overcome_gain / 1024)) / 225957.6 * 1024) / 1024)) * (1 - int(int(int(solar_shield_base * (1 + solar_shield_gain / 1024)) * (1 - all_shield_ignore / 1024)) / (int(int(solar_shield_base * (1 + solar_shield_gain / 1024)) * (1 - all_shield_ignore / 1024)) + 6.364 * (1155 * target_level - 130350)) * 1024) / 1024)) * (target_level - 130) * 0.05) * (1 + int((int(strain_base * (1 + strain_gain / 1024)) / 133333.2 + strain_rate / 1024) * 1024) / 1024)) * (1 + pve_addition / 1024)) * (1 + solar_damage_cof / 1024))"

    print(f)
    print(f.terms)
    g = parse_expr(str(f))
    print(g)
