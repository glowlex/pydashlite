import math
import pytest

parametrize = pytest.mark.parametrize


class Object(object):
    def __init__(self, **attrs):
        for key, value in attrs.items():
            setattr(self, key, value)

    def __eq__(self, o: object) -> bool:
        for k, v in self.__dict__.items():
            try:
                if v != getattr(o, k):
                    return False
            except:
                return False
        return True


@pytest.fixture(autouse=True)
def add_missing(doctest_namespace):
    doctest_namespace["math"] = math
    doctest_namespace['ClassObject'] = Object
