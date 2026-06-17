"""Choix de design :
- `submit` rend une Future IMMÉDIATEMENT — la fn ne bloque pas.
- `wait_done` appelle `.result()` pour bloquer + récupérer la valeur ;
  ensuite `done()` est True.
- C'est la mécanique standard de polling : `done()` côté lecteur,
  result()` côté consommateur final.
"""
from __future__ import annotations

import time
from concurrent.futures import Future, ThreadPoolExecutor


def compute(x: int) -> int:
    time.sleep(0.05)
    return x * 2


def submit_job(x: int, ex: ThreadPoolExecutor) -> Future[int]:
    return ex.submit(compute, x)


def wait_done(fut: Future[int]) -> bool:
    fut.result()  # bloque
    return fut.done()
