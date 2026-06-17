"""Checkpoint chapitre 20 — Reproduire l'exemple `flag download` de
Fluent Python, transposé en `shard download` ML.

Tu écris TROIS versions équivalentes :

1. `download_sequential(names) -> (success_count, failed_names)` :
   appelle `download_shard` en série, accumule.

2. `download_threaded(names, max_workers) -> (success_count, failed_names)` :
   utilise `ThreadPoolExecutor + ex.map` — préserve l'ordre.

3. `download_robust(names, max_workers) -> (success_count, failed_names)` :
   utilise `submit` + `as_completed` + `fut.exception()` pour TRIER
   les succès des erreurs SANS interrompre le batch.

- `download_shard(name: str) -> int` est fournie : sleep + renvoie len(name).
  Lève `RuntimeError` si `name == "BROKEN"`.

Les trois doivent donner le MÊME résultat sur des inputs sans erreur.
La version 3 doit gérer les erreurs proprement (les comptabiliser dans
`failed_names`).
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
    raise NotImplementedError("À implémenter")


def download_threaded(names: list[str], max_workers: int = 4) -> tuple[int, list[str]]:
    raise NotImplementedError("À implémenter")


def download_robust(names: list[str], max_workers: int = 4) -> tuple[int, list[str]]:
    raise NotImplementedError("À implémenter")
