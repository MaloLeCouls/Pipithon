"""Choix de design :
- `wait(futs, return_when=FIRST_COMPLETED)` : bloque jusqu'à la première
  finie. Renvoie `(done, not_done)`.
- `cancel` sur les non finies. Best-effort : si déjà running, le worker
  finit son boulot mais on n'attendra pas son résultat.
- `done.pop()` : on prend la première du set retourné.
"""
from __future__ import annotations

import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait


def query_replica(name: str, delay: float) -> str:
    time.sleep(delay)
    return f"answer:{name}"


def race(replicas: list[tuple[str, float]]) -> str:
    with ThreadPoolExecutor(max_workers=len(replicas)) as ex:
        futures = [ex.submit(query_replica, n, d) for n, d in replicas]
        done, not_done = wait(futures, return_when=FIRST_COMPLETED)
        for f in not_done:
            f.cancel()
        winner = done.pop()
        return winner.result()
