"""Choix de design :
- `asyncio.as_completed(coros)` renvoie un itérable de futures dans l'ordre
  de TERMINAISON. C'est exactement ce qu'on veut : on traite chaque shard
  dès qu'il est prêt, sans attendre le plus lent.
- Pas besoin de wrapper en `create_task` : `as_completed` accepte les
  coroutines directement et les schedule pour nous.
- Pour préserver l'index, chaque coroutine renvoie son index propre — c'est
  l'astuce canonique du chapitre.
"""
from __future__ import annotations

import asyncio


async def load_shard(index: int, delay: float) -> int:
    await asyncio.sleep(delay)
    return index


async def order_by_completion(delays: list[float]) -> list[int]:
    coros = [load_shard(i, d) for i, d in enumerate(delays)]
    order: list[int] = []
    for fut in asyncio.as_completed(coros):
        order.append(await fut)
    return order
