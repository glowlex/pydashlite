from typing import Dict, TypeVar, Hashable, List

V = TypeVar('V')
K = TypeVar('K', bound=Hashable)


def chunkDict(obj: Dict[K, V], size: int = 1) -> List[Dict[K, V]]:
    '''
    creates a list split into groups the length of size
    >>> chunkDict({'a': 1, 'b': 2, 'c': 3}, 2)
    [{'a': 1, 'b': 2}, {'c': 3}]\n
    :param size: chunk size
    '''
    res = []
    if size < 1:
        raise ValueError("size must be greater 0")
    ks = list(obj)
    for i in range(len(ks)//size +(len(ks)%size != 0)):
        res.append({k: obj[k] for k in ks[i*size:(i+1)*size]})
    return res
