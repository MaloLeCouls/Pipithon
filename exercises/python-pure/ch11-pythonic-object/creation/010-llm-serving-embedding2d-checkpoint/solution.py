"""Checkpoint ch.11 — Embedding2d = Vector2d transposé.

Choix de design :
- `__slots__` + `@property` read-only : value object immuable et économe
  en mémoire. Reproduit exactement `Vector2d v3` de Fluent Python.
- `__iter__` rend `tuple(self)` possible — qui sert à `__eq__`/`__hash__`
  par valeur.
- `__hash__` n'est défini que parce que `__eq__` est défini (sinon
  hash serait None). Tuple immuable des coords -> hash stable.
- `__format__` avec mini-langage `'p'` pour la forme polaire — copie
  conforme du chapitre.
- `from_pair` : `cls(...)` pour le polymorphisme via sous-classe.
"""
from __future__ import annotations

import math
from collections.abc import Iterator


class Embedding2d:
    __slots__ = ("__x", "__y")

    def __init__(self, x: float, y: float) -> None:
        object.__setattr__(self, "_Embedding2d__x", float(x))
        object.__setattr__(self, "_Embedding2d__y", float(y))

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    def __iter__(self) -> Iterator[float]:
        return iter((self.x, self.y))

    def __repr__(self) -> str:
        return f"Embedding2d({self.x!r}, {self.y!r})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Embedding2d):
            return NotImplemented
        return tuple(self) == tuple(other)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __format__(self, spec: str) -> str:
        if spec == "":
            return str(self)
        if spec == "p":
            r = abs(self)
            theta = math.atan2(self.y, self.x)
            return f"<{r}, {theta}>"
        raise ValueError(f"Unknown format spec: {spec}")

    @classmethod
    def from_pair(cls, pair: tuple[float, float]) -> "Embedding2d":
        x, y = pair
        return cls(x, y)
