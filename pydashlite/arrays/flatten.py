from typing import Iterable, TypeVar, List, Union

from ..tools import isIterable

V = TypeVar('V')


def flatten(array: Iterable[Union[V, Iterable[V]]]) -> List[V]:
    """
    equivalent flattenDepth(arr, depth=1)
    >>> flatten([[1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> flatten([[1, 2], [3, [4]], [5], 6])
    [1, 2, 3, [4], 5, 6]
    """
    return flattenDepth(array)


def flattenDeep(array: Iterable[Union[V, Iterable[V]]]) -> List[V]:
    '''
    equivalent flattenDepth(arr, depth=0)
    >>> flattenDeep([[1, 2], [[3], [[4]]], 5])
    [1, 2, 3, 4, 5]
    '''
    return flattenDepth(array, 0)


def flattenDepth(array: Iterable[Union[V, Iterable[V]]], depth=1) -> List[V]:
    '''
    >>> flattenDepth([[1, 2], [3, [4]], [5], 6], depth=1)
    [1, 2, 3, [4], 5, 6]
    >>> flattenDepth([[1, 2], [3, [4]], [5]], depth=2)
    [1, 2, 3, 4, 5]
    >>> flattenDeep([[1, 2], [[3], [[4]]], 5], depth=0)
    [1, 2, 3, 4, 5]
    depth=0 processes values as long as they are iterables and not strings
    '''
    res = []
    folded = False
    for x in array:
        if isIterable(x) and not isinstance(x, str):
            res.extend(x)
            folded = True
        else:
            res.append(x)
    if depth != 1 and folded:
        return flattenDepth(res, depth - 1)
    else:
        return res
