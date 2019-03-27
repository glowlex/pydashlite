from typing import Union, Sequence, Iterable, List, Callable, Any, Hashable
import itertools
import copy
import re
from inspect import signature, getfullargspec

from .arrays import flatten
from .tools import is_iterable

class _NoValue:
    pass


def pick(obj:Any, *properties) -> dict:
    props_flaten = flatten(properties)
    if isinstance(obj, dict) and _is_flat(props_flaten):
        return pick_flat(obj, props_flaten)
    else:
        return pick_deep(obj, props_flaten)


def pick_deep(obj:dict, paths:List[Hashable], deep_copy=False) -> dict:
    res = {}
    for path in paths:
        value = get(obj, path, _NoValue, deep_copy)
        if value is not _NoValue:
            set_(res, path, value)
    return res


def pick_flat(obj:dict, keys:Iterable) -> dict:
    return {k:v for k,v in obj.items() if k in keys}


def omit_flat(obj:dict, keys:Iterable) -> dict:
    return {k:v for k,v in obj.items() if k not in keys}


def _is_flat(array:Iterable) -> bool:
    for x in array:
        if is_iterable(x) and (not isinstance(x, str) or (x.find('.') !=-1 or x.find('[') !=-1)):
            return False
    return True


def set_(obj:Any, path:list, value:Any, deep_copy=False)->Any:
    path = _get_path_array(path)
    if deep_copy:
        obj = copy.deepcopy(obj)
    
    current_dest = obj
    nxt = type(obj)
    for k, v in zip(path, path[1:]):
        if k == '':
            nxt = dict
            continue
        if v == '':
            nxt = list
        current_dest = _merge_obj_struct(current_dest, nxt, k)
        
    last = path[-1]
    _set_basic(current_dest, last, value)
    return obj


def _merge_obj_struct(dest:Any, typ:Any, key:Any) -> Any:
    ext = get(dest, key, _NoValue)
    if ext is _NoValue:
        value = typ()
    else:
        return ext

    _set_basic(dest, key, value)
    return value


def _set_basic(dest:Any, key:Any, value:Any) -> Any:
    try:
        dest[key] = value
    except:
        if hasattr(dest, 'extend'):
            dest.extend([None]*(key-len(dest)) + [value])
        if isinstance(key, str):
            setattr(dest, key, value)
    return dest


def _get_path_array(path:Iterable[Union[int, str]]) -> list:
    if isinstance(path, str):
        path = _extract_path_keys(path)
    elif not is_iterable(path):
        path = [path]
    return path


pat = re.compile(r'(\[\d+\])')
pat1 = re.compile(r'(?<=[^\\])\.')
def _extract_path_keys(path:list)->list:
    res = []
    path = path.split('.') 
    for v in path:
        if v =='':
            continue
        path_splitted = pat.split(v)
        if len(path_splitted) == 1:
            res.extend(path_splitted)
            continue
        r1 = ['']*len(path_splitted)
        r1[::2] = path_splitted[::2]
        r1[2::2] = [int(p[1:-1]) for p in path_splitted[1::2]]
        res.extend(r1)
    return res


def get(obj:Any, path:Union[str, list], default=None, deep_copy=False)->Any:
    path = _get_path_array(path)
    res = obj
    for k in path:
        if k=='':
            continue
        try:
            res = res[k]
        except:
            try:
                res = getattr(res, k)
                if callable(res):
                    return default
            except:
                return default
    if deep_copy:
        return copy.deepcopy(res)
    else:
        return res


def map_keys(obj:dict, iteratee:Callable=None) -> dict:
    if iteratee is None:
        iteratee = lambda v,k,obj: k
    #n = len(getfullargspec(iteratee).args)
    n = _check_args_number(iteratee, obj)
    return {iteratee(*(v, k, obj)[:n]): v for k,v in obj.items()}


def _check_args_number(it, obj={}):
    a = head(obj)
    try:
        it(a[1])
        return 1
    except:
        try:
            it(a[1], a[0])
            return 2
        except:
            return 3


def rename_keys(obj:dict, key_map:dict)->dict:
    return {key_map.get(k, k):v for k,v in obj.items()}


def invert(obj:dict)->dict:
    return {v:k for k,v in obj.items()}


def head(obj:dict, default=None) -> tuple:
    try:
        r = next(iter(obj.items()))
    except:
        return default
    else:
        return r


def chunk(obj:dict, size:int=1) -> list:
    res = []
    ks = keys(obj)
    while len(ks):
        res.append({k:obj[k] for k in ks[:size]})
        ks = ks[size:]
    return res


def keys(obj:dict) -> list:
    return list(obj)


def find_key(obj:dict, iteratee:Union[Callable[[Hashable], bool], Any]=None, default=None) -> Any:
    if iteratee is None:
        iteratee = lambda x: x
    elif not callable(iteratee):
        it = iteratee
        iteratee = lambda x: x==it

    for k,v in obj.items():
        if iteratee(v):
            return k
    return default


#collection, arrays, objects
def group_by(obj:dict, iteratee:Union[Callable[[Any], Hashable], Any]=None) -> dict:
    res = {}
    if iteratee is None:
        iteratee = lambda x: x
    elif not callable(iteratee):
        it = iteratee
        iteratee = lambda x: get(x, it)

    for v in obj.values():
        elems = res.setdefault(iteratee(v), [])
        elems.append(v)
    return res


def merge(dest:dict, src:dict, max_depth=-1, deep_copy=False):
    if max_depth == 0:
        return src

    if deep_copy:
        src = copy.deepcopy(src)

    if isinstance(src, dict) and isinstance(dest, dict):
        iterate = src.items()
    elif isinstance(src, list) and isinstance(dest, list):
        iterate = enumerate(src)
    else:
        return src
    
    for key, src_value in iterate:
        dest_value = get(dest, [key])
        res_value = merge(dest_value, src_value, max_depth=max_depth-1)
        _set_basic(dest, key, res_value)
    return dest



def merge1(dest:dict, src:dict, max_depth=-1, deep_copy=False):
    '''not a real deep copy'''
    if max_depth == 0:
        if deep_copy:
            return copy.copy(src)
        return src

    if isinstance(src, dict) and isinstance(dest, dict):
        typ = 1
    elif isinstance(src, list) and isinstance(dest, list):
        typ = 2
    else:
        if deep_copy:
            return copy.copy(src)
        return src
    
    _merge1(dest, src, typ, max_depth, deep_copy)

    return dest


def _merge1(dest:dict, src:dict, type, max_depth, deep_copy):
    if type==1:
        iterate = src.items()
    else:
        iterate = enumerate(src)
    depth = max_depth-1
    for key, src_value in iterate:
        dest_value = get(dest, [key])
        if depth != 0:
            if isinstance(src_value, dict) and isinstance(dest_value, dict):
                res_value = _merge1(dest_value, src_value, 1, depth, deep_copy)
            elif isinstance(src_value, list) and isinstance(dest_value, list):
                res_value = _merge1(dest_value, src_value, 2, depth, deep_copy)
            else:
                res_value = src_value
            if deep_copy:
                res_value = copy.copy(res_value)
            _set_basic(dest, key, res_value)
        else:
            if deep_copy:
                src_value = copy.copy(src_value)
            _set_basic(dest, key, src_value)
    return dest