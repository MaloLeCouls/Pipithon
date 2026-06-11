"""On a un décorateur @audit qui log chaque appel et un @cache de mémoïsation.

L'ordre actuel : `@audit` au-dessus de `@cache` :
- audit s'applique en dernier -> il enveloppe le cache.
- chaque appel passe par audit, MÊME les hit du cache -> on audite tout.

L'objectif : auditer SEULEMENT les vrais calculs (les miss). Donc inverse
les décorateurs pour que cache enveloppe audit.

Le test compte les entrées dans AUDIT.
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


@audit
@functools.cache
def square(n: int) -> int:
    return n * n
