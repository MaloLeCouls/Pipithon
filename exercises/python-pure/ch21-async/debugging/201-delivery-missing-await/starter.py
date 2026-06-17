"""Ce dispatcher renvoie systématiquement des objets `coroutine` au lieu
des statuts attendus. Le test du comportement échoue avec « expected str,
got coroutine ». Cherche pourquoi.

Indices :
- `ship` est `async def`.
- Quand tu appelles `ship(p)` sans rien devant, tu obtiens une coroutine
  (objet, pas valeur).
- Tu dois la **réveiller** pour récupérer le résultat.
"""
from __future__ import annotations

import asyncio


async def ship(package: str) -> str:
    await asyncio.sleep(0)
    return f"shipped:{package}"


async def dispatch_all(packages: list[str]) -> list[str]:
    results: list[str] = []
    for p in packages:
        # BUG : on a oublié `await` -> on stocke la coroutine, pas le résultat.
        status = ship(p)
        results.append(status)
    return results
