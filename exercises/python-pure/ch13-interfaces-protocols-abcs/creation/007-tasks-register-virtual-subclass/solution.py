"""Choix de design :
- `Storable.register(RedisTask)` : RedisTask devient virtual subclass.
- Pas d'héritage syntaxique — `RedisTask.__mro__` ne contient PAS Storable.
- Mais `isinstance(rt, Storable)` est True et `issubclass(RedisTask, Storable)`
  aussi. Mécanique de goose typing : « il marche comme un Storable, on dit
  qu'il en est un, sans réécrire son code ».
- Limite : Python ne vérifie pas que RedisTask a vraiment `save`. Cf. piège
  du chapitre.
"""
from __future__ import annotations

import abc


class Storable(abc.ABC):
    @abc.abstractmethod
    def save(self) -> None: ...


class MemoryTask(Storable):
    def __init__(self) -> None:
        self.saved = False

    def save(self) -> None:
        self.saved = True


class RedisTask:
    def __init__(self) -> None:
        self.saved = False

    def save(self) -> None:
        self.saved = True


def register_redis() -> None:
    Storable.register(RedisTask)
