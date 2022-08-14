from typing import Any, Iterable, List, TypeVar, Iterable, Union, overload

from .get import get
from ..tools.no_value import NoValue

T = TypeVar('T')
K = TypeVar('K', str, int)


@overload
def at(obj: Iterable[Any], paths: Iterable[K]) -> List[Any]:
    ...


@overload
def at(obj: Iterable[Any], paths: Iterable[Iterable[K]]) -> List[Any]:
    ...


def at(obj: Any, paths: Iterable[Any]) -> List[Any]:
    """
    returns a list of values located in the in given paths
    >>> at([1, 2, 3], [0, 2])
    [1, 3]
    >>> at({'one': {'two': {'three': 4}, 4: 8}}, ['one.two.three', ['one', 4], 2])
    [4, 8, None]
    """
    return [get(obj, p) for p in paths]
