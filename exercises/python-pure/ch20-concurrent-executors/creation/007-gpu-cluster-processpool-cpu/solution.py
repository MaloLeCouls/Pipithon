"""Choix de design :
- `ProcessPoolExecutor` : spawn de processus séparés, GIL inopérant. Pour
  du CPU-bound c'est l'option (vs threads).
- `ex.map(fn, iter)` : équivalent parallèle de `map`, préserve l'ordre.
- `hash_job` est au top-level (picklable). C'est obligatoire pour
  ProcessPool ; une lambda lèverait `PicklingError`.
"""
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor


def hash_job(payload: str) -> int:
    h = 0
    for c in payload:
        h = (h * 31 + ord(c)) & 0xFFFFFFFF
    for _ in range(10_000):
        h = (h * 7 + 1) & 0xFFFFFFFF
    return h


def batch_hashes(payloads: list[str]) -> list[int]:
    with ProcessPoolExecutor(max_workers=2) as ex:
        return list(ex.map(hash_job, payloads))
