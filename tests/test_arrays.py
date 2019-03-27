

import pydashlite.arrays as pdl

from . import fixtures
from .fixtures import parametrize



@parametrize('case,expected', [
    ([1, 2, 1, 3, 1], [1, 2, 3]),
    ([dict(a=1), dict(a=2), dict(a=1)], [dict(a=1), dict(a=2)]),
])
def test_uniq(case, expected):
    assert pdl.uniq(case) == expected


@parametrize('case,expected', [
    (([1, 2, 3], [101, 2, 1, 10], [2, 1]), [1, 2, 3, 101, 10]),
    (([11, 22, 33],), [11, 22, 33]),
    (([11,],[dict(a=1), dict(a=1)]), [11, dict(a=1)]),
])
def test_union(case, expected):
    assert pdl.union(*case) == expected


@parametrize('case,expected', [
    (([1,2,3], [2]), [3]),
    (([1,2,3], [0, 2]), [1, 3]),
    (([1,2,3], []), []),
    (([1, 'a', None, dict], [-1, 5, 'a', dict]), [])
])
def test_at(case, expected):
    assert pdl.at(*case) == expected


@parametrize('case,expected', [
    (([1, 2, 3], [101, 2, 1, 10], [2, 1]), [1, 2]),
    (([1, 1, 2, 2], [1, 1, 2, 2]), [1, 2]),
    (([1, 2, 3], [4]), []),
    #(([1, 2, 3],), [1, 2, 3]),
    (([], [101, 2, 1, 10], [2, 1]), []),
    (([],), []),
    (([1, 'a', None, dict(a=1)], [-1, 5, 'a', dict(a=1)]), ['a', dict(a=1)])
])
def test_intersection(case, expected):
    assert pdl.intersection(*case) == expected    


@parametrize('case,expected', [
    (([1, 2, 3], [101, 2, [1, 10]], [2, 1]), [1, 2, 3, 101, 2, [1, 10], 2, 1]),
    (([],), [])
])
def test_concat(case, expected):
    assert pdl.concat(*case) == expected  


@parametrize('case,expected', [
    (([1,2,3],), 6),
    (([1,2,3],None, 2), 8),
    (([{1:1},{1:2},{1:3}],lambda x:x[1]), 6),
])
def test_sum_by(case, expected):
    assert pdl.sum_by(*case) == expected  