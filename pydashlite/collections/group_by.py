from typing import Union, Iterable, List, Callable, Any, Hashable, Dict, TypeVar, overload
from .get import get

V = TypeVar('V')
K = TypeVar('K', bound=Hashable)
Y = TypeVar('Y', bound=Hashable)


@overload
def groupBy(obj: Dict[K, V], iteratee: Union[Callable[[V], Y], Any]) -> Dict[Y, List[V]]:
    ...


@overload
def groupBy(obj: Iterable[V], iteratee: Union[Callable[[V], Y], Any] = None) -> Dict[Y, List[V]]:
    ...


    '''
    creates an object composed of keys generated from the values itself
    or results of running each element thru iteratee
    >>> groupBy([1,1,2,3])
    {1: [1, 1], 2:[2], 3:[3]}
    >>> groupBy({'a': 1, 'b': 2, 'c': 2, 'd': 3})
    {1: [1], 2:[2, 2], 3:[3]}
    >>> groupBy([4.2, 6.1, 6.4], lambda num: int(math.floor(num)))
    {4: [4.2], 6: [6.1, 6.4]}
    '''
    res: Dict[Y, List[V]] = {}
    try:
        values = obj.values()
    except:
        values = obj

    if iteratee is None:
        for v in values:
            elems = res.setdefault(v, [])
            elems.append(v)
    else:
        if not callable(iteratee):
            it = iteratee

            def iteratee(x: V) -> Y:
                return get(x, it)
        for v in values:
            elems = res.setdefault(iteratee(v), [])
            elems.append(v)
    return res
