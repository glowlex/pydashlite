from typing import Dict, TypeVar, Hashable, List, overload

from ..objects import chunkDict
from ..arrays import chunkList

V = TypeVar('V')
K = TypeVar('K', bound=Hashable)


@overload
def chunk(obj: List[V], size: int = 1) -> List[List[V]]:
    ...


@overload
def chunk(obj: Dict[K, V], size: int = 1) -> List[Dict[K, V]]:
    ...


def chunk(obj, size: int = 1):
    if isinstance(obj, dict):
        return chunkDict(obj, size)
    else:
        return chunkList(obj, size)
