from typing import TypeVar
import copy

from .get import get
from .set_ import _setBasic

T = TypeVar('T')


def merge(dest: T, src: T, maxDepth=-1, deepCopySrc=False, deepCopyDst=False) -> T:
    '''
    merges objects inplace or with deepCopySrc|deepCopyDst=True apply deepcopy on dst|src first
    if end object fields have dict types:
    >>> merge({'characters': [{'name': 'barney'}, {'name': 'fred'}]}, {'characters': [{'age': 36}, {'age': 40}]})
    {'characters': [{'name': 'barney', 'age': 36}, {'name': 'fred', 'age': 40}]}
    if end object fields have different types:
    >>> merge({'characters': {'barney': {'age': 36}}}, {'characters': {'barney': [5]}})
    {'characters': {'barney': [5]}}
    >>> merge({'characters': {'barney': {'age': 36}}}, {'characters': {'barney': [5]}})
    {'characters': {'barney': [5]}}
    :param maxDepth:
        >>> merge({"first": {'a': 1, 'b': 2}}, {'first': {'c': 1, 'd': 2}}, maxDepth=2)
        {'first': {'a': 1, 'b': 2, 'c': 1, 'd': 2}}
        >>> merge({'first': {'second': 3}}, {'first': {'second': 1}}, maxDepth=1)
        {'first': {'c': 1, 'd': 2}}
        maxDepth=-1 - without limitation
    :param deepCopySrc:
    :param deepCopyDst:
        make copy.deepcopy before operations
    '''
    if maxDepth == 0:
        return src

    if deepCopyDst:
        dest = copy.deepcopy(dest)
    if deepCopySrc:
        src = copy.deepcopy(src)

    if isinstance(src, dict) and isinstance(dest, dict):
        iterate = src.items()
    elif isinstance(src, list) and isinstance(dest, list):
        iterate = enumerate(src)
    else:
        return src

    for key, src_value in iterate:
        dest_value = get(dest, [key])
        res_value = merge(dest_value, src_value, maxDepth=maxDepth-1)
        _setBasic(dest, key, res_value)
    return dest
