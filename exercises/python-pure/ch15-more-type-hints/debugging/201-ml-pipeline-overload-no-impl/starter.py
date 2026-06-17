"""Tous les appels à `normalize` lèvent `NotImplementedError`. Pourtant
le code a l'air complet : 2 overloads + une impl à 1 ligne.

Indices :
- Les `@overload` ne fournissent PAS de corps utilisable — ils sont
  remplacés par un placeholder.
- La VRAIE fonction (la dernière déclaration) ne doit PAS être décorée
  `@overload` — sinon elle est elle aussi remplacée par le placeholder.
- Solution : enlever `@overload` de la dernière déclaration.
"""
from __future__ import annotations

from typing import overload


@overload
def normalize(x: int) -> float: ...


@overload
def normalize(x: list[int]) -> list[float]: ...


# BUG : @overload sur l'impl finale -> Python remplace le corps par un placeholder.
@overload
def normalize(x: int | list[int]) -> float | list[float]:
    if isinstance(x, int):
        return float(x)
    return [float(i) for i in x]
