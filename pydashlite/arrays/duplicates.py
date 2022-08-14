from typing import Dict, Iterable, List, Optional, TypeVar, Callable, Hashable, Any

from ..tools.no_value import NoValue

V = TypeVar('V')
VH = TypeVar('VH', bound=Hashable)
K = TypeVar('K', bound=Hashable)


def duplicates(array: Iterable[V], iteratee: Optional[Callable[[V], Any]] = None) -> List[V]:
    '''
    returns list containing the last duplicate of each non unique value\n
    compares with == statement, suitable for unhashable types\n
    preserves order
    >>> duplicates([1, 1, 2, 3])
    [1]
    >>> duplicates([1, 2, 2, 1])
    [1, 2]
    >>> duplicates(['A', 'b', 'C', 'a', 'B', 'c', 'C'], lambda x: x.lower())
    ['a', 'B', 'C']
    >>> duplicates([[1], [1], [2], 3])
    [[1]]
    '''
    res: List[V] = []
    if iteratee is None:
        tmp = list(array)
    elif callable(iteratee):
        tmp = [iteratee(x) for x in array]
    else:
        raise ValueError('wrong iteratee')

    array = tuple(array)
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


def duplicatesHash(array: Iterable[VH], iteratee: Optional[Callable[[VH], K]] = None) -> List[VH]:
    '''
    returns list containing the last duplicate of each non unique value\n
    only for hashable types\n
    preserves order
    >>> duplicates([1, 1, 2, 3])
    [1]
    >>> duplicates([1, 2, 2, 1])
    [1, 2]
    >>> duplicates(['A', 'b', 'C', 'a', 'B', 'c'], lambda x: x.lower())
    ['a', 'B', 'c']
    '''
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
