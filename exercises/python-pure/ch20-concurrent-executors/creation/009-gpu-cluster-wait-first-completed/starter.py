"""Tu as N replicas du même service ; tu lances une requête à TOUS,
tu prends la PREMIÈRE réponse (latence ↓), tu annules les autres
(coût ↓).

C'est ce que vLLM/SGLang appellent « speculative racing » dans des
contextes plus avancés. La primitive : `concurrent.futures.wait` avec
`return_when=FIRST_COMPLETED`.

Contrat :

- `query_replica(name: str, delay: float) -> str` est fournie (renvoie
  `f"answer:{name}"` après le delay).
- `race(replicas: list[tuple[str, float]]) -> str` :
  - submit chaque `(name, delay)`,
  - `wait(futures, return_when=FIRST_COMPLETED)` → `(done, not_done)`,
  - cancel le reste (`for f in not_done: f.cancel()`),
  - renvoie le `result()` de la première finie.

NB : avec ThreadPoolExecutor, `.cancel()` ne marche que si la future
n'est pas encore EN COURS — c'est best-effort.
"""
from __future__ import annotations

import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait


def query_replica(name: str, delay: float) -> str:
    time.sleep(delay)
    return f"answer:{name}"


def race(replicas: list[tuple[str, float]]) -> str:
    raise NotImplementedError("À implémenter")
