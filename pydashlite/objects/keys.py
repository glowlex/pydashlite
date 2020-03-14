from typing import Any, Dict, List, TypeVar, Hashable

V = TypeVar('V')
K = TypeVar('K', bound=Hashable)


def keys(obj: Dict[K, V]) -> List[K]:
    return list(obj.keys())
