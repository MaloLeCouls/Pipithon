"""Choix de design :
- `async with sem:` : pythonique pour acquire/release. Pas de try/finally manuel.
- `tracker.append(1)` à l'entrée puis `pop()` à la sortie : permet aux tests
  d'observer le pic de concurrence (`max(tracker_max_observed)`).
- Le `await asyncio.sleep(0)` cède le contrôle pour laisser d'autres coros
  acquérir le sem — sinon on enchaîne TOUT en série (un seul thread Python).
- `gather` lance tout d'un coup ; c'est le SEM qui régule, comme dans
  Fluent Python `flags_asyncio2.py`.
"""
from __future__ import annotations

import asyncio


async def infer(prompt: str, sem: asyncio.Semaphore, tracker: list[int]) -> int:
    async with sem:
        tracker.append(1)
        try:
            await asyncio.sleep(0)
            return len(prompt)
        finally:
            tracker.pop()


async def serve(prompts: list[str], max_concurrent: int) -> list[int]:
    sem = asyncio.Semaphore(max_concurrent)
    tracker: list[int] = []
    coros = [infer(p, sem, tracker) for p in prompts]
    return list(await asyncio.gather(*coros))
