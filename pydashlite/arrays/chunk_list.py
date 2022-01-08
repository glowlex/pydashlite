from typing import List, TypeVar

V = TypeVar('V')


def chunkList(array: List[V], size: int = 1) -> List[List[V]]:
    res = []
    if size < 1:
        raise ValueError("size must be greater 0")
    for i in range(len(array)//size +(len(array)%size != 0)):
        res.append(array[i*size:(i+1)*size])
    return res
