from typing import Any, Dict, List, TypeVar, Hashable

V = TypeVar('V')
K = TypeVar('K', bound=Hashable)


def keys(obj: Dict[K, V]) -> List[K]:
    '''
    returns list of keys
    >>> keys({1: 'a', 2: 'b'})
    [1, 2]
    '''
    return list(obj.keys())
