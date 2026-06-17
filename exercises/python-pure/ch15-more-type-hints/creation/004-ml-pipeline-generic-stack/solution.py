"""Choix de design :
- `Generic[T]` parametrise la classe ; mypy infère T à partir de la
  première utilisation (`Stack[int]()` → T = int).
- Implé interne : une `list[T]` — `append`/`pop` font tout le boulot.
- À runtime, `T` n'a aucun effet : c'est pur typing. Mais ça empêche
  les fautes de frappe + change le type de `pop()` retourné par mypy.
"""
from __future__ import annotations

from typing import Generic, TypeVar


T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def __len__(self) -> int:
        return len(self._items)
