from typing import Iterable, List, TypeVar
from itertools import chain

from .uniq import uniq

T = TypeVar('T')


def union(array: Iterable[T], *others: Iterable[T]) -> List[T]:
    return uniq(chain(array, *others))
