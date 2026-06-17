"""Choix de design :
- `TypeVar("T")` : T est lié à la liste d'entrée. `first(list[int])` rend
  `int`, `first(list[str])` rend `str`.
- mypy peut désormais vérifier les usages en aval — pas d'Any qui contamine.
"""
from __future__ import annotations

from typing import TypeVar


T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]
