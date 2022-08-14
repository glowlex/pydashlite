from typing import Any, Dict, TypeVar, Hashable, Callable, Union

V = TypeVar('V')
K = TypeVar('K', bound=Hashable)
D = TypeVar('D', None, Any)


def findKey(obj: Dict[K, V], iteratee: Union[Callable[[V], bool], V], default: D = None) -> Union[K, D]:
    '''
    >>> findKey({1: 'a', 2: 'b'}, 'b')
    2
    >>> findKey({1: 'a', 2: 'b'}, lambda x: x == 'a')
    1
    '''
    if callable(iteratee):
        for k, v in obj.items():
            if iteratee(v):
                return k
    else:
        for k, v in obj.items():
            if v == iteratee:
                return k
    return default
