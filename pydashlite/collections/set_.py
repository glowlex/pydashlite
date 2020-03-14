from typing import List, Any, Hashable, TypeVar, Union
import copy

from .get import get
from ..tools import NoValue, get_path_array

T = TypeVar('T')


def set_(obj: T, path: Union[List[Hashable], Hashable], value: Any, deep_copy=False) -> T:
    path = get_path_array(path)
    if deep_copy:
        obj = copy.deepcopy(obj)

    current_dest = obj
    nxt = type(obj)
    for k, v in zip(path, path[1:]):
        if k == '':
            nxt = dict
            continue
        if v == '':
            nxt = list
        current_dest = _mergeObjStruct(current_dest, nxt, k)

    last = path[-1]
    _setBasic(current_dest, last, value)
    return obj


def _mergeObjStruct(dest: Any, typ: Any, key: Any) -> Any:
    ext = get(dest, key, NoValue)
    if ext is NoValue:
        value = typ()
    else:
        return ext

    _setBasic(dest, key, value)
    return value


def _setBasic(dest: Any, key: Any, value: Any) -> Any:
    try:
        dest[key] = value
    except:
        if hasattr(dest, 'extend'):
            dest.extend([None] * (key - len(dest)) + [value])
        elif isinstance(key, str):
            setattr(dest, key, value)
    return dest
