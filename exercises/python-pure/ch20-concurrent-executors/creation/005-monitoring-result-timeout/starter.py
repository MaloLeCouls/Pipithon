"""Tu interroges une probe lente. Tu n'as pas envie d'attendre plus de
50 ms — au-delà, tu renvoies une valeur sentinelle `-1`.

Contrat :

- `slow_probe(name: str, sleep_s: float) -> int` est fournie.
- `sample_with_timeout(name: str, sleep_s: float, timeout: float) -> int` :
  - submit `slow_probe` dans un ThreadPool,
  - utilise `fut.result(timeout=timeout)`,
  - si `concurrent.futures.TimeoutError` est levée, renvoie `-1`.

Note : la tâche ne s'arrête PAS automatiquement — elle continue dans
le worker. Le timeout interrompt seulement le WAIT.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutTimeout


def slow_probe(name: str, sleep_s: float) -> int:
    time.sleep(sleep_s)
    return len(name)


def sample_with_timeout(name: str, sleep_s: float, timeout: float) -> int:
    raise NotImplementedError("À implémenter")
