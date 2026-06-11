"""Choix de design :
- functools.partial fige un argument et renvoie une nouvelle callable.
- On fige `depot=depot` par mot-clé : plus explicite qu'un positionnel.
- Alternative : def make_router(depot): def fn(dest): return route_from(depot, dest); return fn.
  Marche aussi mais perd la nature « pré-fabriquée » de partial.
"""
from __future__ import annotations

from collections.abc import Callable
from functools import partial


def route_from(depot: str, destination: str) -> str:
    return f"{depot} -> {destination}"


def make_router(depot: str) -> Callable[[str], str]:
    return partial(route_from, depot)
