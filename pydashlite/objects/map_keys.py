from typing import Union, List, Hashable, TypeVar, Dict, Callable, Optional

from ..collections import head
from ..tools import NoValue

V = TypeVar('V')
K = TypeVar('K', bound=Hashable)


def mapKeys(obj: Dict[K, V], iteratee: Callable[[V, Optional[K], Optional[Dict[K, V]]], K]) -> Dict[K, V]:
    '''
    creates an object with the same values as obj and keys generated by running each element of object thru iteratee
    >>> mapKeys({'a': 1, 'b': 2}, lambda v: v + 1)
    {2: 1, 3: 2}
    >>> mapKeys({'a': 1, 'b': 2}, lambda v, k, obj: obj[k] + 1)
    {2: 1, 3: 2}
    '''
    n = _check_args_number(iteratee, obj)
    return {iteratee(*(v, k, obj)[:n]): v for k, v in obj.items()}


def _check_args_number(it, obj):
    k = head(obj, NoValue)
    if k is NoValue:
        return 3
    v = obj[k]
    try:
        it(v)
        return 1
    except:
        try:
            it(v, k)
            return 2
        except:
            return 3
