"""Checkpoint chapitre 13 — Reproduire la `Tombola` ABC de Fluent Python,
transposée en `TokenBuffer` pour un serveur d'inférence.

Tu vas écrire :

1. ABC `TokenBuffer(abc.ABC)` :
   - `@abstractmethod load(self, tokens: Iterable[int]) -> None` :
     ajoute des tokens au buffer.
   - `@abstractmethod pick(self) -> int` : pop un token. Lève `LookupError`
     si vide.
   - méthode CONCRÈTE `loaded(self) -> bool` : True s'il reste au moins un
     token. Implémentation : `bool(self.inspect())`.
   - méthode CONCRÈTE `inspect(self) -> tuple[int, ...]` : vide le buffer
     via `pick()` jusqu'à `LookupError`, recharge via `load()`, renvoie
     un tuple TRIÉ (ascendant) des items vus.

2. `RandomBuffer(TokenBuffer)` :
   - `__init__(self, seed: int = 0)` : stocke un `random.Random(seed)` et
     une liste interne vide.
   - `load` : extend la liste avec les tokens reçus.
   - `pick` : choisit un index ALÉATOIRE via le rng, pop cet index. Lève
     `LookupError` si vide.

3. `FIFOBuffer(TokenBuffer)` :
   - `__init__(self)` : `collections.deque[int]`.
   - `load` : extend.
   - `pick` : `popleft()`. Lève `LookupError` si vide.
   - OVERRIDE `loaded` : `bool(self._queue)` (plus efficace que `inspect`).

4. `ListBuffer(list)` :
   - Hérite de `list`.
   - `load` = `list.extend`.
   - `pick` = `list.pop` (avec rewrap `LookupError` au lieu d'`IndexError`).
   - **REGISTER** comme virtual subclass de `TokenBuffer` (pas d'héritage
     syntaxique de l'ABC, juste `TokenBuffer.register(ListBuffer)`).
"""
from __future__ import annotations

import abc
import collections
import random
from collections.abc import Iterable


class TokenBuffer(abc.ABC):
    @abc.abstractmethod
    def load(self, tokens: Iterable[int]) -> None: ...

    @abc.abstractmethod
    def pick(self) -> int: ...

    def loaded(self) -> bool:
        raise NotImplementedError("À implémenter")

    def inspect(self) -> tuple[int, ...]:
        raise NotImplementedError("À implémenter")


class RandomBuffer(TokenBuffer):
    def __init__(self, seed: int = 0) -> None:
        raise NotImplementedError("À implémenter")

    def load(self, tokens: Iterable[int]) -> None:
        raise NotImplementedError("À implémenter")

    def pick(self) -> int:
        raise NotImplementedError("À implémenter")


class FIFOBuffer(TokenBuffer):
    def __init__(self) -> None:
        raise NotImplementedError("À implémenter")

    def load(self, tokens: Iterable[int]) -> None:
        raise NotImplementedError("À implémenter")

    def pick(self) -> int:
        raise NotImplementedError("À implémenter")

    def loaded(self) -> bool:
        raise NotImplementedError("À implémenter")


class ListBuffer(list):
    def load(self, tokens: Iterable[int]) -> None:
        raise NotImplementedError("À implémenter")

    def pick(self) -> int:
        raise NotImplementedError("À implémenter")


# Register ListBuffer comme virtual subclass de TokenBuffer.
# Le test exige `isinstance(ListBuffer([1,2]), TokenBuffer) is True`.
# À toi de finaliser ici.
