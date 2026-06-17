"""Tu as N probes de monitoring à interroger. Sans async, tu les fais en
série (et la latence totale = somme des latences). Avec `asyncio.gather`,
tu les lances en parallèle (latence totale ≈ max).

Contrat :

- `async def probe(name: str) -> int` est fournie : renvoie une valeur fake.
- `async def sample_all(names: list[str]) -> list[int]` : appelle `probe(n)`
  pour chaque `n`, EN PARALLÈLE via `asyncio.gather`, et renvoie la liste
  des valeurs **dans l'ordre des `names`**.

Bonus pédagogique : si `names` est vide, renvoie `[]` (gather sur 0 coros).
"""
from __future__ import annotations

import asyncio


async def probe(name: str) -> int:
    """Stub : I/O simulé, renvoie len(name) comme « valeur de métrique »."""
    await asyncio.sleep(0)
    return len(name)


async def sample_all(names: list[str]) -> list[int]:
    raise NotImplementedError("À implémenter")
