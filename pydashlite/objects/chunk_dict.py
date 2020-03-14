from typing import Dict, TypeVar, Hashable, List

V = TypeVar('V')
K = TypeVar('K', bound=Hashable)


def chunkDict(obj: Dict[K, V], size: int = 1) -> List[Dict[K, V]]:
    res = []
    if size < 1:
        raise ValueError("size must be greater 0")
    ks = list(obj)
    while len(ks):
        res.append({k: obj[k] for k in ks[:size]})
        ks = ks[size:]
    return res
