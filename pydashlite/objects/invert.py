from typing import Hashable, TypeVar, Dict


V = TypeVar('V', bound=Hashable)
K = TypeVar('K', bound=Hashable)


def invert(obj: Dict[K, V]) -> Dict[V, K]:
    return {v: k for k, v in obj.items()}
