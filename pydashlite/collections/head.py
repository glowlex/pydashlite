from typing import Any, Iterable, TypeVar, Union, overload, KeysView, Optional, Dict


T = TypeVar('T')
Y = TypeVar('Y')


@overload
def head(iterable: KeysView[T], default: Y) -> Union[T, Y]:
    ...


@overload
def head(iterable: Iterable[T], default: Y) -> Union[T, Y]:
    ...


@overload
def head(iterable: KeysView[T], default=None) -> Optional[T]:
    ...


@overload
def head(iterable: Iterable[T], default=None) -> Optional[T]:
    ...


def head(iterable: Union[Iterable[T], Dict[T, Any]], default: Optional[Y] = None) -> Union[Optional[T], Y]:
    '''
    returns first element of iterable if exists otherwise return default
    >>> head([1, 2])
    1
    >>> print(head([]))
    None
    >>> head({"a": 1})
    'a'
    >>> head({"a": 1, "b": 2}.values())
    1
    '''
    try:
        return next(iter(iterable), default)
    except:
        return default
