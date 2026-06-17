"""Tu calcules des fingerprints CPU-heavy (hash) sur des `Job`s du cluster.
Avec des threads, le GIL bloque le parallélisme. `ProcessPoolExecutor`
spawn de vrais processus → vrai parallélisme.

Contrat :

- `hash_job(payload: str) -> int` est fournie : calcule un hash CPU-heavy
  (boucle d'arithmétique pour simuler).
- `batch_hashes(payloads: list[str]) -> list[int]` :
  - `ProcessPoolExecutor(max_workers=2)` dans un `with`,
  - `ex.map(hash_job, payloads)` (préserve l'ordre),
  - renvoie une `list`.

NB : `hash_job` doit être au TOP LEVEL (déjà le cas) pour être picklable.
Une lambda ou closure échouerait.
"""
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor


def hash_job(payload: str) -> int:
    h = 0
    for c in payload:
        h = (h * 31 + ord(c)) & 0xFFFFFFFF
    # Loop CPU-heavy artificielle pour simuler du calcul long
    for _ in range(10_000):
        h = (h * 7 + 1) & 0xFFFFFFFF
    return h


def batch_hashes(payloads: list[str]) -> list[int]:
    raise NotImplementedError("À implémenter")
