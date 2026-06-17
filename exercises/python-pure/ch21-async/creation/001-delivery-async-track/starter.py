"""Premier contact avec `async def` / `await`.

Tu maintiens un service de tracking de colis. La fonction `lookup(tracking_id)`
interroge un backend (simulé ici par `_fake_query`, déjà fourni). Tu dois la
rendre **asynchrone** pour qu'un appelant puisse en lancer 1000 sans bloquer.

Contrat :

- `async def lookup(tracking_id: str) -> str` : prend un id de colis, fait un
  `await _fake_query(tracking_id)` (déjà async), renvoie le statut renvoyé.
- Si `tracking_id` est vide, renvoie `"invalid"` SANS faire d'await (raccourci
  de validation, classique).

`_fake_query` est déjà fournie en bas : ne la modifie pas.
"""
from __future__ import annotations

import asyncio


async def _fake_query(tracking_id: str) -> str:
    """Stub : simule un I/O en cédant le contrôle puis renvoie un statut."""
    await asyncio.sleep(0)
    if tracking_id.startswith("TRK-"):
        return "delivered"
    return "unknown"


async def lookup(tracking_id: str) -> str:
    raise NotImplementedError("À implémenter")
