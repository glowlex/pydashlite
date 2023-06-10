from typing import Iterable, List, TypeVar
from itertools import chain

from .uniq import uniq

T = TypeVar('T')


def union(array: Iterable[T], *others: Iterable[T]) -> List[T]:
    '''
    compares with == statement, suitable for unhashable types\n
    preserves order\n
    returns first unique elements
    >>> union([2, 1, 2], [1, 4])
    [2, 1, 4]
    '''
    return uniq(chain(array, *others))
