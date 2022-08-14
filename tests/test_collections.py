import math
from collections import namedtuple

import pydashlite.collections as pdl

from . import fixtures
from .fixtures import parametrize, Object


@parametrize('case,expected', [
    (({'a': 1, 'b': 2, 'c': 3}, 'a'), {'a': 1}),
    (({'a': 1, 'b': 2, 'c': 3}, 'a', 'b'), {'a': 1, 'b': 2}),
    (({'a': 1, 'b': 2, 'c': 3}, ['a', 'b']), {'a': 1, 'b': 2}),
    (({'a': 1, 'b': 2, 'c': 3}, ['a'], ['b']), {'a': 1, 'b': 2}),
    (([1, 2, 3],), {}),
    (([1, 2, 3], 0), {0: 1}),
    ((fixtures.Object(a=1, b=2, c=3), 'a'), {'a': 1}),
    (({'a': {'b': 1, 'c': 2, 'd': 3}}, 'a.b', 'a.d'), {'a': {'b': 1, 'd': 3}}),
    (({'a': [{'b': 1}, {'c': 2}, {'d': 3}]}, 'a[0]', 'a[2]'), {'a': [{'b': 1}, None, {'d': 3}]}),
    (({'a': {'b': 1, 'c': 2, 'd': fixtures.Object(a=1, b=2, c=3)}}, ['a.d.m', 'd', 1]), {}),
    (({'a': 1}, 'b.3'), {}),
    (({'a': 1}, 'a', 2), {'a': 1})
])
def test_pick(case, expected):
    assert pdl.pick(*case) == expected


@parametrize('case,expected', [
    (({'characters': [{'name': 'barney'}, {'name': 'fred'}]}, {'characters': [{'age': 36}, {'age': 40}]}),
        {'characters': [{'name': 'barney', 'age': 36}, {'name': 'fred', 'age': 40}]}),
    (({'characters': [{'name': 'barney'}, {'name': 'fred'}, {}]}, {'characters': [{'age': 36}, {'age': 40}]}),
        {'characters': [{'name': 'barney', 'age': 36}, {'name': 'fred', 'age': 40}, {}]}),
    (({'characters': [{'name': 'barney'}, {'name': 'fred'}]}, {'characters': [{'age': 36}, {'age': 40}, {}]}),
        {'characters': [{'name': 'barney', 'age': 36}, {'name': 'fred', 'age': 40}, {}]}),
    (({'characters': {'barney': {'age': 36}, 'fred': {'score': 7}}},
        {'characters': {'barney': {'score': 5}, 'fred': {'age': 40}}}),
        {'characters': {'barney': {'age': 36, 'score': 5}, 'fred': {'age': 40, 'score': 7}}}),
    (({'characters': {'barney': {'age': 36}, 'fred': {'score': 7}}}, {'characters': {'barney': [5], 'fred': 7}}),
        {'characters': {'barney': [5], 'fred': 7}}),
    (({'characters': {'barney': {'age': 36}, 'fred': {'score': 7}}}, {'foo': {'barney': [5], 'fred': 7}}),
        {'characters': {'barney': {'age': 36}, 'fred': {'score': 7}}, 'foo': {'barney': [5], 'fred': 7}}),
    (({'foo': {'bar': 1}}, {'foo': {}}), {'foo': {'bar': 1}}),
    (({1: {2: {'a': 1, 'b': 2}}}, {1: {2: {'c': 1, 'd': 2}}}, 2), {1: {2: {'c': 1, 'd': 2}}}),
    (({1: {2: {'a': 1, 'b': 2}}}, {1: {2: [1, 2]}}, 2), {1: {2: [1, 2]}})
])
def test_merge(case, expected):
    assert pdl.merge(*case) == expected


