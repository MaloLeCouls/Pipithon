"""Choix de design :
- `Protocol[K, V]` : interface paramétrée par K (clé) et V (valeur).
  mypy infère K/V à partir de l'usage : `Cache[int, str]` exige
  `get(key: int) -> str | None`.
- `DictCache` est volontairement non-générique (concret pour dict[Any, Any]),
  l'exo se concentre sur la déclaration du Protocol, pas l'impl générique
  (qui demanderait `Generic[K, V]`).
"""
from __future__ import annotations

from typing import Protocol, TypeVar


K = TypeVar("K")
V = TypeVar("V")


class Cache(Protocol[K, V]):
    def get(self, key: K) -> V | None: ...
    def set(self, key: K, value: V) -> None: ...


class DictCache:
    def __init__(self) -> None:
        self._data: dict[object, object] = {}

    def get(self, key: object) -> object | None:
        return self._data.get(key)

    def set(self, key: object, value: object) -> None:
        self._data[key] = value
