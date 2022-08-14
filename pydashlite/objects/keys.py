from typing import Any, Dict, List, TypeVar, Hashable

V = TypeVar('V')
K = TypeVar('K', bound=Hashable)


def keys(obj: Dict[K, V]) -> List[K]:
    '''
    returns list of keys
    >>> invert({1: 'a', 2: 'b'})
    ['a', 'b']
    '''
    return list(obj.keys())
