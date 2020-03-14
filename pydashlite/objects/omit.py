from typing import Iterable, TypeVar, Iterable, Hashable, Dict
import copy


V = TypeVar('V')
K = TypeVar('K', bound=Hashable)


def omitPlain(obj: Dict[K, V], keys: Iterable[K]) -> Dict[K, V]:
    res = copy.copy(obj)
    for k in keys:
        if k in res:
            del res[k]
    return res
