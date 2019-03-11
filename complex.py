from decimal import Decimal

class Complex:
    def __init__(self, a, b):
        self.a = Decimal(a)
        self.b = Decimal(b)

    def __eq__(self, other):
        Complex.__restrict_ops(other)
        return (self.a == other.a and
                self.b == other.b)

    def __add__(self, other):
        Complex.__restrict_ops(other)
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        Complex.__restrict_ops(other)
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        Complex.__restrict_ops(other)
        # TODO: can do this with only 3 multiplications http://mathworld.wolfram.com/ComplexMultiplication.html
        return Complex((self.a * other.a) - (self.b * other.b),
                      ((self.a * other.b) + (self.b * other.a)))

    def __div__(self, other):
        Complex.__restrict_ops(other)
        if other.a == 0 and other.b == 0:
            raise ArithmeticError('Cannot by a zero Complex instance')
        return Complex(1/(other.a**2 + other.b**2), 0) *
               Complex((self.a * other.a) + (self.b * other.b),
                       (self.b * other.a) - (self.a * other.b))

    @classmethod
    def __restrict_ops(cls, other):
        if not isinstance(other, cls):
            raise ValueError(f'{cls} ops must be between {cls} instances')

    def conjugate(self):
        return Complex(self.a, self.b * -1)
