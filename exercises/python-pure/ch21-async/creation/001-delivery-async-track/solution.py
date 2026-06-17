"""Choix de design :
- `async def lookup` : on déclare une coroutine — son corps ne s'exécute qu'au
  premier `await`/`asyncio.run`.
- Court-circuit `invalid` SANS await : pas besoin de céder le contrôle pour un
  cas d'erreur trivial. C'est légal et même recommandé.
- Sinon `await _fake_query(...)` : on récupère la valeur résolue de la
  coroutine interne.
"""
from __future__ import annotations

import asyncio


async def _fake_query(tracking_id: str) -> str:
    await asyncio.sleep(0)
    if tracking_id.startswith("TRK-"):
        return "delivered"
    return "unknown"


async def lookup(tracking_id: str) -> str:
    if not tracking_id:
        return "invalid"
    return await _fake_query(tracking_id)
