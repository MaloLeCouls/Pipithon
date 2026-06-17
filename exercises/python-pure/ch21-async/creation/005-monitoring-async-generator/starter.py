"""Ton agent monitoring produit un flux de datapoints (CPU usage, ts...).
Tu veux le consommer paresseusement, en async, avec `async for`. C'est
pile le cas d'usage d'un **async generator** : `async def` + `yield`.

Contrat :

- `async def stream_metrics(values: list[int]) -> AsyncIterator[int]` :
  pour chaque `v` dans `values`, fait `await asyncio.sleep(0)` (céder le
  contrôle) puis `yield v * 2` (datapoint normalisé).
- `async def collect(values: list[int]) -> list[int]` : consomme
  `stream_metrics(values)` via `async for` et accumule dans une liste.

Note : un async generator se reconnaît à `inspect.isasyncgenfunction`.
"""
from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator


async def stream_metrics(values: list[int]) -> AsyncIterator[int]:
    raise NotImplementedError("À implémenter")


async def collect(values: list[int]) -> list[int]:
    raise NotImplementedError("À implémenter")
