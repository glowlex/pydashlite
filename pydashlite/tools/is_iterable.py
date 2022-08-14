from typing import Any


# def isIterable(obj: Any) -> bool:
#     try:
#         iter(obj)
#     except:
#         return False
#     else:
#         return True


def isIterable(obj: Any) -> bool:
    '''
    returns True if obj is iterable
    '''
    try:
        obj.__iter__()
    except:
        return False
    else:
        return True
