"""Choix de design :
- `submit` chacun, puis `as_completed` : on récupère dans l'ordre où
  les jobs FINISSENT, pas l'ordre où on les a soumis.
- Le résultat est explicitement un `list[tuple[int, int]]`, ordre = fin.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def run_job(job_id: int, runtime: float) -> tuple[int, int]:
    time.sleep(runtime)
    return job_id, int(runtime * 1000)


def report(jobs: list[tuple[int, float]]) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        futures = [ex.submit(run_job, jid, rt) for jid, rt in jobs]
        for fut in as_completed(futures):
            out.append(fut.result())
    return out
