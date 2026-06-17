"""Choix de design :
- `ex.map(track_one, ids)` : parallèle + ordre préservé.
- `list(...)` matérialise avant la sortie du `with`.
- Sémantique idem, vitesse N fois mieux (jusqu'à `max_workers`).
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor


def track_one(tid: str) -> str:
    time.sleep(0.001)
    return f"shipped:{tid}"


def track_all(ids: list[str]) -> list[str]:
    with ThreadPoolExecutor(max_workers=8) as ex:
        return list(ex.map(track_one, ids))
