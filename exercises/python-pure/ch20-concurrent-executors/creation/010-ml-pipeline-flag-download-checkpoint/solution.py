"""Checkpoint ch.20 — Flag download transposé en shard download.

Choix de design :
- `download_sequential` : naïf, baseline. Sur erreur, on l'attrape et
  on ajoute au compteur. Équivalent du `download_many` v1 de Fluent
  Python.
- `download_threaded` : `ex.map` parallèle, ordre préservé. Problème :
  si UN shard lève, `map` lève à l'iteration sur ce shard — donc on
  perd les résultats suivants. Pour cet exo, `download_threaded` est
  utilisée sur des inputs SANS erreur (tests le garantissent).
- `download_robust` : submit + as_completed + fut.exception() = la
  version production-ready. Aucun shard plantant ne casse les autres.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def download_shard(name: str) -> int:
    time.sleep(0.001)
    if name == "BROKEN":
        raise RuntimeError(f"download failed: {name}")
    return len(name)


def download_sequential(names: list[str]) -> tuple[int, list[str]]:
    success = 0
    failed: list[str] = []
    for name in names:
        try:
            download_shard(name)
            success += 1
        except RuntimeError:
            failed.append(name)
    return success, failed


def download_threaded(names: list[str], max_workers: int = 4) -> tuple[int, list[str]]:
    """Version `ex.map` — suppose qu'il n'y a pas d'erreur dans `names`."""
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        list(ex.map(download_shard, names))
    return len(names), []


def download_robust(names: list[str], max_workers: int = 4) -> tuple[int, list[str]]:
    success = 0
    failed: list[str] = []
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        fut_to_name = {ex.submit(download_shard, n): n for n in names}
        for fut in as_completed(fut_to_name):
            name = fut_to_name[fut]
            if fut.exception() is None:
                success += 1
            else:
                failed.append(name)
    return success, failed
