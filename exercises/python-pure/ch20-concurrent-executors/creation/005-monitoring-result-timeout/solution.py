"""Choix de design :
- `fut.result(timeout=timeout)` : bloque au plus `timeout` secondes.
  Au-delà, lève `concurrent.futures.TimeoutError` (différente de la
  classe builtin `TimeoutError` — attention à l'import !).
- On capture et renvoie `-1` comme sentinel.
- Le `with` finit par attendre la tâche (shutdown=wait), donc le test
  peut être lent si sleep_s >> timeout. C'est l'objet du chapitre 20 :
  un timeout sur .result() n'annule PAS le job (pour ça, il faut
  `executor.shutdown(cancel_futures=True)`).
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutTimeout


def slow_probe(name: str, sleep_s: float) -> int:
    time.sleep(sleep_s)
    return len(name)


def sample_with_timeout(name: str, sleep_s: float, timeout: float) -> int:
    with ThreadPoolExecutor(max_workers=1) as ex:
        fut = ex.submit(slow_probe, name, sleep_s)
        try:
            return fut.result(timeout=timeout)
        except FutTimeout:
            return -1
