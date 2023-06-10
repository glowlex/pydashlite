from typing import List, Any, Hashable, TypeVar, Union
import copy

from .get import get
from ..tools import NoValue, get_path_array

T = TypeVar('T')


def unset(obj: Any, path: Union[List[Hashable], Hashable], deepCopy=False) -> bool:
    '''
    removes the property at path of obj\n
    returns True if property was deleted\n
    >>> unset({"a": [{"b": {"c": 7}}]}, "a.[0].b.c")  # doctest: +SKIP
    {"a": [{"b": {}}]}
    >>> unset({"a": [{"b": {"c": 7}}]}, ["a", 0, "b", "c"])  # doctest: +SKIP
    {"a": [{"b": {}}]}
    >>> unset({'a': ClassObject(a=1, b=2)}, ['a', 'b'])  # doctest: +SKIP
    {'a': ClassObject(a=1)}\n
    :param deepCopy: apply copy.deepcopy to obj before unset operation
    '''
    if not obj:
        return False
    if deepCopy:
        obj = copy.deepcopy(obj)
    path = get_path_array(path)
    if not path:
        raise ValueError('path')
    parentObj = get(obj, path[:-1], default=NoValue)
    if parentObj is NoValue:
        return False
    lastP = path[-1]
    lastValue = get(parentObj, lastP, default=NoValue)
    if lastValue is NoValue:
        return False
    try:
        del parentObj[lastP]
    except:
        try:
            delattr(parentObj, lastP)
        except:
            return False
    return True
