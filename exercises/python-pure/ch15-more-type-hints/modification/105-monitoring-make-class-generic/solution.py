"""Choix de design :
- `Generic[T]` paramètre la classe. `Box[int](42).unwrap()` est typé `int`.
- `T` est inféré depuis l'usage ; pas besoin d'écrire `Box[int](...)`
  explicitement la plupart du temps.
"""
from __future__ import annotations

from typing import Generic, TypeVar


T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def unwrap(self) -> T:
        return self.value
