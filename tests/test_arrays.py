

import math
import pydashlite.arrays as pdl

from . import conftest
from .conftest import parametrize


@parametrize('case,expected', [
    (([4.2, 6.1, 6.4], lambda num: int(math.floor(num))), {4: [4.2], 6: [6.1, 6.4]}),
    (([{1: 1}, {1: 2}, {1: 2}], lambda x: x[1]), {1: [{1: 1}], 2: [{1: 2}, {1: 2}]}),
    (([{1: 1}, {1: 2}, {1: 2}], 1), {1: [{1: 1}], 2: [{1: 2}, {1: 2}]}),
])
def test_groupBy(case, expected):
    assert pdl.groupListBy(*case) == expected


@parametrize('case,expected', [
    (([1, 2, 3, 2, 1, 5, 6, 5, 5, 5],), [1, 2, 5]),
    ((['A', 'b', 'C', 'a', 'B', 'c'], lambda letter: letter.lower()), ['a', 'B', 'c']),
    ((['A', 'b', 'C', 'c', 'a', 'B'], lambda letter: letter.lower()), ['a', 'B', 'c']),
    ((['A', 'b', 'a', 'B', 'b'], lambda letter: letter.lower()), ['a', 'b']),
])
def test_duplicates_hash(case, expected):
    assert pdl.duplicatesHash(*case) == expected


@parametrize('case,expected', [
    (([1, 2, 3, 2, 1, 5, 6, 5, 5, 5],), [1, 2, 5]),
    ((['A', 'b', 'C', 'a', 'B', 'c'], lambda letter: letter.lower()), ['a', 'B', 'c']),
    ((['A', 'b', 'C', 'c', 'a', 'B'], lambda letter: letter.lower()), ['a', 'B', 'c']),
    ((['A', 'b', 'a', 'B', 'b'], lambda letter: letter.lower()), ['a', 'b']),
    (([{1: 2}, {1: 3}, {1: 2}],), [{1: 2}])
])
def test_duplicates(case, expected):
    assert pdl.duplicates(*case) == expected


@parametrize('case,expected', [
    (([], 89), None),
    (([1, [], ['2222'], 4], 1), 0),
    (([1, [], ['2222'], 4], []), 1),
    (([1, [], ['2222'], 4], lambda x: x == 4), 3),
])
def test_find_index(case, expected):
    assert pdl.findIndex(*case) == expected


@parametrize('case,expected', [
    (([1, [], ['2222'], [3, [[4]]]], 1), [1, '2222', 3, [[4]]]),
    (([1, [], ['2222'], [3, [[4]]]], 2), [1, '2222', 3, [4]]),
])
def test_flatten_depth(case, expected):
    assert pdl.flattenDepth(*case) == expected


@parametrize('case,expected', [
    ([1, [], ['2222'], [3, [[4]]]], [1, '2222', 3, 4]),
])
def test_flatten_deep(case, expected):
    assert pdl.flattenDeep(case) == expected


@parametrize('case,expected', [
    ([[]], []),
    ([1, [], ['2222'], [3, [[4]]]], [1, '2222', 3, [[4]]]),
])
def test_flatten(case, expected):
    assert pdl.flatten(case) == expected


@parametrize('case,expected', [
    ([], []),
    ([1, 2], [1, 2]),
    ([1, 2, 1, 3, 1, 1], [1, 2, 3]),
])
def test_uniq_hash(case, expected):
    assert pdl.uniqHash(case) == expected


@parametrize('case,expected', [
    ([], []),
    ([1, 2], [1, 2]),
    ([1, 2, 1, 3, 1, 1], [1, 2, 3]),
    ([dict(a=1), dict(a=2), dict(a=1)], [dict(a=1), dict(a=2)]),
    ([dict(a=1), 1, dict(a=1), 1], [dict(a=1), 1])
])
def test_uniq(case, expected):
    assert pdl.uniq(case) == expected


@parametrize('case,expected', [
    (([], lambda x: x), []),
    (([1, 2, 1, 5, 1, 1], lambda x: x % 3), [1, 2]),
    (([dict(a=1), dict(a=2), dict(a=1)], lambda x: {2: 2}), [dict(a=1)]),
])
def test_uniq_by(case, expected):
    assert pdl.uniqBy(*case) == expected


@parametrize('case,expected', [
    (([], lambda x: x), []),
    (([1, 5, 1, 1, 2], lambda x: x % 3), [1, 2]),
])
def test_uniq_hash_by(case, expected):
    assert pdl.uniqHashBy(*case) == expected


@parametrize('case,expected', [
    (([1, 2, 3], [101, 2, 1, 10], [2, 1]), [1, 2, 3, 101, 10]),
    (([11, 22, 33],), [11, 22, 33]),
    (([11, ], [dict(a=1), dict(a=1)]), [11, dict(a=1)]),
])
def test_union(case, expected):
    assert pdl.union(*case) == expected


@parametrize('case,expected', [
    (([1, 2, 3], [101, 2, 1, 10], [2, 1]), [1, 2]),
    (([[1], 2, 3], [[1], [2]]), [[1]]),
    (([1, 1, 2, 2], [1, 1, 2, 2]), [1, 2]),
    (([1, 2, 3], [4]), []),
    (([1, 2, 3],), [1, 2, 3]),
    (([], [101, 2, 1, 10], [2, 1]), []),
    (([],), []),
    (([1, 'a', None, dict(a=1)], [-1, 5, 'a', dict(a=1)]), ['a', dict(a=1)]),
    (([3, 1], [1, 2, 3]), [3, 1]),
    (([3, 2, 1], [1, 3]), [3, 1]),
    (([1, 2, 3], [1], [2]), []),
    (([3, 1, 1, 1], [1, 2, 3]), [3, 1]),
])
def test_intersection(case, expected):
    assert pdl.intersection(*case) == expected


@parametrize('case,expected', [
    (([1, 2, 3], [101, 2, 1, 10], [2, 1]), [1, 2]),
    (([1, 1, 2, 2], [1, 1, 2, 2]), [1, 2]),
    (([1, 2, 3], [4]), []),
    (([1, 2, 3],), [1, 2, 3]),
    (([], [101, 2, 1, 10], [2, 1]), []),
    (([],), []),
    (([3, 1], [1, 2, 3]), [3, 1]),
    (([3, 2, 1], [1, 3]), [3, 1]),
    (([1, 2, 3], [1], [2]), []),
    (([3, 1, 1, 1], [1, 2, 3]), [3, 1]),
])
def test_intersection_hash(case, expected):
    assert pdl.intersectionHash(*case) == expected


@parametrize('case,expected', [
    (([1, 2, 3], [101, 2, [1, 10]], [2, 1]), [1, 2, 3, 101, 2, [1, 10], 2, 1]),
    (([], []), [])
])
def test_concat(case, expected):
    assert pdl.concat(*case) == expected


@parametrize('case,expected', [
    (([1, 2, 3],), 6),
    (([1, 2, 3], None, 2), 8),
    (([{1: 1}, {1: 2}, {1: 3}], lambda x: x[1]), 6),
])
def test_sum_by(case, expected):
    assert pdl.sumBy(*case) == expected


@parametrize('case,expected', [
    (([0, 1, [], [2], None, '', 'a'],), [1, [2], 'a']),
])
def test_removeEmpty(case, expected):
    assert pdl.removeEmpty(*case) == expected
