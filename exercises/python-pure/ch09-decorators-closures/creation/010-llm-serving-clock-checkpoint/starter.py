"""Le « test ferme la doc » du chapitre 9, façon Fluent Python.

Reproduis le pair canonique :

1. `clock(fmt: str)` : décorateur paramétré (3 niveaux) qui chronomètre la
   fonction et append à `CLOCK_LOG` une chaîne formatée selon `fmt`. Le
   format contient les placeholders {name}, {elapsed}, {result}. Utilise
   `@functools.wraps(fn)` pour préserver __name__/__doc__.
   Pour la testabilité on remplace le « temps réel » par un compteur global
   `_TICK` qui s'incrémente de 1 à chaque appel — comme ça les tests sont
   déterministes (elapsed = 1, 2, 3, ...).

2. `make_averager()` : closure (total, count) + nonlocal qui renvoie une
   fn `(new_value: float) -> float` — la moyenne courante.

Les deux briques sont rendues testables ensemble : un averager wrappé par
clock doit produire des moyennes correctes ET un log de chronométrage.
"""
from __future__ import annotations

from collections.abc import Callable

CLOCK_LOG: list[str] = []
_TICK = 0


def clock(fmt: str):
    ...


def make_averager() -> Callable[[float], float]:
    ...
