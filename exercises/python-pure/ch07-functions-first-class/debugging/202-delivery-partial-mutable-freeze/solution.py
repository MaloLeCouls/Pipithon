"""Bug : `partial(route, extras=[])` capture UNE liste, partagée entre tous
les appels du router. C'est l'équivalent du défaut mutable, version partial.

Fix :
- Sentinelle dans `route` : extras défaut à None, instancié si besoin.
- partial ne fige plus que `depot`.
"""
from __future__ import annotations

from collections.abc import Callable
from functools import partial


def route(depot: str, destination: str, extras: list[str] | None = None) -> str:
    if extras is None:
        extras = []
    extras.append("delivered")
    return f"{depot} -> {destination} ({','.join(extras)})"


def make_router(depot: str) -> Callable[..., str]:
    return partial(route, depot)
