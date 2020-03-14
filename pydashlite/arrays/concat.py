from typing import Iterable, List, TypeVar

from .flatten import flatten

T = TypeVar('T')


def concat(*arrays: Iterable[T]) -> List[T]:
    return flatten(arrays)
