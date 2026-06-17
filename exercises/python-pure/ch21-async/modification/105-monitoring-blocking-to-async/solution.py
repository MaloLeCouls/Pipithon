"""Choix de design :
- `await asyncio.sleep(0)` cède le contrôle SANS bloquer la boucle. C'est
  le standby canonique pour signaler « je suis prêt à passer la main ».
- Plus d'import `time` : on ne s'autorise PAS un seul outil qui bloque.
"""
from __future__ import annotations

import asyncio


async def aggregate(points: list[int]) -> int:
    total = 0
    for p in points:
        await asyncio.sleep(0)
        total += p
    return total
