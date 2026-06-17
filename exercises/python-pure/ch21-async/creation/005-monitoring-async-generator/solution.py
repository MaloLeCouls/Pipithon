"""Choix de design :
- `async def` + `yield` = async generator function. Pas besoin d'écrire
  `__aiter__`/`__anext__` à la main : Python le génère pour nous.
- Le `await asyncio.sleep(0)` entre `yield` est volontaire : c'est ce qui
  rend la fonction utilisable comme un VRAI flux async (céder, reprendre).
- Côté consommateur : `async for ... in stream(...)` — pas de `next()`,
  pas de boucle while + try/except StopAsyncIteration.
"""
from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator


async def stream_metrics(values: list[int]) -> AsyncIterator[int]:
    for v in values:
        await asyncio.sleep(0)
        yield v * 2


async def collect(values: list[int]) -> list[int]:
    out: list[int] = []
    async for dp in stream_metrics(values):
        out.append(dp)
    return out
