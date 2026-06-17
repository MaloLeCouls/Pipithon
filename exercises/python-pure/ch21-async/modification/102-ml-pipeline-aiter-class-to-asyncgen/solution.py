"""Choix de design :
- Une seule fn `async def` + un `yield` — le compilateur génère le protocole
  `__aiter__`/`__anext__` pour nous. 3 lignes au lieu d'une classe entière.
- Le `await asyncio.sleep(0)` reste : on cède le contrôle entre chaque
  batch, comportement IDENTIQUE à la classe d'origine.
"""
from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator


async def stream_batches(batches: list[list[int]]) -> AsyncIterator[list[int]]:
    for b in batches:
        await asyncio.sleep(0)
        yield b
