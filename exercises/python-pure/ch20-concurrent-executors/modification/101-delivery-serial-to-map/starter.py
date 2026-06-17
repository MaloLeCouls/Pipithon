"""Cette boucle interroge un service de tracking en série. Sur N=100,
c'est ~100x trop lent. Parallélise via `ThreadPoolExecutor + ex.map`.

Comportement attendu : MÊME résultat, MÊME ordre, juste plus vite.
"""
from __future__ import annotations

import time


def track_one(tid: str) -> str:
    time.sleep(0.001)
    return f"shipped:{tid}"


def track_all(ids: list[str]) -> list[str]:
    # Anti-pattern : boucle séquentielle sur de l'I/O bound.
    return [track_one(tid) for tid in ids]
