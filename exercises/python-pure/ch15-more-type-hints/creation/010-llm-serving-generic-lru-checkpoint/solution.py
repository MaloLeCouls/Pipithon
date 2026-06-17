"""Checkpoint ch.15 — `LRUCache[K, V]` générique.

Choix de design :
- `Generic[K, V]` paramètre la classe sur la clé et la valeur. `LRUCache[str, int]`
  est typé pour mypy.
- `OrderedDict` : insertion-ordered + `move_to_end`/`popitem(last=False)`.
  Donne l'LRU en O(1) par op.
- `get` marque la clé comme « plus récente ». C'est ce qui fait que
  les KEYS LUES restent dans le cache même quand on fait des putes.
- `put` évince UNIQUEMENT quand la capacity est dépassée APRÈS insertion.
"""
from __future__ import annotations

from collections import OrderedDict
from typing import Generic, TypeVar


K = TypeVar("K")
V = TypeVar("V")


class LRUCache(Generic[K, V]):
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError(f"capacity must be > 0, got {capacity}")
        self._capacity = capacity
        self._data: OrderedDict[K, V] = OrderedDict()

    def get(self, key: K) -> V | None:
        if key not in self._data:
            return None
        self._data.move_to_end(key)
        return self._data[key]

    def put(self, key: K, value: V) -> None:
        if key in self._data:
            self._data.move_to_end(key)
        self._data[key] = value
        if len(self._data) > self._capacity:
            self._data.popitem(last=False)

    def __len__(self) -> int:
        return len(self._data)

    def __contains__(self, key: object) -> bool:
        return key in self._data
