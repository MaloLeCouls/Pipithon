"""Un Protocol GÉNÉRIQUE paramétré par 2 TypeVars : `Cache[K, V]`.

Contrat :

- `K = TypeVar("K")`, `V = TypeVar("V")`.
- `Cache(Protocol[K, V])` :
  - `def get(self, key: K) -> V | None: ...`
  - `def set(self, key: K, value: V) -> None: ...`
- `class DictCache` (implémentation simple) :
  - `__init__(self)` : `self._data: dict = {}`.
  - `get(self, key) -> value or None`.
  - `set(self, key, value) -> None`.
- Pas besoin de `@runtime_checkable` ici — c'est pour mypy.
"""
from __future__ import annotations

from typing import Protocol, TypeVar


K = TypeVar("K")
V = TypeVar("V")


class Cache(Protocol[K, V]):
    ...


class DictCache:
    # À implémenter (data + get + set).
    ...
