"""Choix de design :
- `__aiter__` est sync : c'est la spec — il retourne un async iterator
  (ici `self`), pas une coroutine.
- `__anext__` est async : il PEUT awaiter un I/O réel ici (on simule via
  `asyncio.sleep(0)` pour bien céder le contrôle).
- `StopAsyncIteration` (pas `StopIteration`) : c'est l'exception attendue
  par `async for`.
"""
from __future__ import annotations

import asyncio


class BatchStream:
    def __init__(self, batches: list[list[int]]) -> None:
        self._batches = batches
        self._i = 0

    def __aiter__(self) -> "BatchStream":
        return self

    async def __anext__(self) -> list[int]:
        if self._i >= len(self._batches):
            raise StopAsyncIteration
        await asyncio.sleep(0)
        b = self._batches[self._i]
        self._i += 1
        return b
