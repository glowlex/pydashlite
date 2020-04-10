import re

pat = re.compile(r'(?:[^\w\d]|_)+')


def camelCase(text: str) -> str:
    spl = pat.split(text)
    ns = ''.join(x.capitalize() for x in spl)
    return f'{ns[:1].lower()}{ns[1:]}'
