"""Ce décorateur trace les appels mais limite la signature à un seul argument
positionnel. Toute fonction qui prend des kwargs ou plusieurs args plante.

Refactor : rends le wrapper TRANSPARENT à n'importe quelle signature.
Le test passe priority=1 en kwarg pour démontrer.
"""
from __future__ import annotations

TRACES: list[str] = []


def trace(fn):
    def wrapper(arg):
        TRACES.append(fn.__name__)
        return fn(arg)
    return wrapper
