import re

pat = re.compile(r'(?:[^\w\d]|_)+')


def camelCase(text: str) -> str:
    spl = pat.split(text)
    ns = ''.join(f'{x[:1].capitalize()}{x[1:]}' if x.upper() != x else x.capitalize() for x in spl)
    return f'{ns[:1].lower()}{ns[1:]}'
