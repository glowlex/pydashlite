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


    '''
    returns first element of iterable if exists otherwise return default
    >>> head([1, 2])
    1
    >>> head([])
    None
    >>> head({"a": 1})
    'a'
    '''
    try:
        return next(iter(iterable), default)
    except:
        return default
