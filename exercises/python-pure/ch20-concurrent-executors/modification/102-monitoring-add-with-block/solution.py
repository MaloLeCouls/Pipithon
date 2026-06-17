"""Choix de design :
- `with ThreadPoolExecutor(...) as ex:` : shutdown garanti même sur
  exception, et plus court à écrire.
- Le `list(...)` à l'intérieur du with matérialise les résultats avant
  que l'executor soit fermé.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor


def probe(name: str) -> int:
    time.sleep(0.001)
    return len(name)


def sample_all(names: list[str]) -> list[int]:
    with ThreadPoolExecutor(max_workers=4) as ex:
        return list(ex.map(probe, names))
