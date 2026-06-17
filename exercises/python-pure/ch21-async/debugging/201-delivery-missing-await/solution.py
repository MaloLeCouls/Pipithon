"""Fix : ajouter l'`await`. La coroutine `ship(p)` est ainsi exécutée et
le résultat (`str`) est stocké dans `results`.

Note : ici on garde la boucle séquentielle volontairement — c'est l'exo
201 qui isole UN bug à la fois. Le passage à `gather` est l'objet de
l'exo `modification` 101.
"""
from __future__ import annotations

import asyncio


async def ship(package: str) -> str:
    await asyncio.sleep(0)
    return f"shipped:{package}"


async def dispatch_all(packages: list[str]) -> list[str]:
    results: list[str] = []
    for p in packages:
        status = await ship(p)
        results.append(status)
    return results
