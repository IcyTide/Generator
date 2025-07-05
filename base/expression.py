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

    def __pow__(self, other):
        return Pow(self, other)

    def __rpow__(self, other):
        return Pow(other, self)

    def __neg__(self):
        return Neg(self)

    @property
    def terms(self):
        return {}

    @property
    def simplify(self):
        return sum(v * k for k, v in self.terms.items())

    def evaluate(self, values=None):
        raise NotImplementedError("evaluate must be implemented by subclasses")

    def derivative(self, var):
        raise NotImplementedError("derivative must be implemented by subclasses")


class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    @property
    def terms(self):
        return {self: 1}

    def evaluate(self, values=None):
        if values is None or self.name not in values:
            raise ValueError(f"Value for variable '{self.name}' not provided.")
        return values[self.name]

    def derivative(self, var):
        return Constant(1) if self == var else Constant(0)


class Constant(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return other == self.value

    @property
    def terms(self):
        return {1: self.value}

    def evaluate(self, values=None):
        return self.value

    def derivative(self, var):
        return Constant(0)


class UnaryOperator(Expression):
    def __init__(self, operand):
        self.operand = operand if isinstance(operand, Expression) else Constant(operand)


class Neg(UnaryOperator):
    def __new__(cls, operand):
        if isinstance(operand, Neg):
            return operand.operand
        if operand == 0:
            return operand
        return super().__new__(cls, operand)

    def __repr__(self):
        return f"-{self.operand}"

    @property
    def terms(self):
        return {k: -v for k, v in self.operand.terms.items()}

    def evaluate(self, values=None):
        return -self.operand.evaluate(values)

    def derivative(self, var):
        return -self.operand.derivative(var)


class BinaryOperator(Expression):
    def __init__(self, left, right):
        self.left = left if isinstance(left, Expression) else Constant(left)
        self.right = right if isinstance(right, Expression) else Constant(right)


class Add(BinaryOperator):
    def __new__(cls, left, right):
        if left == 0:
            return right
        if right == 0:
            return left
        if isinstance(left, Constant) and isinstance(right, Constant):
            return Constant(left.value + right.value)
        return super().__new__(cls)

    def __repr__(self):
        return f"({self.left} + {self.right})"

    @property
    def terms(self):
        terms = {**self.left.terms}
        for k, v in self.right.terms.items():
            if k not in terms:
                terms[k] = 0
            terms[k] += v
        return terms

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
        return super().__new__(cls)

    def __repr__(self):
        return f"({self.left} - {self.right})"

    @property
    def terms(self):
        terms = {**self.left.terms}
        for k, v in self.right.terms.items():
            if k not in terms:
                terms[k] = 0
            terms[k] -= v
        return terms

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
        return super().__new__(cls)
    def __repr__(self):
        return f"({self.left} * {self.right})"

    @property
    def terms(self):
        terms = {}
        for left_k, left_v in self.left.terms.items():
            for right_k, right_v in self.right.terms.items():
                k, v = left_k * right_k, left_v * right_v
                if k not in terms:
                    terms[k] = 0
                terms[k] += v
        return terms

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
        return super().__new__(cls)

    def __repr__(self):
        return f"({self.left} / {self.right})"

    @property
    def terms(self):
        terms = {}
        for left_k, left_v in self.left.terms.items():
            for right_k, right_v in self.right.terms.items():
                k, v = left_k / right_k, left_v / right_v
                if k not in terms:
                    terms[k] = 0
                terms[k] += v
        return terms

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
        return super().__new__(cls)

    def __repr__(self):
        return f"({self.left} ** {self.right})"

    def evaluate(self, values=None):
        return self.left.evaluate(values) ** self.right.evaluate(values)

    def derivative(self, var):
        return self.right * self.left.derivative(var) * self.left ** (self.right - 1)


if __name__ == '__main__':
    x = Variable('x')
    y = Variable('y')

    f = x * 2 + 3 * y + 4 * x * y + 5 * (x + y) * y # + 6 * (x + y) * x
    print(f)
    print(f.simplify)