from typing import List, TypeVar

V = TypeVar('V')


def chunkList(array: List[V], size: int = 1) -> List[List[V]]:
    '''
    creates a list split into groups the length of size
    >>> chunkList([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]\n
    :param size: chunk size
    '''
    res = []
    if size < 1:
        raise ValueError("size must be greater 0")
    for i in range(len(array)//size + (len(array) % size != 0)):
        res.append(array[i*size:(i+1)*size])
    return res
