from typing import Iterable, TypeVar, List, Union

from ..tools import isIterable

V = TypeVar('V')


def flatten(array: Iterable[Union[V, Iterable[V]]]) -> List[V]:
    return flattenDepth(array)


def flattenDeep(array: Iterable[Union[V, Iterable[V]]]) -> List[V]:
    return flattenDepth(array, 0)


def flattenDepth(array: Iterable[Union[V, Iterable[V]]], depth=1) -> List[V]:
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
