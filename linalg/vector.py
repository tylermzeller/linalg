from collections import defaultdict
from typing import Dict, Sequence, Union

from linalg.number_types import AbstractNumeric, RealNumeric, RealNumber
from linalg.alg import inner_prod, mat_prod, elmwise_prod, outer_prod

class DimensionError(Exception): pass

class Vector:
    def __init__(self, values: Sequence[AbstractNumeric], is_col: bool=False) -> None:
        self.dim: Dict[int, int] = defaultdict(lambda: 1)
        self.dim[1] = len(values)
        self.values: Sequence[AbstractNumeric] = values
        self.is_col = is_col

    def __repr__(self) -> str:
        return f'<{",".join([str(v) for v in self.values])}>{"T" if self.is_col else ""}'

    def __eq__(self, other) -> bool:
        return (
            self.is_col == other.is_col and
            all([i == j for i, j in zip(self.values, other.values)])
        )

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __add__(self, other) -> 'Vector':
        if not isinstance(other, Vector):
            raise TypeError('Cannot add Vector and {other.__class__}')
        if other.dim[1] != self.dim[1]:
            raise DimensionError(f'Cannot add Vectors with dimension {self.dim[1]} and {other.dim[1]}')
        if self.is_col != other.is_col:
            raise DimensionError(f'Cannot add {"column" if self.is_col else "row"} Vector to {"column" if other.is_col else "row"} Vector')
        return Vector([x + y for x, y in zip(self.values, other.values)], is_col=self.is_col)

    def __sub__(self, other) -> 'Vector':
        return self + (-other)

    def __mul__(self, other: Union['Vector', RealNumeric]) -> 'Vector':
        if isinstance(other, RealNumber):
            return Vector([other * x for x in self.values], is_col=self.is_col)
        if isinstance(other, Vector):
            if self.dim[1] != other.dim[1]:
                raise DimensionError(f'Cannot multiply Vectors with dimension {self.dim[1]} and {other.dim[1]}')
            if self.is_col and not other.is_col:
                return outer_prod(self.values, other.values) # TODO: return a Matrix
            if not self.is_col and other.is_col:
                return inner_prod(self.values, other.values)
            return Vector(elmwise_prod(self.values, other.values), is_col=self.is_col)

    def __neg__(self) -> 'Vector':
        return self * -1

    def copy(self) -> 'Vector':
        return Vector(self.values[:], is_col=self.is_col)

    def to_row(self) -> 'Vector':
        return Vector(self.values[:], is_col=False)

    def to_col(self) -> 'Vector':
        return Vector(self.values[:], is_col=True)
