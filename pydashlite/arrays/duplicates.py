from typing import Dict, Iterable, List, TypeVar, Callable, Hashable, Any

from ..tools.no_value import NoValue

V = TypeVar('V')
VH = TypeVar('VH', bound=Hashable)
K = TypeVar('K', bound=Hashable)


def duplicates(array: Iterable[V], iteratee: Callable[[V], Any] = None) -> List[V]:
    res: List[V] = []
    if iteratee is None:
        tmp = list(array)
    elif callable(iteratee):
        tmp = [iteratee(x) for x in array]
    else:
        raise ValueError('wrong iteratee')

    array = list(array)
    for i, v in enumerate(tmp):
        if v is NoValue:
            continue
        dups = []
        for ix, x in enumerate(tmp[i+1:]):
            if v == x:
                dups.append(array[i+1+ix])
                tmp[i+1+ix] = NoValue
        if dups:
            res.append(dups[-1])
    return res


def duplicatesHash(array: Iterable[VH], iteratee: Callable[[VH], K] = None) -> List[VH]:
    res: Dict[Hashable, List[VH]] = {}
    tmp: Dict[Hashable, int] = {}
    if iteratee is None:
        for v in array:
            if v not in tmp:
                tmp[v] = 1
                res[v] = []
            else:
                res[v].append(v)
    elif callable(iteratee):
        for v in array:
            k = iteratee(v)
            if k not in tmp:
                tmp[k] = 1
                res[k] = []
            else:
                res[k].append(v)
    return [x[-1] for x in res.values() if x]
