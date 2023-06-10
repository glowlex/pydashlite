from typing import Any, Hashable, List, Union, TypeVar
import copy

from ..tools import NoValue, get_path_array

Y = TypeVar('Y', Hashable, str, int)


def get(obj: Any, path: Union[Y, List[Y]], default=None, doDeepCopy=False) -> Any:
    '''
    returns the value at path of object
    >>> get({'one': {'two': {'three': 4}}}, ['one', 'two', 'three'])
    4
    >>> get({"a": ClassObject(b=5)}, 'a.b')
    5
    >>> get([1, 2, 3], 2)
    3
    '''
    res = obj
    for k in get_path_array(path):
        if k == '':
            continue
        try:
            res = res[k]
        except LookupError:
            return default
        except TypeError:
            try:
                res = getattr(res, k)
                if callable(res):
                    return default
            except:
                return default
    if doDeepCopy:
        return copy.deepcopy(res)
    else:
        return res
