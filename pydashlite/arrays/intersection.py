from typing import Dict, Hashable, Iterable, List, Sequence, Tuple, TypeVar

from .uniq import uniq, uniqHash
from .flatten import flatten

T = TypeVar('T')
X = TypeVar('X', bound=Hashable)


def intersection(array: Sequence[T], *others: Sequence[T]) -> List[T]:
    '''
    compares with == statement, suitable for unhashable types\n
    preserves order
    >>> intersection([1, 2, 3], [1, 2], [2])
    [2]
    >>> intersection([3, 1], [1, 2, 3])
    [1, 3]
    >>> intersection([[1], 2, 3], [[1], [2]])
    [[1]]
    '''
    res: Dict[int, Tuple[T, Tuple[int, int]]] = {}
    chunks = [array, *others]
    if len(chunks) == 1:
        return list(array)
    mn = min([(len(x), i) for i, x in enumerate(chunks)], key=lambda x: x[0])[1]
    a = chunks[mn]= uniq(chunks[mn])
    for ix, x in enumerate(a):
        checks = 0
        for ic, c in enumerate(chunks):
            if c is a:
                if ix not in res:
                    res[ix] = (x, (ic, ix))
                checks += 1
                continue
            for iv, v in enumerate(c):
                if x == v:
                    if ix not in res:
                        res[ix] = (v, (ic, iv))
                    checks += 1
                    break
            else:
                break
        if checks != len(chunks) and ix in res:
            del res[ix]
    t = sorted(res.values(), key=lambda x: x[1])
    return [x[0] for x in t]
