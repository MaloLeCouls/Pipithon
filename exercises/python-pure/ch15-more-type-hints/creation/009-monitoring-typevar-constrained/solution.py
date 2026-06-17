"""Choix de design :
- `TypeVar("T", int, float)` : T est int OU float, choisi par mypy à
  partir de l'usage. Garantit la cohérence du retour avec l'entrée.
- `sum(xs)` builtin somme tous les éléments en préservant le type
  (somme d'ints = int, somme de floats = float).
- Sur une liste vide, `sum([])` renvoie 0 (int). C'est un edge case
  du type qu'on ignore pour simplifier l'exo.
"""
from __future__ import annotations

from typing import TypeVar


T = TypeVar("T", int, float)


def sum_typed(xs: list[T]) -> T:
    return sum(xs)  # type: ignore[return-value]
