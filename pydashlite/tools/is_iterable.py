from typing import Any


# def isIterable(obj: Any) -> bool:
#     try:
#         iter(obj)
#     except:
#         return False
#     else:
#         return True


def isIterable(obj: Any) -> bool:
    try:
        obj.__iter__()
    except:
        return False
    else:
        return True
