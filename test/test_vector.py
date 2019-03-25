import pytest
from linalg.vector import Vector

class TestVector:
    def test_add(self):
        a = Vector([1,2,3])
        b = Vector([2,4,6])
        c = a + b
        assert c == Vector([3,6,9])

    def test_sub(self):
        a = Vector([1,2,3])
        b = Vector([2,4,6])
        c = a - b
        assert c == Vector([-1,-2,-3])

    def test_mul_scalar(self):
        a = Vector([1,2,3])
        b = a * 2
        assert b == Vector([2,4,6])

    def test_neg(self):
        a = Vector([1,2,3])
        assert -a == Vector([-1,-2,-3])
