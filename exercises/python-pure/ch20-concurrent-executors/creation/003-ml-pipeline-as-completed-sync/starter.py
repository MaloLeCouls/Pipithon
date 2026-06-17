"""Tu charges N shards en parallèle ; tu veux les TRAITER dans l'ordre
d'ARRIVÉE (pas d'appel) pour minimiser le temps mort.

`concurrent.futures.as_completed(futures)` itère les Futures dans
l'ordre de fin.

Contrat :

- `load_shard(index: int, delay: float) -> int` est fournie (renvoie
  `index` après le delay).
- `order_by_completion(delays: list[float]) -> list[int]` :
  - submit chaque shard,
  - itère `as_completed` et accumule les `result()` dans une liste.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def load_shard(index: int, delay: float) -> int:
    time.sleep(delay)
    return index


def order_by_completion(delays: list[float]) -> list[int]:
    raise NotImplementedError("À implémenter")
