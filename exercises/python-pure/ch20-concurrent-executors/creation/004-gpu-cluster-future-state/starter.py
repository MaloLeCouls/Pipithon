"""Tu observes le cycle de vie d'une `Future` :
- avant submit : non-running, non-done,
- pendant l'exécution : running == True,
- après fin : done == True.

Contrat :

- `compute(x: int) -> int` est fournie (`time.sleep(0.05)` + `x * 2`).
- `submit_job(x: int, ex)` :
  - submit `compute(x)` sur `ex` (déjà fourni),
  - retourne la `Future` immédiatement (sans attendre la fin).
- `wait_done(fut) -> bool` :
  - bloque jusqu'à la fin (via `.result()`),
  - renvoie `fut.done()`.
"""
from __future__ import annotations

import time
from concurrent.futures import Future, ThreadPoolExecutor


def compute(x: int) -> int:
    time.sleep(0.05)
    return x * 2


def submit_job(x: int, ex: ThreadPoolExecutor) -> Future[int]:
    raise NotImplementedError("À implémenter")


def wait_done(fut: Future[int]) -> bool:
    raise NotImplementedError("À implémenter")
