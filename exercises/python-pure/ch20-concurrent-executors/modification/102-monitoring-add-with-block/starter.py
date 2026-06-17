"""L'executor est créé manuellement, sans `with`. Si une exception
remontait, ses threads resteraient en vol (zombies).

Wrappe-le dans un `with` pour garantir le shutdown.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor


def probe(name: str) -> int:
    time.sleep(0.001)
    return len(name)


def sample_all(names: list[str]) -> list[int]:
    # Anti-pattern : pas de `with` -> shutdown non garanti.
    ex = ThreadPoolExecutor(max_workers=4)
    results = list(ex.map(probe, names))
    ex.shutdown(wait=True)
    return results
