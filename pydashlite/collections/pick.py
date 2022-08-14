from typing import Any, Dict, TypeVar, List, Hashable, Union, overload

from ..tools import isFlat, NoValue
from ..objects import pickPlain
from ..arrays import flatten
from ..collections import set_, get

T = TypeVar('T')
K = TypeVar('K', bound=Hashable)


@overload
def pick(obj: List[T], *properties) -> Dict[K, T]:
    ...


@overload
def pick(obj: Dict[K, T], *properties) -> Dict[K, T]:
    ...


def pick(obj: Union[List[T], Dict[K, T]], *properties) -> Dict[K, T]:
    '''
    auto choose pickPlain or pickDeep
    creates an object composed of the picked object properties
    >>> pick({'a': 1, 'b': 2, 'c': 3}, 'a')
    {'a': 1}
    >>> pick({'a': {'b': 1, 'c': 2, 'd': 3}}, 'a.b', 'a.d')
    {'a': {'b': 1, 'd': 3}}
    >>> pick({'a': [{'b': 1}, {'c': 2}, {'d': 3}]}, 'a[0]', 'a[2]')
    {'a': [{'b': 1}, None, {'d': 3}]}
    '''
    propsFlaten = flatten(properties)
    if isinstance(obj, dict) and isFlat(propsFlaten):
        return pickPlain(obj, propsFlaten)
    else:
        return pickDeep(obj, propsFlaten)


def pickDeep(obj: Union[List[T], Dict[K, T]], paths: List[K], deepCopy=False) -> Dict[K, T]:
    '''
    creates an object composed of the picked object properties
    >>> pickDeep({'a': 1, 'b': 2, 'c': 3}, 'a')
    {'a': 1}
    >>> pickDeep({'a': {'b': 1, 'c': 2, 'd': 3}}, 'a.b', 'a.d')
    {'a': {'b': 1, 'd': 3}}
    >>> pickDeep({'a': [{'b': 1}, {'c': 2}, {'d': 3}]}, 'a[0]', 'a[2]')
    {'a': [{'b': 1}, None, {'d': 3}]}
    :param deepCopy:
        apply copy.deepcopy to picked values
    '''
    res: Dict[K, T] = {}
    for path in paths:
        value = get(obj, path, NoValue, deepCopy)
        if value is not NoValue:
            set_(res, path, value)
    return res
