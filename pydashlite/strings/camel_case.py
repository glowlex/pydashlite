import re

pat = re.compile(r'(?:[^\w\d]|_)+')


def camelCase(text: str) -> str:
    '''
    transform string to camelCase format
    >>> camelCase('FooBarBaz')
    fooBarBaz
    >>> camelCase('FOO_BAR BAZ')
    fooBarBaz
    >>> camelCase('FOO BAR_bAz')
    fooBarBAz
    >>> camelCase('  foo  bar baz  ')
    fooBarBaz
    >>> camelCase('foo__bar_baz')
    fooBarBaz
    >>> camelCase('foo-_bar-_-baz')
    fooBarBaz
    >>> camelCase(',foo!bar,baz,')
    fooBarBaz
    >>> camelCase('--foo.bar;baz')
    fooBarBaz
    '''
    spl = pat.split(text)
    ns = ''.join(f'{x[:1].capitalize()}{x[1:]}' if x.upper() != x else x.capitalize() for x in spl)
    return f'{ns[:1].lower()}{ns[1:]}'
