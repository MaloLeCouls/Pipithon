"""Choix de design :
- `bound=Comparable` : T peut être n'importe quel sous-type de Comparable
  (= toute classe avec `__lt__`). mypy refuse `max_priority([object(),
  object()])` parce que `object` n'a pas `__lt__`.
- `max(items)` builtin fait le boulot, et préserve le type T en retour.
- On laisse `max([])` lever ValueError naturellement.
"""
from __future__ import annotations

from typing import Protocol, TypeVar


class Comparable(Protocol):
    def __lt__(self, other: object) -> bool: ...


T = TypeVar("T", bound=Comparable)


def max_priority(items: list[T]) -> T:
    return max(items)
