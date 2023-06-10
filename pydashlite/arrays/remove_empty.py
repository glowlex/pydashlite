from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')


def removeEmpty(array: Iterable[Optional[T]]) -> List[T]:
    '''
    returns list without bool(value)==False elements\n
    shortcut for list(filter(None, array))
    >>> removeEmpty([0, 1, [], [2], None, '', 'a'])
    [1, [2], 'a']
    '''
    return list(filter(None, array))
