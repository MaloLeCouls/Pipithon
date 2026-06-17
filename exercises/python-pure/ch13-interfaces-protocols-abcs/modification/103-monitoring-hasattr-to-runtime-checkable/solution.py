"""Choix de design :
- `Protocol` + `@runtime_checkable` : déclaration explicite du contrat,
  réutilisable comme annotation de type partout dans le code.
- `isinstance(obj, Pingable)` remplace le couple `hasattr`/`callable` —
  même sémantique, intention plus claire.
- mypy --strict comprend désormais `is_pingable` comme un type guard
  potentiel (à compléter avec `TypeGuard` si besoin).
"""
from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Pingable(Protocol):
    def ping(self) -> bool: ...


def is_pingable(obj: object) -> bool:
    return isinstance(obj, Pingable)
