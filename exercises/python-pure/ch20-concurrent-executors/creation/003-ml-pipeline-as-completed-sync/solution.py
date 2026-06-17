"""Choix de design :
- `with ThreadPoolExecutor`, on submit tout, puis `as_completed` rend
  les Futures dans l'ordre de fin.
- Chaque future est lue avec `.result()`. Si elle a levé, le re-raise
  remonte ici — comportement sain (on n'avale rien).
- Le résultat est l'ordre d'arrivée, comme dans Fluent Python's flag
  download.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def load_shard(index: int, delay: float) -> int:
    time.sleep(delay)
    return index


def order_by_completion(delays: list[float]) -> list[int]:
    order: list[int] = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = [ex.submit(load_shard, i, d) for i, d in enumerate(delays)]
        for fut in as_completed(futures):
            order.append(fut.result())
    return order
