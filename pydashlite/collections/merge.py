from typing import TypeVar
import copy

from .get import get
from .set_ import _setBasic

T = TypeVar('T')


def merge(dest: T, src: T, maxDepth=-1, deepCopySrc=False) -> T:
    if maxDepth == 0:
        return src

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
