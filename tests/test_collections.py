import math

import pydashlite.collections as pdl

from . import fixtures
from .fixtures import parametrize


@parametrize('case,expected', [
    (([4.2, 6.1, 6.4], lambda num: int(math.floor(num))), {4: [4.2], 6: [6.1, 6.4]}),
    (({'a':1, 'b':2, 'c':2, 'd': 3}, ), {1:[1], 2:[2, 2], 3:[3]}),
    (({'a':{1:1}, 'b':{1:2}, 'c':{1:2}}, 1), {1:[{1:1}], 2:[{1:2}, {1:2}]}),
    (({'a':[1], 'b':[2], 'c':[2,3], 'd': [3]}, lambda x: x[0]), {1:[[1]], 2:[[2], [2,3]], 3:[[3]]}),
    (([{1:1},{1:2},{1:2}],lambda x:x[1]), {1:[{1:1}], 2:[{1:2}, {1:2}]})
])
def test_group_by(case, expected):
    assert pdl.group_by(*case) == expected