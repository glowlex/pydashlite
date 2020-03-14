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
    propsFlaten = flatten(properties)
    if isinstance(obj, dict) and isFlat(propsFlaten):
        return pickPlain(obj, propsFlaten)
    else:
        return pickDeep(obj, propsFlaten)


def pickDeep(obj: Union[List[T], Dict[K, T]], paths: List[K], deepCopy=False) -> Dict[K, T]:
    res: Dict[K, T] = {}
    for path in paths:
        value = get(obj, path, NoValue, deepCopy)
        if value is not NoValue:
            set_(res, path, value)
    return res
