"""Un `TypeVar` peut être **contraint** à un ensemble fini de types.
Différent du `bound` (qui accepte tout sous-type) : ici T est int OU
float, pas leur union.

Contrat :

- `T = TypeVar("T", int, float)`.
- `sum_typed(xs: list[T]) -> T` : renvoie la somme. Pour une `list[int]`,
  renvoie un `int` ; pour `list[float]`, un `float`.

NB : si l'appelant mixe int et float dans la même liste, mypy refuse —
parce que T est l'un OU l'autre, pas leur union.
"""
from __future__ import annotations

from typing import TypeVar


T = TypeVar("T", int, float)


def sum_typed(xs: list[T]) -> T:
    raise NotImplementedError("À implémenter")
