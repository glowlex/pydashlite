from typing import Callable, Hashable, Iterable, TypeVar, List, Any

T = TypeVar('T')
X = TypeVar('X', bound=Hashable)


def uniq(array: Iterable[T]) -> List[T]:
    '''
    compares with == statement, suitable for unhashable types\n
    preserves order
    >>> uniq([1, 2, 2, [3]])
    [1, 2, [3]]
    '''
    res: List[T] = []
    for v in array:
        if v not in res:
            res.append(v)
    return res


def uniqBy(array: Iterable[T], iteratee: Callable[[T], Any]) -> List[T]:
    '''
    compares with == statement, suitable for unhashable types\n
    preserves order
    >>> uniqBy([1, 2, 2, [3]], lambda x: x)
    [1, 2, [3]]
    '''
    res: List[T] = []
    keys: List[Any] = []
    for v in array:
        a = iteratee(v)
        if a not in keys:
            keys.append(a)
            res.append(v)
    return res


def uniqHash(array: Iterable[X]) -> List[X]:
    '''
    only for hashable types\n
    preserves order
    >>> uniqHash([1, 2, 2, 3])
    [1, 2, 3]
    '''
    res = {x: 1 for x in array}
    return list(res)


def uniqHashBy(array: Iterable[X], iteratee: Callable[[X], int]) -> List[X]:
    '''
    only for hashable types\n
    preserves order
    >>> uniqHashBy([[1], [2], [2], [3]], lambda x: x[0])
    [[1], [2], [3]]
    '''
    res = {iteratee(x): x for x in array}
    return list(res.values())
