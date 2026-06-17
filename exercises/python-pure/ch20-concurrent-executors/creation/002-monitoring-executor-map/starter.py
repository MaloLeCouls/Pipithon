"""`ex.map(fn, iterable)` est l'équivalent parallèle de `map(fn, iterable)`.
Pratique quand on veut l'ordre d'origine + un map idiomatique.

Contrat :

- `probe(name: str) -> int` est fournie.
- `sample_all(names: list[str]) -> list[int]` :
  - utilise `ThreadPoolExecutor` + `ex.map(probe, names)`,
  - renvoie une `list` (pas l'iterator paresseux).
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor


def probe(name: str) -> int:
    time.sleep(0.001)
    return len(name)


def sample_all(names: list[str]) -> list[int]:
    raise NotImplementedError("À implémenter")
