"""Fix : `ex.submit(probe, name)`. On passe la FN et ses ARGS séparés —
comme `functools.partial`. Le pool appelle `probe(name)` dans un worker.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor


def probe(name: str) -> int:
    time.sleep(0.001)
    return len(name)


def sample_all(names: list[str]) -> list[int]:
    with ThreadPoolExecutor(max_workers=4) as ex:
        futures = [ex.submit(probe, name) for name in names]
    return [f.result() for f in futures]
