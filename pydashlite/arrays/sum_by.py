from typing import Callable, Iterable, Optional, TypeVar

T = TypeVar('T')
Num = TypeVar('Num', int, float)


def sumBy(array: Iterable[T], iteratee: Optional[Callable[[T], Num]] = None, start: Num = 0) -> Num:
    '''
    analog build-in sum, but with iteratee param
    >>> sumBy([{'a': 1}, {'a': 2}, {'a': 3}], lambda x: x['a'])
    6
    >>> sumBy([1, 2, 3])
    6
    '''
    if iteratee is None:
        return sum(array, start=start)
    return sum([iteratee(y) for y in array], start=start)
