"""Checkpoint ch.21 — Scheduler async, équivalent `flags_asyncio2.py`.

Choix de design :
- `__aenter__`/`__aexit__` minimaux : pas de ressource lourde à gérer, mais
  on expose la sémantique async-CM pour que l'appelant utilise `async with`.
- `infer_one` prend le sem via `async with self._sem:` — le pattern canonique
  pour borner la concurrence.
- `infer_many` : `gather` lance tout d'un coup ; le SEM régule. C'est la
  symétrie exacte de `flags_asyncio2.py`.
- `as_they_complete` : `create_task` pour transformer les coroutines en
  Tasks (sinon `as_completed` les schedulerait au début mais on perdrait
  l'index), puis `as_completed` pour itérer dans l'ordre de fin.
- L'astuce de l'index : chaque inner task renvoie `(index, n_tokens)` —
  comme `download_one` retourne `(country_code, ...)` dans Fluent Python.
"""
from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator


class LLMScheduler:
    def __init__(self, max_concurrent: int) -> None:
        self._sem = asyncio.Semaphore(max_concurrent)

    async def __aenter__(self) -> "LLMScheduler":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        return None

    async def infer_one(self, prompt: str) -> int:
        async with self._sem:
            await asyncio.sleep(0)
            return len(prompt)

    async def infer_many(self, prompts: list[str]) -> list[int]:
        coros = [self.infer_one(p) for p in prompts]
        return list(await asyncio.gather(*coros))

    async def as_they_complete(self, prompts: list[str]) -> AsyncIterator[tuple[int, int]]:
        async def _indexed(i: int, prompt: str) -> tuple[int, int]:
            n = await self.infer_one(prompt)
            return i, n

        tasks = [asyncio.create_task(_indexed(i, p)) for i, p in enumerate(prompts)]
        for fut in asyncio.as_completed(tasks):
            yield await fut
