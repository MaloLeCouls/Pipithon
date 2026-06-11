"""Le « test ferme la doc » du chapitre 6, façon Fluent Python.

Reproduis deux classes de camion de livraison qui exposent les pièges de
mutabilité que tu dois avoir compris à fond.

1) `HauntedBus` — modélise le bug du défaut mutable :
   - `__init__(self, passengers: list[str] = ???)` doit utiliser un défaut
     mutable PARTAGÉ entre toutes les instances.
   - `pick(self, name)` -> append à `self.passengers`.
   - `drop(self, name)` -> remove de `self.passengers`.

2) `Bus` — la version saine :
   - `__init__` utilise le pattern None-guard pour isoler chaque instance.
   - `pick`/`drop` idem.

3) `make_fleet(prototype: Bus) -> tuple[Bus, Bus]` :
   - renvoie (shallow_clone, deep_clone) du prototype.
   - shallow_clone partage la liste des passagers ; deep_clone non.
   - Utilise `copy.copy` et `copy.deepcopy`.

But du checkpoint : observer comment HauntedBus pollue ses instances, et
comment shallow vs deep changent le comportement du clone.
"""
from __future__ import annotations


class HauntedBus:
    def __init__(self, passengers: list[str] = ...) -> None:  # type: ignore[assignment]
        ...

    def pick(self, name: str) -> None:
        ...

    def drop(self, name: str) -> None:
        ...


class Bus:
    def __init__(self, passengers: list[str] | None = None) -> None:
        ...

    def pick(self, name: str) -> None:
        ...

    def drop(self, name: str) -> None:
        ...


def make_fleet(prototype: Bus) -> tuple[Bus, Bus]:
    ...
