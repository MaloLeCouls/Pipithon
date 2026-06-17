"""Tu lives N colis ; certains plantent (`ValueError: refused`).
Tu veux savoir quels ont marché et quels ont planté, SANS qu'une seule
erreur fasse tout exploser.

`Future.exception()` rend l'exception SANS la re-raise — parfait
pour le triage.

Contrat :

- `deliver_one(tracking_id: str) -> str` est fournie ; lève `ValueError`
  si l'id commence par `"BAD-"`.
- `deliver_all(ids: list[str]) -> tuple[list[str], list[str]]` :
  renvoie `(ok_ids, failed_ids)` selon `fut.exception() is None`.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor


def deliver_one(tracking_id: str) -> str:
    time.sleep(0.001)
    if tracking_id.startswith("BAD-"):
        raise ValueError(f"refused: {tracking_id}")
    return f"delivered:{tracking_id}"


def deliver_all(ids: list[str]) -> tuple[list[str], list[str]]:
    raise NotImplementedError("À implémenter")
