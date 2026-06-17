"""Tu interroges un service de tracking pour N colis. Plutôt que de
faire N appels en série, soumets-les en parallèle dans un pool de
threads (I/O bound, donc threads OK malgré le GIL).

Contrat :

- `track_one(tracking_id: str) -> str` est fournie (stub bloquant simulé
  avec `time.sleep(0.001)` + renvoie un statut).
- `track_all(ids: list[str]) -> list[str]` :
  - utilise `ThreadPoolExecutor(max_workers=8)` dans un `with`,
  - soumet chaque id via `submit`,
  - récupère les résultats via `Future.result()` dans l'ORDRE DES IDS.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor


def track_one(tracking_id: str) -> str:
    time.sleep(0.001)
    return f"shipped:{tracking_id}"


def track_all(ids: list[str]) -> list[str]:
    raise NotImplementedError("À implémenter")
