"""Choix de design :
- `fut.exception() is None` distingue succès / échec sans re-raise.
- API change : on renvoie un tuple pour exposer le bilan complet.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def run_one(payload: str) -> int:
    time.sleep(0.001)
    if payload == "BROKEN":
        raise RuntimeError("fail")
    return len(payload)


def run_all(payloads: list[str]) -> tuple[int, int]:
    success = 0
    fail = 0
    with ThreadPoolExecutor(max_workers=4) as ex:
        futures = [ex.submit(run_one, p) for p in payloads]
        for fut in as_completed(futures):
            if fut.exception() is None:
                success += 1
            else:
                fail += 1
    return success, fail
