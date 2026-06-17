"""Fix : remplacer `asyncio.run(_tokenize(prompt))` par `await _tokenize(prompt)`.
Une coroutine s'attend à être conduite par UN loop, pas à en créer un nouveau
à chaque appel.

Règle : `asyncio.run` n'apparaît qu'au TOP LEVEL (entrypoint script).
Partout ailleurs, c'est `await ...`.
"""
from __future__ import annotations

import asyncio


async def _tokenize(prompt: str) -> int:
    await asyncio.sleep(0)
    return len(prompt)


async def serve_one(prompt: str) -> int:
    return await _tokenize(prompt)
