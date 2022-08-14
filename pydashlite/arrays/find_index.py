from typing import Any, Iterable, TypeVar, Callable, Union

V = TypeVar('V')
D = TypeVar('D', None, Any)


def findIndex(array: Iterable[V], iteratee: Union[Callable[[V], bool], V], default: D = None) -> Union[int, D]:
    '''
    >>> findIndex([1, 2, 3], 3)
    2
    >>> findIndex([1, 2, 3], lambda x: x==3)
    2
    >>> findIndex([1, 2, 3], 4, default=-1)
    -1
    '''
    if callable(iteratee):
        for k, v in enumerate(array):
            if iteratee(v):
                return k
    else:
        for k, v in enumerate(array):
            if v == iteratee:
                return k
    return default
