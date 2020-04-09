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


def head(iterable: Union[Iterable[T], Dict[T, Any]], default: Y = None) -> Union[Optional[T], Y]:
    try:
        return next(iter(iterable), default)
    except:
        return default
