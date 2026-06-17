"""Cette fn calcule un hash CPU-heavy sur N payloads avec un
ThreadPool. À cause du GIL, les threads n'apportent RIEN sur du
calcul pur — tu paies l'overhead pour rien.

Refactore en `ProcessPoolExecutor` (vrai parallélisme).
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor


def hash_payload(payload: str) -> int:
    h = 0
    for c in payload:
        h = (h * 31 + ord(c)) & 0xFFFFFFFF
    for _ in range(5_000):
        h = (h * 7 + 1) & 0xFFFFFFFF
    return h


def batch_hashes(payloads: list[str]) -> list[int]:
    # Anti-pattern : ThreadPool sur CPU-bound = bloqué par le GIL.
    with ThreadPoolExecutor(max_workers=2) as ex:
        return list(ex.map(hash_payload, payloads))
