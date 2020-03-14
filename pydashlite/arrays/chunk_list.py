from typing import List, TypeVar

V = TypeVar('V')


def chunkList(array: List[V], size: int = 1) -> List[List[V]]:
    res = []
    if size < 1:
        raise ValueError("size must be greater 0")
    while len(array):
        res.append(array[:size])
        array = array[size:]
    return res
