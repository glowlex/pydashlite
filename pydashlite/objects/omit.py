from typing import Iterable, TypeVar, Iterable, Hashable, Dict
import copy


V = TypeVar('V')
K = TypeVar('K', bound=Hashable)


def omitPlain(obj: Dict[K, V], keys: Iterable[K]) -> Dict[K, V]:
    '''
    creates an object composed of keys and values that are not omitted\n
    only one level depth
    >>> omitPlain({'a': 1, 'b': 2, 'c': 3}, ['a', 'c'])
    {'b': 2}
    '''
    res = copy.copy(obj)
    for k in keys:
        if k in res:
            del res[k]
    return res
