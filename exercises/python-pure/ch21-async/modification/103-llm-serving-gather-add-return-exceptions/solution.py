"""Choix de design :
- `return_exceptions=True` : les erreurs deviennent des items dans la liste.
- Compréhension qui remplace tout BaseException par None — l'API publique
  reste `list[int | None]`. L'appelant gère le None comme un opt-out.
"""
from __future__ import annotations

import asyncio


async def infer(prompt: str) -> int:
    await asyncio.sleep(0)
    if prompt == "":
        raise ValueError("empty prompt")
    return len(prompt)


async def batch(prompts: list[str]) -> list[int | None]:
    results = await asyncio.gather(
        *(infer(p) for p in prompts),
        return_exceptions=True,
    )
    return [None if isinstance(r, BaseException) else r for r in results]
