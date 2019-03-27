from typing import Union, Sequence, Iterable, List, Callable, Any, Hashable
from .objects import get


#collection, arrays, objects
def group_by(obj:Iterable, iteratee:Union[Callable[[Any], Hashable], Any]=None) -> dict:
    res = {}
    if iteratee is None:
        iteratee = lambda x: x
    elif not callable(iteratee):
        it = iteratee
        iteratee = lambda x: get(x, it)

    if isinstance(obj, dict):
        values = obj.values()
    else:
        values = obj

    for v in values:
        elems = res.setdefault(iteratee(v), [])
        elems.append(v)
    return res
