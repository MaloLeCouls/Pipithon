"""Un async iterator écrit à la main : verbeux, sujet aux bugs (le
StopAsyncIteration, l'index, etc.). Remplace-le par une **fonction**
`async def stream_batches(batches) -> AsyncIterator[list[int]]` avec
`yield`. Beaucoup plus court.

Contrat : `async for b in stream_batches(batches)` doit produire les mêmes
batches dans le même ordre.

⚠️ La signature attendue est une FONCTION (pas une classe). Le test va
vérifier `inspect.isasyncgenfunction(stream_batches)`.
"""
from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator


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


# À implémenter : la version async generator function.
# Supprime la classe ci-dessus si tu veux (le test n'en a pas besoin).
async def stream_batches(batches: list[list[int]]) -> AsyncIterator[list[int]]:
    raise NotImplementedError("À implémenter")
