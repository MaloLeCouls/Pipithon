"""Cette coroutine `aggregate` fait croire qu'elle est async (elle est
`async def`)... mais elle insère un `time.sleep(0.001)` entre chaque
datapoint. Résultat : pendant qu'elle « calcule », **AUCUNE autre
coroutine** ne peut tourner sur la boucle. C'est exactement ce que le
chapitre interdit.

Refactore-la pour :
- supprimer tout usage de `time.sleep`,
- garder le même calcul (somme des datapoints),
- céder proprement le contrôle via `await asyncio.sleep(0)`.

Le test vérifie : (a) le comportement (somme correcte), (b) absence
syntaxique de `time.sleep` dans `aggregate`.
"""
from __future__ import annotations

import asyncio
import time


async def aggregate(points: list[int]) -> int:
    total = 0
    for p in points:
        # Anti-pattern : time.sleep dans une coroutine -> bloque la boucle.
        time.sleep(0.001)
        total += p
    return total
