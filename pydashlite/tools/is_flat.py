from typing import Iterable, TypeVar, Iterable

from .is_iterable import isIterable

T = TypeVar('T')


def isFlat(array: Iterable[T]) -> bool:
    '''
    returns True if list is one dimensional array
    '''
    for x in array:
        if isIterable(x) and (not isinstance(x, str) or (x.find('.') != -1 or x.find('[') != -1)):
            return False
    return True
