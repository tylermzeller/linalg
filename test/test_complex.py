import pytest
from linalg.number_types import Complex

class TestComplex:
    def test_conjugate(self):
        a = Complex(a=1, b=1)
        a_star = a.conjugate()
        assert a_star == Complex(a=1, b=-1)
        b = a_star.conjugate()
        assert b == a

    def test_add(self):
        a = Complex(a=1, b=1)
        b = Complex(a=1, b=2)
        c = a + b
        assert c == Complex(a=2, b=3)

    def test_mul(self):
        a = Complex(r=1, theta=1)
        b = Complex(r=1, theta=2)
        c = a * b
        assert c == Complex(r=1, theta=3)

    def test_sub(self):
        a = Complex(a=1, b=1)
        b = Complex(a=1, b=2)
        c = a - b
        assert c == Complex(a=0, b=-1)

    def test_div(self):
        a = Complex(r=1, theta=1)
        b = Complex(r=1, theta=2)
        c = a / b
        assert c == Complex(r=1, theta=-1)
