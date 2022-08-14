from typing import Iterable, TypeVar, Iterable, Hashable, Dict

from ..tools import NoValue


T = TypeVar('T')
V = TypeVar('V')
K = TypeVar('K', bound=Hashable)


def pickPlain(obj: Dict[K, V], keys: Iterable[K]) -> Dict[K, V]:
    '''
    creates an object composed of keys\n
    only one level depth
    >>> pickPlain({'a': 1, 'b': 2, 'c': 3}, ['a', 'c'])
    {'a': 1, 'c': 3}
    '''
    res = {}
    for k in keys:
        if k in obj:
            res[k] = obj[k]
    return res
