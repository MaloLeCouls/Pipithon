"""On veut un router avec une liste d'options supplémentaires (`extras`) qui
DÉMARRE vide pour chaque appel. L'auteur a essayé `partial(route, extras=[])`.

BUG : le `[]` est figé par partial. Tous les appels partagent la même liste,
les `extras.append(...)` d'un appel se voient sur le suivant.

Refactor :
1. Retire l'argument `extras` du partial.
2. Garde le default mutable-safe DANS `route` : `extras: list | None = None`
   puis `if extras is None: extras = []` à l'intérieur.

`make_router(depot)` doit renvoyer une fonction `(destination, extras=None) -> str`.
"""
from __future__ import annotations

from collections.abc import Callable
from functools import partial


def route(depot: str, destination: str, extras: list[str]) -> str:
    extras.append("delivered")
    return f"{depot} -> {destination} ({','.join(extras)})"


def make_router(depot: str) -> Callable[..., str]:
    return partial(route, depot, extras=[])
