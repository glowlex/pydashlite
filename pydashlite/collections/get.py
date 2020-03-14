from typing import Any, Hashable, List, Union, TypeVar
import copy

from ..tools import NoValue, get_path_array

Y = TypeVar('Y', Hashable, str, int)


def get(obj: Any, path: Union[Y, List[Y]], default=None, doDeepCopy=False) -> Any:
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