@parametrize('case,expected', [
    (({}, ['one', 'two', 'three', 'four'], 1), {'one': {'two': {'three': {'four': 1}}}}),
    (({}, 'one.two.three.four', 1), {'one': {'two': {'three': {'four': 1}}}}),
    (({'one': {'two': {}, 'three': {}}}, ['one', 'two', 'three', 'four'], 1),
     {'one': {'two': {'three': {'four': 1}}, 'three': {}}}),
    (({'one': {'two': {}, 'three': {}}}, 'one.two.three.four', 1),
     {'one': {'two': {'three': {'four': 1}}, 'three': {}}}),
    (({}, 'one', 1), {'one': 1}),
    (([], [0, 0, 0], 1), [[[1]]]),
    (([], '[0].[0].[0]', 1), [[[1]]]),
    (([1, 2, [3, 4, [5, 6]]], [2, 2, 1], 7), [1, 2, [3, 4, [5, 7]]]),
    (([1, 2, [3, 4, [5, 6]]], '[2].[2].[1]', 7), [1, 2, [3, 4, [5, 7]]]),
    (([1, 2, [3, 4, [5, 6]]], [2, 2, 2], 7), [1, 2, [3, 4, [5, 6, 7]]]),
    (([1, 2, [3, 4, [5, 6]]], '[2].[2].[2]', 7), [1, 2, [3, 4, [5, 6, 7]]]),
    (({}, 'a.b[0].c', 1), {'a': {'b': [{'c': 1}]}}),
    (({}, 'a.b[0][0].c', 1), {'a': {'b': [[{'c': 1}]]}}),
    (({}, 'a', tuple), {'a': tuple}),
    ((tuple([1, 2, 3]), 0, 5), tuple([1, 2, 3])),
    ((Object(a=1), 'a', 2), Object(a=2)),
])
def test_set_(case, expected):
    assert pdl.set_(*case) == expected


@parametrize('case,expected,modValue', [
    (({"a": [{"b": {"c": 7}}]}, "a.[0].b.c"), True, {"a": [{"b": {}}]}),
    (({"a": [{"b": {"c": 7}}]}, ["a", 0, "b", "c"]), True, {"a": [{"b": {}}]}),
    (([1, 2, 3], "[1]"), True, [1, 3]),
    (({1: 'a', 2: 'b'}, 1), True, {2: 'b'}),
    (([1, 2, 3], 1), True, [1, 3]),
    (([1, [2, 3]], [1, 1]), True, [1, [2]]),
    (([1, 2, 3], "[0][0]"), False, [1, 2, 3]),
    (([1, 2, 3], "[0][0][0]"), False, [1, 2, 3]),
    (({'a': {'b': fixtures.Object(a=1, b=2, c=3)}}, ['a', 'b', 'a']), True, {'a': {'b': fixtures.Object(b=2, c=3)}}),
])
def test_unset(case, expected, modValue):
    assert pdl.unset(*case) == expected
    assert case[0] == modValue


