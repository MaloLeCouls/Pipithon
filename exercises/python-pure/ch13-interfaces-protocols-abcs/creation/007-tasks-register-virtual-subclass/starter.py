"""Tu as une ABC `Storable` et un legacy `RedisTask` que tu ne veux PAS
modifier. `ABC.register` te permet de déclarer `RedisTask` comme « virtual
subclass » : `isinstance(rt, Storable)` devient True sans qu'il ait à
hériter ou implémenter quoi que ce soit.

Contrat :

- ABC `Storable(abc.ABC)` avec une méthode abstraite `save(self) -> None`.
- Classe `MemoryTask(Storable)` qui hérite normalement et implémente `save`.
- Classe `RedisTask` (PAS de subclassing) avec `save(self) -> None` (no-op).
- Fonction `register_redis() -> None` qui appelle
  `Storable.register(RedisTask)`.

Tests : avant register, `isinstance(RedisTask(), Storable)` est False.
Après `register_redis()`, c'est True.
"""
from __future__ import annotations

import abc


class Storable(abc.ABC):
    ...


class MemoryTask(Storable):
    ...


class RedisTask:
    def save(self) -> None:
        pass


def register_redis() -> None:
    raise NotImplementedError("À implémenter")
