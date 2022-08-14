from typing import Hashable, TypeVar, Dict


V = TypeVar('V', bound=Hashable)
K = TypeVar('K', bound=Hashable)


def invert(obj: Dict[K, V]) -> Dict[V, K]:
    '''
    swap keys with values
    >>> invert({1: 'a', 2: 'b'})
    {'a': 1, 'b': 2}
    '''
    return {v: k for k, v in obj.items()}
