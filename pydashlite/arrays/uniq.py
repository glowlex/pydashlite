from typing import Callable, Hashable, Iterable, TypeVar, List, Any

T = TypeVar('T')
X = TypeVar('X', bound=Hashable)


def uniq(array: Iterable[T]) -> List[T]:
    res: List[T] = []
    for v in array:
        if v not in res:
            res.append(v)
    return res


def uniqBy(array: Iterable[T], iteratee: Callable[[T], Any]) -> List[T]:
    res: List[T] = []
    keys: List[Any] = []
    for v in array:
        a = iteratee(v)
        if a not in keys:
            keys.append(a)
            res.append(v)
    return res


def uniqHash(array: Iterable[X]) -> List[X]:
    res = {x: 1 for x in array}
    return list(res)


def uniqHashBy(array: Iterable[X], iteratee: Callable[[X], int]) -> List[X]:
    res = {iteratee(x): x for x in array}
    return list(res.values())
