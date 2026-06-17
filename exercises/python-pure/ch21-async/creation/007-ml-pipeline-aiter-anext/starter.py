"""Avant les async generators, on écrivait le protocole à la main avec
`__aiter__` + `__anext__`. C'est verbeux, mais nécessaire à comprendre
pour lire le code legacy d'async I/O (ex. aiohttp, aiosqlite).

Contrat — classe `BatchStream(batches: list[list[int]])` :
- `__aiter__(self) -> "BatchStream"` (SYNC, pas `async`) : retourne `self`.
- `__anext__(self) -> list[int]` (`async def`) : renvoie le prochain batch,
  ou lève `StopAsyncIteration` si épuisé.

Astuce : maintiens un index `_i` ; au début, `_i = 0`. À chaque `__anext__`,
si `_i >= len(self._batches)` → `raise StopAsyncIteration`, sinon récupère
`b = self._batches[self._i]`, incrémente `_i`, renvoie `b`.

Bonus : `await asyncio.sleep(0)` avant le `return` pour que ce soit
réellement « cédant ». Pas obligatoire au sens du protocole.
"""
from __future__ import annotations


class BatchStream:
    def __init__(self, batches: list[list[int]]) -> None:
        self._batches = batches
        self._i = 0

    def __aiter__(self) -> "BatchStream":
        raise NotImplementedError("À implémenter")

    async def __anext__(self) -> list[int]:
        raise NotImplementedError("À implémenter")
