from typing import Iterable, Union

from linalg.number_types import AbstractNumeric, AbstractNumber

def mat_prod(a: Iterable, b: Iterable) -> Iterable:
    return [[inner_prod(row, col) for col in b] for row in a]

def outer_prod(a: Iterable, b: Iterable) -> Iterable:
    return mat_prod(a, b)

def inner_prod(a: Union[AbstractNumeric, Iterable],
               b: Union[AbstractNumeric, Iterable]) -> AbstractNumeric:
    if isinstance(a, AbstractNumber) and isinstance(b, AbstractNumber):
        return a * b
    return sum(elmwise_prod(a, b))

def elmwise_prod(a: Iterable, b: Iterable) -> Iterable:
    return [x * y for x, y in zip(a, b)]
