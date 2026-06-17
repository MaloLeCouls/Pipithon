"""Un `Stack[T]` est typé : si tu crées `Stack[int]()`, mypy refuse
les pushes de str.

Contrat :

- `T = TypeVar("T")` au module-level.
- `class Stack(Generic[T])` :
  - `__init__(self)` : crée `_items: list[T] = []`.
  - `push(self, item: T) -> None`.
  - `pop(self) -> T` : pop le dernier ; lève IndexError si vide.
  - `peek(self) -> T` : renvoie le dernier sans pop ; lève IndexError si vide.
  - `__len__(self) -> int`.
"""
from __future__ import annotations

from typing import Generic, TypeVar


T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        raise NotImplementedError("À implémenter")

    def push(self, item: T) -> None:
        raise NotImplementedError("À implémenter")

    def pop(self) -> T:
        raise NotImplementedError("À implémenter")

    def peek(self) -> T:
        raise NotImplementedError("À implémenter")

    def __len__(self) -> int:
        raise NotImplementedError("À implémenter")
