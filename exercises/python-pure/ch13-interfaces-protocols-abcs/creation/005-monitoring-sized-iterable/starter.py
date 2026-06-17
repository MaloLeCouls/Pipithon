"""Une `MetricWindow` représente une fenêtre glissante de N valeurs. On
veut qu'elle réponde à `len(window)` ET qu'on puisse `for v in window:`.

Contrat :

- Classe `MetricWindow(Sized, Iterable[float])`.
- `__init__(self, values: list[float])`.
- `__len__` : taille de la fenêtre.
- `__iter__` : itère les valeurs en ordre.
- Les ABCs imposent ces deux méthodes ; tu en tires gratuitement
  `isinstance(w, Sized)` et `Iterable[float]`.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator, Sized


class MetricWindow(Sized, Iterable[float]):
    def __init__(self, values: list[float]) -> None:
        raise NotImplementedError("À implémenter")

    def __len__(self) -> int:
        raise NotImplementedError("À implémenter")

    def __iter__(self) -> Iterator[float]:
        raise NotImplementedError("À implémenter")
