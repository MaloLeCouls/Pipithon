"""Le décorateur `timed(label)` est PARAMÉTRÉ (3 niveaux). Mais à
l'application, l'auteur a oublié les parenthèses : `@timed` au lieu de
`@timed('latency')`. Résultat : ping est wrappée par timed (qui attend un
label) — TypeError au premier appel.

Corrige l'application. Ne touche pas à la définition de `timed`.
"""
from __future__ import annotations

TIMINGS: list[tuple[str, object]] = []


def timed(label: str):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            TIMINGS.append((label, result))
            return result
        return wrapper
    return decorator


@timed
def ping() -> str:
    return "pong"
