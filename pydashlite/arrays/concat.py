from typing import Iterable, List, TypeVar

from .flatten import flatten

T = TypeVar('T')


def concat(*arrays: Iterable[T]) -> List[T]:
    '''
    >>> concat([1, 2], [3, 4], [5])
    [1, 2, 3, 4, 5]
    '''
    return flatten(arrays)
