"""Choix de design :
- `ex.map(fn, iter)` : équivalent parallèle de `map`. Préserve l'ordre.
- `list(...)` matérialise l'iterator avant la fin du `with` (sinon
  les itérations restantes seraient annulées par le shutdown).
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor


def probe(name: str) -> int:
    time.sleep(0.001)
    return len(name)


def sample_all(names: list[str]) -> list[int]:
    with ThreadPoolExecutor(max_workers=8) as ex:
        return list(ex.map(probe, names))
