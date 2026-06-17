"""Checkpoint ch.13 — TokenBuffer = Tombola version `llm-serving`.

Choix de design :
- `TokenBuffer` expose un mince contrat (`load`/`pick` abstraites) et offre
  `loaded`/`inspect` GRATUITES — pattern Template Method, identique à Tombola.
- `RandomBuffer` montre la voie « inheritance + impl complète », avec un rng
  injectable pour la reproductibilité.
- `FIFOBuffer` montre l'override des méthodes concrètes héritées quand on
  peut faire MIEUX que l'impl par défaut (loaded = O(1) vs vider+recharger).
- `ListBuffer` montre le `register` : duck-typing élevé au rang d'ABC sans
  héritage syntaxique. Aucun garde-fou (cf. piège du chapitre), à manier
  avec discipline.
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
        return bool(self.inspect())

    def inspect(self) -> tuple[int, ...]:
        items: list[int] = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class RandomBuffer(TokenBuffer):
    def __init__(self, seed: int = 0) -> None:
        self._items: list[int] = []
        self._rng = random.Random(seed)

    def load(self, tokens: Iterable[int]) -> None:
        self._items.extend(tokens)

    def pick(self) -> int:
        if not self._items:
            raise LookupError("pick from empty RandomBuffer")
        idx = self._rng.randrange(len(self._items))
        return self._items.pop(idx)


class FIFOBuffer(TokenBuffer):
    def __init__(self) -> None:
        self._queue: collections.deque[int] = collections.deque()

    def load(self, tokens: Iterable[int]) -> None:
        self._queue.extend(tokens)

    def pick(self) -> int:
        if not self._queue:
            raise LookupError("pick from empty FIFOBuffer")
        return self._queue.popleft()

    def loaded(self) -> bool:
        return bool(self._queue)


class ListBuffer(list):
    def load(self, tokens: Iterable[int]) -> None:
        self.extend(tokens)

    def pick(self) -> int:
        try:
            return self.pop()
        except IndexError as e:
            raise LookupError("pick from empty ListBuffer") from e


TokenBuffer.register(ListBuffer)
