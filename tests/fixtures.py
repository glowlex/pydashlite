import pytest

from pydash._compat import iteritems

parametrize = pytest.mark.parametrize


class Object(object):
    def __init__(self, **attrs):
        for key, value in iteritems(attrs):
            setattr(self, key, value)


