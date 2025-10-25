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
        return Int(self.operand.evaluate(values))

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
            return right
        if right == 0:
            return left
        if isinstance(left, Constant) and isinstance(right, Constant):
            return Constant(left.value + right.value)
        if isinstance(right, (int, float)) and right < 0:
            return Sub(left, -right)
        if isinstance(right, Constant) and right.value < 0:
            return Sub(left, -right.value)
        if isinstance(left, (Add, Sub)) and isinstance(right, (int, float)):
            if isinstance(left.left, Constant):
                return left.__class__(left.left.value + right, left.right)
            if isinstance(left.right, Constant):
                return left.__class__(left.left, left.right.value + right)
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
        if right == 0:
            return left
        if left == right:
            return Constant(0)
        if isinstance(left, Constant) and isinstance(right, Constant):
            return Constant(left.value - right.value)
        if isinstance(right, (int, float)) and right < 0:
            return Add(left, -right)
        if isinstance(right, Constant) and right.value < 0:
            return Add(left, -right.value)
        if isinstance(left, (Add, Sub)) and isinstance(right, (int, float)):
            if isinstance(left.left, Constant):
                return left.__class__(left.left.value - right, left.right)
            if isinstance(left.right, Constant):
                return left.__class__(left.left, left.right.value - right)
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


class Pow(BinaryOperator):
    def __new__(cls, left, right):
        if left == 0:
            return Constant(0)
        if left == 1:
            return Constant(1)
        if right == 0:
            return Constant(1)
        if right == 1:
            return left
        if isinstance(left, Constant) and isinstance(right, Constant):
            return Constant(left.value ** right.value)
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
