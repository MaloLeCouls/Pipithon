"""Ton dispatcher livre N colis indépendamment. La version actuelle fait
les `await ship(p)` EN SÉRIE — 100 colis = 100 latences cumulées. Refactore
en parallèle avec `asyncio.gather`.

Contrat :
- `ship(package: str) -> str` reste inchangée (déjà async).
- `dispatch_all(packages)` doit renvoyer la MÊME liste de statuts, mais
  en lançant les `ship` en parallèle via `asyncio.gather`.

Le test vérifie aussi qu'il n'y a PLUS de `await` à l'intérieur d'une
boucle for/while (signature d'awaits séquentiels).
"""
from __future__ import annotations

import asyncio


async def ship(package: str) -> str:
    await asyncio.sleep(0)
    return f"shipped:{package}"


async def dispatch_all(packages: list[str]) -> list[str]:
    # Anti-pattern : await dans une boucle, donc séquentiel.
    results: list[str] = []
    for p in packages:
        status = await ship(p)
        results.append(status)
    return results
