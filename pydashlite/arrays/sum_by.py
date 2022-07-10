from typing import Callable, Iterable, Optional, TypeVar

T = TypeVar('T')
Num = TypeVar('Num', int, float)


def sumBy(array: Iterable[T], iteratee: Optional[Callable[[T], Num]] = None, start: Num = 0) -> Num:
    if iteratee is None:
        return sum(array, start=start)
    return sum([iteratee(y) for y in array], start=start)
