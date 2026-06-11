"""Choix de design :
- Inversion : @functools.cache en haut, @audit en bas.
- Application : cache(audit(square)).
- Quand un cache hit se produit, cache renvoie directement -> audit n'est pas
  appelée. Seuls les vrais calculs traversent audit.
"""
from __future__ import annotations

import functools

AUDIT: list[str] = []


def audit(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        AUDIT.append(fn.__name__)
        return fn(*args, **kwargs)
    return wrapper


@functools.cache
@audit
def square(n: int) -> int:
    return n * n
