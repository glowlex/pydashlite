from typing import Callable, Iterable, TypeVar

T = TypeVar('T')
Num = TypeVar('Num', int, float)


def sumBy(array: Iterable[T], iteratee: Callable[[T], Num] = None, start: Num = 0) -> Num:
    if iteratee is None:
        return sum([y for y in array], start)
    return sum([iteratee(y) for y in array], start)
