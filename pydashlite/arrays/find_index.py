from typing import Any, Iterable, TypeVar, Callable, Union

V = TypeVar('V')
D = TypeVar('D', None, Any)


def findIndex(array: Iterable[V], iteratee: Union[Callable[[V], bool], V], default: D = None) -> Union[int, D]:
    if callable(iteratee):
        for k, v in enumerate(array):
            if iteratee(v):
                return k
    else:
        for k, v in enumerate(array):
            if v == iteratee:
                return k
    return default
