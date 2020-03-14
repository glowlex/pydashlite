import re
from typing import List, Union

pat = re.compile(r'(\[\d+\])')


def extract_path_keys(path: str) -> List[Union[str, int]]:
    res: List[Union[str, int]] = []
    for v in path.split('.'):
        if v == '':
            continue
        path_splitted = pat.split(v)
        if len(path_splitted) == 1:
            res.extend(path_splitted)
            continue
        r1: List[Union[str, int]] = [''] * len(path_splitted)
        r1[::2] = path_splitted[::2]
        r1[2::2] = [int(p[1:-1]) for p in path_splitted[1::2]]
        res.extend(r1)
    return res
