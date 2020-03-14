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
    return [get(obj, p) for p in paths]
