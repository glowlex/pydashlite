from typing import Any, Dict, TypeVar, Hashable, Callable, Union

V = TypeVar('V')
K = TypeVar('K', bound=Hashable)
D = TypeVar('D', None, Any)


def findKey(obj: Dict[K, V], iteratee: Union[Callable[[V], bool], V], default: D = None) -> Union[K, D]:
    if callable(iteratee):
        for k, v in obj.items():
            if iteratee(v):
                return k
    else:
        for k, v in obj.items():
            if v == iteratee:
                return k
    return default
