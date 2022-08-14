from typing import Union, Iterable, List, Callable, Any, Hashable, Dict, TypeVar
from ..collections import get

V = TypeVar('V')
K = TypeVar('K', bound=Hashable)
Y = TypeVar('Y', bound=Hashable)


def groupListBy(arr: Iterable[V], iteratee: Union[Callable[[V], Y], Any] = None) -> Dict[Y, List[V]]:
    '''
    >>> groupListBy([1, 2, 3, 1])
    {1: [1, 1], 2: [2], 3: [3]}
    >>> groupListBy([1, 2, 3, 1, 4], lambda x: x>2)
    {False: [1, 2, 1], True: [3, 4]}
    '''
    res: Dict[Y, List[V]] = {}
    if iteratee is None:
        for v in arr:
            elems = res.setdefault(v, [])
            elems.append(v)
    else:
        if not callable(iteratee):
            it = iteratee

            def iteratee(x: V) -> Y:
                return get(x, it)
        for v in arr:
            elems = res.setdefault(iteratee(v), [])
            elems.append(v)
    return res
