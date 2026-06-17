"""Choix de design :
- Compréhension de liste pour créer les coroutines, puis `gather(*coros)`.
- `gather` préserve l'ordre d'appel — utile quand chaque résultat correspond
  à une entrée précise.
- Pas besoin de `return_exceptions` ici (les probes ne lèvent pas), ce sera
  l'objet de l'exo robuste plus loin (009).
"""
from __future__ import annotations

import asyncio


async def probe(name: str) -> int:
    await asyncio.sleep(0)
    return len(name)


async def sample_all(names: list[str]) -> list[int]:
    coros = [probe(name) for name in names]
    return list(await asyncio.gather(*coros))
