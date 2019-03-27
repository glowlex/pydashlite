from typing import Union, Sequence, Iterable, List, Callable, Any, Hashable
import itertools
import copy
import re

from .tools import is_iterable


def at(array:Iterable, indexes:list) -> list:
    return [v for i, v in enumerate(array) if i in indexes]


def uniq(array:Iterable) -> list:
    res = []
    # try:
    #     res = list(set(array))
    # except:
    for v in array:
        if v not in res:
            res.append(v)
    return res


def union(array:Iterable, *others:Iterable) -> list:
    return uniq(itertools.chain(array, *others))


def flatten(array:Iterable) -> list:
    return list(itertools.chain(*[x if is_iterable(x) and not isinstance(x, str) else [x] for x in array]))


def head(iterable:Iterable, default=None) -> Any:
    try:
        r = next(iter(iterable))
    except:
        return default
    else:
        return r


def intersection(array:Iterable, *others:Iterable) -> list:
    res = []
    merged = [array, *others]
    merged.sort(key=lambda x:len(x))
    iters = itertools.chain(*merged[1:])
    for v in iters:
        if v in merged[0] and v not in res:
            res.append(v)
    return res
    #return uniq(res)


def concat(*arrays) -> list:
    return flatten(arrays)


def sum_by(array:list, iteratee:Callable[[Any], int]=None, start:int=0):
    if iteratee is None:
        iteratee = lambda x:x
    return sum([iteratee(y) for y in array], start)


#collection, arrays, objects
def group_by(array:list, iteratee:Union[Callable[[Any], Hashable], Any]=None) -> dict:
    res = {}
    if iteratee is None:
        iteratee = lambda x: x
    elif not callable(iteratee):
        it = iteratee
        iteratee = lambda x: get(x, it)

    for v in array:
        elems = res.setdefault(iteratee(v), [])
        elems.append(v)
    return res