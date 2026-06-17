"""Choix de design :
- Héritage multiple `Sized` + `Iterable[float]` : on hérite des deux
  contrats. Python n'a pas de surprise (ces ABCs n'ont pas d'état).
- `__iter__` renvoie un nouveau iter sur `self._values` à chaque appel ;
  ça permet plusieurs `for` indépendants sur le même MetricWindow.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator, Sized


class MetricWindow(Sized, Iterable[float]):
    def __init__(self, values: list[float]) -> None:
        self._values = list(values)

    def __len__(self) -> int:
        return len(self._values)

    def __iter__(self) -> Iterator[float]:
        return iter(self._values)
