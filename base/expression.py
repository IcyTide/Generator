import math


def is_number(var):
    if isinstance(var, int):
        return True
    if isinstance(var, float):
        return True
    if isinstance(var, Constant):
        return True
    return False


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

    def __pow__(self, power, modulo=None):
        return Pow(self, power)

    def __rpow__(self, other):
        return Pow(other, self)

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
        if values is None:
            values = {}
        return values.get(self.name, 0)

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
            return operand.operand  # - (-a) = a
        if operand == 0:
            return operand  # -0 = 0
        if isinstance(operand, Constant):
            operand = operand.value
        if isinstance(operand, (int, float)):
            return Constant(-operand)  # - (-a) = a
        return super().__new__(cls).init(operand)

    def __str__(self):
        return f"-{self.operand}"

    def evaluate(self, values=None):
        return -self.operand.evaluate(values)

    def derivative(self, var):
        return -self.operand.derivative(var)


class Int(UnaryOperator):
    def __new__(cls, operand):
        if isinstance(operand, Constant):
            operand = operand.value
        if isinstance(operand, (int, float)):
            return int(operand)
        return super().__new__(cls).init(operand)

    def __str__(self):
        return f"int({self.operand})"

    def evaluate(self, values=None):
        return Int(self.operand.evaluate(values))

    def derivative(self, var):
        return self.operand.derivative(var)


class Ceil(UnaryOperator):
    def __new__(cls, operand):
        if isinstance(operand, Constant):
            operand = operand.value
        if isinstance(operand, (int, float)):
            return math.ceil(operand)
        return super().__new__(cls).init(operand)

    def __str__(self):
        return f"ceil({self.operand})"

    def evaluate(self, values=None):
        return Ceil(self.operand.evaluate(values))

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
    def __new__(cls, left, right: int | float | Expression):
        if left == 0:
            return right  # 0 + a = a
        if right == 0:
            return left  # a + 0 = 0
        if isinstance(left, Constant):
            left = left.value
        if isinstance(right, Constant):
            right = right.value
        if isinstance(right, (int, float)) and right < 0:
            return Sub(left, -right)  # a + (-b) = a - b
        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            return Constant(left + right)
        if isinstance(right, (int, float)):
            if isinstance(left, Add):
                if isinstance(left.left, Constant):
                    return Add(left.left.value + right, left.right)  # (a + b) + c = (a + c) + b
                if isinstance(left.right, Constant):
                    return Add(left.left, left.right.value + right)  # (a + b) + c = a + (b + c)
            if isinstance(left, Sub):
                if isinstance(left.left, Constant):
                    return Add(left.left.value - right, left.right)  # (a - b) + c = (a - c) + b
                if isinstance(left.right, Constant):
                    return Sub(left.left, left.right.value - right)  # (a - b) + c = a - (b - c)
        if isinstance(left, (int, float)):
            if isinstance(right, Add):
                if isinstance(right.left, Constant):
                    return Add(left + right.left.value, right.right)  # a + (b + c) = (a + b) + c
                if isinstance(right.right, Constant):
                    return Add(right.left, left + right.right.value)  # a + (b + c) = b + (a + c)
            if isinstance(right, Sub):
                if isinstance(right.left, Constant):
                    return Sub(left + right.left.value, right.right)  # a + (b - c) = (a + b) - c
                if isinstance(right.right, Constant):
                    return Sub(right.left, right.right.value - left)  # a + (b - c) = b - (c - a)
        return super().__new__(cls).init(left, right)

    def __str__(self):
        return f"{self.left} + {self.right}"

    def evaluate(self, values=None):
        return self.left.evaluate(values) + self.right.evaluate(values)

    def derivative(self, var):
        return self.left.derivative(var) + self.right.derivative(var)


class Sub(BinaryOperator):
    def __new__(cls, left, right: int | float | Expression):
        if left == 0:
            return -right
        if right == 0:  # 0 - a = -a
            return left  # a - 0 = a
        if left == right:
            return Constant(0)  # a - a = 0
        if isinstance(left, Constant):
            left = left.value
        if isinstance(right, Constant):
            right = right.value
        if isinstance(right, (int, float)) and right < 0:
            return Add(left, -right)  # a - (-b) = a + b
        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            return Constant(left - right)
        if isinstance(right, (int, float)):
            if isinstance(left, Add):
                if isinstance(left.left, Constant):
                    return Add(left.left.value - right, left.right)  # (a + b) - c = (a - c) + b
                if isinstance(left.right, Constant):
                    return Add(left.left, left.right.value - right)  # (a + b) - c = (b - c) + a
            if isinstance(left, Sub):
                if isinstance(left.left, Constant):
                    return Sub(left.left.value - right, left.right)  # (a - b) - c = (a - c) - b
                if isinstance(left.right, Constant):
                    return Sub(left.left, left.right.value + right)  # (a - b) - c = a - (b + c)
        if isinstance(left, (int, float)):
            if isinstance(right, Add):
                if isinstance(right.left, Constant):
                    return Sub(left - right.left.value, right.right)  # a - (b + c) = (a - b) - c
                if isinstance(right.right, Constant):
                    return Sub(left - right.right.value, right.left)  # a - (b + c) = (a - c) - b
            if isinstance(right, Sub):
                if isinstance(right.left, Constant):
                    return Add(left - right.left.value, right.right)  # a - (b - c) = (a - b) + c
                if isinstance(right.right, Constant):
                    return Sub(left + right.right.value, right.left)  # a - (b - c) = (a + c) -b
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
            return Constant(0)  # 0 * a = 0; a * 0 = 0
        if left == 1:
            return right  # 1 * a = a
        if right == 1:
            return left  # a * 1 = a
        if isinstance(left, Constant):
            left = left.value
        if isinstance(right, Constant):
            right = right.value
        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            return Constant(left * right)
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
            return Constant(0)  # 0 / a = 0
        if right == 1:
            return left  # a / 1 = a
        if left == right:
            return Constant(1)  # a / a = 1
        if isinstance(left, Constant):
            left = left.value
        if isinstance(right, Constant):
            right = right.value
        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            return Constant(left / right)
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


class Pow(BinaryOperator):
    def __new__(cls, left, right):
        if left == 0:
            return Constant(0)  # 0 ** a = 0
        if left == 1:
            return Constant(1)  # 1 ** a = 1
        if right == 0:
            return Constant(1)  # a ** 0 = 1
        if right == 1:
            return left  # a ** 1 = a
        if isinstance(left, Constant):
            left = left.value
        if isinstance(right, Constant):
            right = right.value
        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            return Constant(left ** right)
        return super().__new__(cls).init(left, right)

    def __str__(self):
        left, right = self.left, self.right
        if isinstance(left, BinaryOperator):
            left = f"({left})"
        if isinstance(right, BinaryOperator):
            right = f"({right})"
        return f"{left} ** {right}"

    def evaluate(self, values=None):
        return self.left.evaluate(values) ** self.right.evaluate(values)

    def derivative(self, var):
        return self.left.derivative(var) * self.right * Pow(self.left, self.right - 1)


class Max(BinaryOperator):
    def __new__(cls, left, right):
        if isinstance(left, Constant):
            left = left.value
        if isinstance(right, Constant):
            right = right.value
        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            return max(left, right)
        return super().__new__(cls).init(left, right)

    def __str__(self):
        return f"max({self.left},{self.right})"

    def evaluate(self, values=None):
        return Max(self.left.evaluate(values), self.right.evaluate(values))

    def derivative(self, var):
        return 0  # Cannot take derivative of max
