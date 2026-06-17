"""Checkpoint chapitre 15 — Un `LRUCache[K, V]` générique typé, qui
évince le moins récemment utilisé quand `capacity` est dépassée.

C'est EXACTEMENT le pattern utilisé pour le prefix-caching dans vLLM
(structure plus complexe, mais même API mentale).

Contrat — `class LRUCache(Generic[K, V])` :

- `__init__(self, capacity: int)` :
  - capacity > 0, sinon ValueError,
  - stocke un `OrderedDict[K, V]` interne.
- `get(self, key: K) -> V | None` :
  - renvoie la valeur ET marque la clé comme « la plus récente »
    (`move_to_end`),
  - None si absente.
- `put(self, key: K, value: V) -> None` :
  - insère / update ; place la clé à la fin (la + récente),
  - si `len(self) > capacity` : pop le PREMIER (le - récent).
- `__len__(self) -> int`.
- `__contains__(self, key: object) -> bool`.

Tests vérifient le comportement LRU + le fait que la classe est
paramétrable (`LRUCache[str, int]`).
"""
from __future__ import annotations

from collections import OrderedDict
from typing import Generic, TypeVar


K = TypeVar("K")
V = TypeVar("V")


class LRUCache(Generic[K, V]):
    # À implémenter (__init__, get, put, __len__, __contains__).
    ...
