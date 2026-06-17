"""Tu télécharges N shards d'un dataset. Chaque shard prend un temps
différent : tu veux les traiter dans l'ordre **d'arrivée**, pas dans
l'ordre d'appel. C'est exactement le boulot de `asyncio.as_completed`.

Contrat :

- `async def load_shard(index: int, delay: float) -> int` est fournie :
  attend `delay` secondes (simulé), puis renvoie `index`.
- `async def order_by_completion(delays: list[float]) -> list[int]` :
  lance toutes les `load_shard(i, delays[i])` en parallèle ; renvoie la
  liste des `index` dans l'ordre où les shards finissent.

Exemple : `delays = [0.03, 0.01, 0.02]` → on attend `[1, 2, 0]` (le shard
d'index 1 a le plus petit délai, donc finit en premier).

Garde des délais courts pour ne pas faire timeout les tests.
"""
from __future__ import annotations

import asyncio


async def load_shard(index: int, delay: float) -> int:
    await asyncio.sleep(delay)
    return index


async def order_by_completion(delays: list[float]) -> list[int]:
    raise NotImplementedError("À implémenter")
