"""Choix de design :
- `__slots__` : pas de `__dict__`, footprint mémoire = exactement 2 slots.
  À l'échelle d'un cache de 100k entrées, c'est des MB économisés.
- Immuabilité maison : `__init__` utilise `object.__setattr__` pour
  contourner le verrou ; `__setattr__` custom rejette toute autre
  écriture. Plus simple alternative : `@dataclass(frozen=True, slots=True)`
  — mais l'exo drille le pattern manuel pour comprendre la mécanique.
- `__hash__` = hash d'un tuple des champs. Tuple est sûr car ses éléments
  (str/tuple/int) sont eux-mêmes hashables et immuables.
"""
from __future__ import annotations


class TokenKey:
    __slots__ = ("_prefix", "_seq_id")

    def __init__(self, prefix: tuple[int, ...], seq_id: int) -> None:
        object.__setattr__(self, "_prefix", prefix)
        object.__setattr__(self, "_seq_id", seq_id)

    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError(f"TokenKey is immutable; cannot set {name!r}")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TokenKey):
            return NotImplemented
        return self._prefix == other._prefix and self._seq_id == other._seq_id

    def __hash__(self) -> int:
        return hash((self._prefix, self._seq_id))
