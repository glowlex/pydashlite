from collections import namedtuple

import pydashlite.objects as pdl

from . import fixtures
from .fixtures import parametrize


@parametrize('case,expected', [
    (({},), {}),
    (({'a': 1, 'b': 2},), {1: 'a', 2: 'b'})
])
def test_invert(case, expected):
    assert pdl.invert(*case) == expected


@parametrize('case,expected', [
    (({}, lambda v: v + 1), {}),
    (({'a': 1, 'b': 2}, lambda v: v + 1), {2: 1, 3: 2}),
    (({'a': 1, 'b': 2}, lambda v, k: k + str(v)), {'a1': 1, 'b2': 2}),
    (({'a': 1, 'b': 2}, lambda v, k, obj: obj[k] + 1), {2: 1, 3: 2}),
])
def test_map_keys(case, expected):
    assert pdl.mapKeys(*case) == expected


@parametrize('case,expected', [
    (({}, {"a": 'b'}), {}),
    (({'a': 1, 'b': 2}, {"a": 'b'}), {'b': 2}),
    (({'a': 1, 'b': 2}, {'a': 1, 'b': 2}), {1: 1, 2: 2}),
    (({'a': 1, 'b': 2}, {}), {'a': 1, 'b': 2}),
])
def test_rename_keys(case, expected):
    assert pdl.renameKeys(*case) == expected


@parametrize('case,expected', [
    (({}, 3), None),
    (({'a': 1, 'b': 2}, lambda x: x == 2), 'b'),
    (({'a': 0, 'b': 0}, None, 6), 6),
    (({'a': 3, 'b': 4}, 4), 'b')
])
def test_find_key(case, expected):
    assert pdl.findKey(*case) == expected


@parametrize('case,expected', [
    (({}, []), {}),
    (({'a': 1, 'b': 2}, ['a']), {'a': 1}),
    (({'a': 1, 'b': 2}, [3]), {}),
    (({'a': 1, 'b': 2, 1: 2, 2: 2}, ['a', 'b', 'c']), {'a': 1, 'b': 2}),
])
def test_pick_plain(case, expected):
    assert pdl.pickPlain(*case) == expected


@parametrize('case,expected', [
    (({}, []), {}),
    (({}, ['r']), {}),
    (({'a': 1, 'b': 2}, ['a']), {'b': 2}),
    (({'a': 1, 'b': 2}, [3]), {'a': 1, 'b': 2}),
    (({'a': 1, 'b': 2, 1: 2, 2: 2}, ['a', 'b', 'c']), {1: 2, 2: 2}),
])
def test_omit_plain(case, expected):
    assert pdl.omitPlain(*case) == expected
