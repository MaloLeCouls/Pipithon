"""Choix de design :
- Compréhension de liste qui CONSTRUIT les coroutines (sans await), puis
  un seul `await gather(*coros)` qui les lance toutes en parallèle.
- gather préserve l'ordre des packages dans le résultat.
"""
from __future__ import annotations

import asyncio


async def ship(package: str) -> str:
    await asyncio.sleep(0)
    return f"shipped:{package}"


async def dispatch_all(packages: list[str]) -> list[str]:
    coros = [ship(p) for p in packages]
    return list(await asyncio.gather(*coros))
