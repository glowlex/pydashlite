from typing import Dict, TypeVar, Hashable

V = TypeVar('V')
K = TypeVar('K', bound=Hashable)


def renameKeys(obj: Dict[K, V], keyMap: Dict[K, K]) -> Dict[K, V]:
    return {keyMap.get(k, k): v for k, v in obj.items()}
