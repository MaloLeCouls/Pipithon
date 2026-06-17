"""Choix de design :
- `threading.Lock` : le callback peut s'exécuter en concurrence sur
  plusieurs threads. Sans lock, `ok += 1` n'est pas atomique en bytecode.
- `add_done_callback(self.record)` : enregistre LE BOUND METHOD.
- `with ... as ex:` : sortie du with bloque jusqu'à la fin des tâches.
  À ce moment-là, tous les callbacks ont été appelés.
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
        self.ok = 0
        self.failed = 0
        self.lock = threading.Lock()

    def record(self, fut: Future) -> None:
        with self.lock:
            if fut.exception() is None:
                self.ok += 1
            else:
                self.failed += 1


def count_outcomes(names: list[str]) -> tuple[int, int]:
    counter = Counter()
    with ThreadPoolExecutor(max_workers=4) as ex:
        for name in names:
            fut = ex.submit(probe, name)
            fut.add_done_callback(counter.record)
    return counter.ok, counter.failed
