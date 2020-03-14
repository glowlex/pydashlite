from typing import Iterable, List, TypeVar

from itertools import chain

T = TypeVar('T')


def intersection(array: Iterable[T], *others: Iterable[T]) -> List[T]:
    res: List[T] = []
    merged = [array, *others]
    if len(merged) == 1:
        return list(array)
    mn = min([(len(x), i) for i, x in enumerate(merged)], key=lambda x: x[0])
    a = merged.pop(mn[1])
    iters = chain(*merged)
    for v in iters:
        if v in a and v not in res:
            res.append(v)
    return res
