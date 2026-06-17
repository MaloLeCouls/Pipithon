"""Choix de design :
- `{future: id}` pour retrouver l'origine de chaque futur (vs ordre).
- `fut.exception()` rend l'exception SANS la lever — on triage.
- On stocke les ids dans (ok, failed) selon le résultat.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def deliver_one(tracking_id: str) -> str:
    time.sleep(0.001)
    if tracking_id.startswith("BAD-"):
        raise ValueError(f"refused: {tracking_id}")
    return f"delivered:{tracking_id}"


def deliver_all(ids: list[str]) -> tuple[list[str], list[str]]:
    ok: list[str] = []
    failed: list[str] = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        fut_to_id = {ex.submit(deliver_one, tid): tid for tid in ids}
        for fut in as_completed(fut_to_id):
            tid = fut_to_id[fut]
            if fut.exception() is None:
                ok.append(tid)
            else:
                failed.append(tid)
    return ok, failed
