"""Choix de design :
- `ProcessPoolExecutor` : chaque worker est un PROCESSUS séparé, donc
  pas de GIL partagé. Vrai parallélisme sur N cœurs.
- `hash_payload` reste au top-level (picklable).
- Comportement identique côté API ; perf ↑ sur du CPU-bound.
"""
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor


def hash_payload(payload: str) -> int:
    h = 0
    for c in payload:
        h = (h * 31 + ord(c)) & 0xFFFFFFFF
    for _ in range(5_000):
        h = (h * 7 + 1) & 0xFFFFFFFF
    return h


def batch_hashes(payloads: list[str]) -> list[int]:
    with ProcessPoolExecutor(max_workers=2) as ex:
        return list(ex.map(hash_payload, payloads))
