from typing import Union, List, Hashable, TypeVar

from ..tools import isIterable
from .extract_path_keys import extract_path_keys

Y = TypeVar('Y', Hashable, str, int)


def get_path_array(path: Union[Y, List[Y]]) -> List[Y]:
    if isinstance(path, str):
        return extract_path_keys(path)
    elif not isIterable(path):
        return [path]
    return path
