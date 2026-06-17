"""Cette version de `batch` traite N prompts mais explose si UN seul plante
(le `gather` lève à la première erreur). C'est inacceptable en prod.

Refactore-la pour :
- ajouter `return_exceptions=True` à `gather`,
- remplacer chaque exception par `None` dans le résultat final.

L'API publique de `batch` reste : `list[int | None]` (None = erreur).
"""
from __future__ import annotations

import asyncio


async def infer(prompt: str) -> int:
    await asyncio.sleep(0)
    if prompt == "":
        raise ValueError("empty prompt")
    return len(prompt)


async def batch(prompts: list[str]) -> list[int | None]:
    # Anti-pattern : un seul `""` dans `prompts` fait sauter tout le batch.
    results = await asyncio.gather(*(infer(p) for p in prompts))
    return list(results)
