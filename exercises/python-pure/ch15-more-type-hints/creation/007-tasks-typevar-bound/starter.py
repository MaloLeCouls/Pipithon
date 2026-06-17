"""Tu veux écrire `max_priority(items)` qui marche sur tout type
COMPARABLE (`<`). `TypeVar(bound=...)` exprime cette contrainte.

Contrat :

- Déclare `Comparable(Protocol)` avec `def __lt__(self, other: object) -> bool: ...`.
- Déclare `T = TypeVar("T", bound=Comparable)`.
- Écris `max_priority(items: list[T]) -> T` :
  renvoie le plus GRAND élément (max).
  Lève `ValueError` si la liste est vide (alignement avec `max([])`).

NB : à runtime, le bound n'est pas vérifié — c'est pur typing.
"""
from __future__ import annotations

from typing import Protocol, TypeVar


class Comparable(Protocol):
    def __lt__(self, other: object) -> bool: ...


T = TypeVar("T", bound=Comparable)


def max_priority(items: list[T]) -> T:
    raise NotImplementedError("À implémenter")
