from decimal import Decimal, getcontext
from typing import Optional, Union, Tuple
from math import asin, cos, sin, sqrt

# For type hints
RealNumeric = Union[int, float, Decimal]
# For type checking (isinstance)
RealNumber: Tuple[RealNumeric] = (int, float, Decimal)

class Complex:
    def __init__(self, a: Optional[RealNumeric]=None, b: Optional[RealNumeric]=None, r: Optional[RealNumeric]=None,
                 theta: Optional[RealNumeric]=None) -> None:
        if a is not None and b is not None:
            self.a = a
            self.b = b
            self.__calc_polar()
        elif r is not None and theta is not None:
            self.r = r
            self.theta = theta
            self.__calc_cart()
        else:
            raise ValueError('Must set a and b or r and theta.')


    def __str__(self) -> str:
        r = self.r.quantize(Decimal(10) ** -10).normalize()
        theta = self.theta.quantize(Decimal(10) ** -10).normalize()
        a = self.a.quantize(Decimal(10) ** -10).normalize()
        b = self.b.quantize(Decimal(10) ** -10).normalize()
        return f'{a} + i{b}, {r}e**(i{theta})'

    def __repr__(self) -> str:
        return str(self)

    def __setattr__(self, name, value) -> None:
        if name in ['a', 'b', 'r', 'theta'] and isinstance(value, RealNumber):
            if isinstance(value, RealNumber):
                self.__dict__[name] = Decimal(value)
            else:
                AttributeError(f'Invalid value for attr {name}: {value}')
        else:
            raise AttributeError(f'Unsupported attr {name}')

    def __eq__(self, other) -> bool:
        Complex.__restrict_ops(other)
        return (self.a == other.a and
                self.b == other.b)

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __add__(self, other) -> 'Complex':
        Complex.__restrict_ops(other)
        return Complex(a=self.a + other.a, b=self.b + other.b)

    def __sub__(self, other) -> 'Complex':
        Complex.__restrict_ops(other)
        return Complex(a=self.a - other.a, b=self.b - other.b)

    def __mul__(self, other) -> 'Complex':
        Complex.__restrict_ops(other)
        return Complex(r=self.r * other.r, theta=self.theta + other.theta)

    def __truediv__(self, other) -> 'Complex':
        Complex.__restrict_ops(other)
        if other.a == 0 and other.b == 0:
            raise ArithmeticError('Cannot by a zero Complex instance')
        return Complex(r=self.r / other.r, theta=self.theta - other.theta)

    @classmethod
    def __restrict_ops(cls, other) -> None:
        if not isinstance(other, cls):
            raise ValueError(f'Complex ops must be between Complex instances')

    @classmethod
    def from_cart(cls, a: RealNumeric, b: RealNumeric)  -> 'Complex':
        return cls(a=a, b=b)

    @classmethod
    def from_polar(cls, r: RealNumeric, theta: RealNumeric) -> 'Complex':
        return cls(r=r, theta=theta)

    def __calc_polar(self) -> None:
        self.r = sqrt(self.a**2 + self.b**2)
        self.theta = asin(self.b / self.r)

    def __calc_cart(self) -> None:
        self.a = self.r * Decimal(cos(self.theta))
        self.b = self.r * Decimal(sin(self.theta))


    def copy(self) -> 'Complex':
        return Complex(r=self.r, theta=self.theta)

    def conjugate(self) -> 'Complex':
        return Complex(a=self.a, b=self.b * -1)

# For type hints
AbstractNumeric = Union[RealNumeric, Complex]
# For type checking (isinstance)
AbstractNumber: Tuple[AbstractNumeric] = RealNumber + (Complex,)
