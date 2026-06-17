"""Choix de design :
- `with ThreadPoolExecutor(...) as ex:` — cleanup garanti à la sortie.
- `submit` rend une Future ; on stocke les futures dans l'ORDRE des ids.
- Lecture finale via `[f.result() for f in futures]` préserve l'ordre.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor


def track_one(tracking_id: str) -> str:
    time.sleep(0.001)
    return f"shipped:{tracking_id}"


def track_all(ids: list[str]) -> list[str]:
    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = [ex.submit(track_one, tid) for tid in ids]
    return [f.result() for f in futures]
