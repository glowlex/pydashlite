from collections import namedtuple

import pydashlite.strings as pdl

from . import fixtures
from .fixtures import parametrize


@parametrize('case,expected', [
    ('fooBarBaz', 'fooBarBaz'),
    ('FooBarBaz', 'fooBarBaz'),
    ('FOO_BAR BAZ', 'fooBarBaz'),
    ('FOO BAR_bAz', 'fooBarBAz'),
    ('  foo  bar baz  ', 'fooBarBaz'),
    ('foo__bar_baz', 'fooBarBaz'),
    ('foo-_bar-_-baz', 'fooBarBaz'),
    (',foo!bar,baz,', 'fooBarBaz'),
    ('--foo.bar;baz', 'fooBarBaz'),
    ('', ''),
])
def test_camel_case(case, expected):
    assert pdl.camelCase(case) == expected
