from typing import Iterable, List, TypeVar

from itertools import chain

T = TypeVar('T')


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
        return list(array)
    mn = min([(len(x), i) for i, x in enumerate(merged)], key=lambda x: x[0])
    a = merged.pop(mn[1])
    iters = chain(*merged)
    for v in iters:
        if v in a and v not in res:
            res.append(v)
    return res