@parametrize('case,expected', [
    (([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]),
    (([], 2), []),
    (({'a': 1, 'b': 2},), [{'a': 1}, {'b': 2}]),
    (({'a': 1, 'b': 2, 1: 2, 2: 2}, 3), [{'a': 1, 'b': 2, 1: 2}, {2: 2}]),
    (({'a': 1, 'b': 2, 1: 2, 2: 2}, 6), [{'a': 1, 'b': 2, 1: 2, 2: 2}]),
    (({}, 6), [])
])
def test_chunk(case, expected):
    assert pdl.chunk(*case) == expected


@parametrize('case,expected', [
    (([1, 2, 3], [2]), [3]),
    (([1, 2, 3], [0, 2]), [1, 3]),
    (([1, 2, 3], []), []),
    (([1, 'a', None, dict], [-1, 5, 'a', dict]), [dict, None, None, None]),
    (({'one': {'two': {'three': 4}, 4: 8}}, ['one.two.three', ['one', 4], 2]), [4, 8, None])
])
def test_at(case, expected):
    assert pdl.at(*case) == expected


@parametrize('case,expected', [
    (([1, 2, 3],), 1),
    (([],), None),
    (({"1": 2, 3: 4},), "1"),
    (({}, 8), 8),
    ((1,), None),
])
def test_head(case, expected):
    assert pdl.head(*case) == expected


@parametrize('case,expected', [
    (([4.2, 6.1, 6.4], lambda num: int(math.floor(num))), {4: [4.2], 6: [6.1, 6.4]}),
    (({'a': 1, 'b': 2, 'c': 2, 'd': 3}, ), {1: [1], 2:[2, 2], 3:[3]}),
    (({'a': {1: 1}, 'b': {1: 2}, 'c': {1: 2}}, 1), {1: [{1: 1}], 2: [{1: 2}, {1: 2}]}),
    (({'a': [1], 'b': [2], 'c': [2, 3], 'd': [3]}, lambda x: x[0]), {1: [[1]], 2: [[2], [2, 3]], 3: [[3]]}),
    (([{1: 1}, {1: 2}, {1: 2}], lambda x: x[1]), {1: [{1: 1}], 2: [{1: 2}, {1: 2}]})
])
def test_groupBy(case, expected):
    assert pdl.groupBy(*case) == expected


@parametrize('case,expected', [
    (({'one': {'two': {'three': 4}}}, 'one.two'), {'three': 4}),
    (({'one': {'two': {'three': 4}}}, 'one.two.three'), 4),
    (({'one': {'two': {'three': 4}}}, ['one', 'two']), {'three': 4}),
    (({'one': {'two': {'three': 4}}}, ['one', 'two', 'three']), 4),
    (({'one': {'two': {'three': 4}}}, 'one.four'), None),
    (({'one': {'two': {'three': 4}}}, 'one.four.three', []), []),
    (({'one': {'two': {'three': 4}}}, 'one.four.0.a', [{'a': 1}]), [{'a': 1}]),
    (({'one': {'two': {'three': [{'a': 1}]}}}, 'one.four.three.0.a', []), []),
    (({'one': {'two': {'three': 4}}}, 'one.four.three'), None),
    (({'one': {'two': {'three': [{'a': 1}]}}}, 'one.four.three.0.a'), None),
    (({'one': {'two': {'three': 4}}}, 'one.four.three', 2), 2),
    (({'one': {'two': {'three': [{'a': 1}]}}}, 'one.four.three.0.a', 2), 2),
    (({'one': {'two': {'three': 4}}}, 'one.four.three', {'test': 'value'}), {'test': 'value'}),
    (({'one': {'two': {'three': [{'a': 1}]}}}, 'one.four.three.0.a', {'test': 'value'}), {'test': 'value'}),
    (({'one': {'two': {'three': 4}}}, 'one.four.three', 'haha'), 'haha'),
    (({'one': {'two': {'three': [{'a': 1}]}}}, 'one.four.three.0.a', 'haha'), 'haha'),
    (({'one': {'two': {'three': 4}}}, 'five'), None),
    (({'one': ['two', {'three': [4, 5]}]}, ['one', 1, 'three', 1]), 5),
    (({'one': ['two', {'three': [4, 5]}]}, 'one.[1].three.[1]'), 5),
    # (({'one': ['two', {'three': [4, 5]}]}, 'one.1.three.1'), 5),
    ((['one', {'two': {'three': [4, 5]}}], '[1].two.three.[0]'), 4),
    ((['one', {'two': {'three': [4, [{'four': [5]}]]}}], '[1].two.three[1][0].four[0]'), 5),
    ((range(50), '[42]'), 42),
    (([[[[[[[[[[42]]]]]]]]]], '[0][0][0][0][0][0][0][0][0][0]'), 42),
    (([range(50)], '[0][42]'), 42),
    (({'a': [{'b': range(50)}]}, 'a[0].b[42]'), 42),
    (({'one': ['hello', 'there']}, 'one.bad.hello', []), []),
    (({'one': ['hello', None]}, 'one.1.hello'), None),
    ((namedtuple('a', ['a', 'b'])(1, 2), 'a'), 1),
    ((namedtuple('a', ['a', 'b'])(1, 2), 0), 1),
    ((namedtuple('a', ['a', 'b'])({'c': {'d': 1}}, 2), 'a.c.d'), 1),
    (({}, 'update'), None),
    (([], 'extend'), None),
    (({(1,): {(2,): 3}}, [(1,)]), {(2,): 3}),
    (({(1,): {(2,): 3}}, [(1,), (2,)]), 3),
    (({object: 1}, object), 1),
    (({object: {object: 1}}, [object, object]), 1),
])
def test_get(case, expected):
    assert pdl.get(*case) == expected
