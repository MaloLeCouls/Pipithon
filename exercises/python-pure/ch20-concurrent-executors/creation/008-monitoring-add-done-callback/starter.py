"""Tu veux compter les `ok` et `failed` au fil de l'eau, sans attendre
la fin de toutes les futures. `add_done_callback` enregistre un hook
qui s'exécute dès qu'une future est done.

Contrat — `class Counter`:

- `__init__` : `self.ok = 0`, `self.failed = 0`, `self.lock = threading.Lock()`.
- `record(self, fut)` : si `fut.exception() is None` → incrémente `ok`,
  sinon `failed`. **Avec le lock** (le callback peut s'exécuter dans
  plusieurs threads concurremment).

- `probe(name: str) -> int` est fournie ; lève ValueError si name=="bad".

- `count_outcomes(names: list[str]) -> tuple[int, int]` :
  - crée un Counter,
  - submit chaque probe(name) ; attache `add_done_callback(counter.record)`,
  - attend la fin avec `with ... as ex:`,
  - renvoie `(counter.ok, counter.failed)`.
"""
from __future__ import annotations

import threading
import time
from concurrent.futures import Future, ThreadPoolExecutor


def probe(name: str) -> int:
    time.sleep(0.001)
    if name == "bad":
        raise ValueError("probe failed")
    return len(name)


class Counter:
    def __init__(self) -> None:
        raise NotImplementedError("À implémenter")

    def record(self, fut: Future) -> None:
        raise NotImplementedError("À implémenter")


def count_outcomes(names: list[str]) -> tuple[int, int]:
    raise NotImplementedError("À implémenter")
