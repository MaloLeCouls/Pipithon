"""Choix de design :
- `gather(*, return_exceptions=True)` : les exceptions deviennent des items
  dans la liste de résultats. PAS de propagation. C'est le seul comportement
  utilisable en production pour un batch.
- On itère `zip(prompts, results)` pour reconstruire un mapping clair.
- `isinstance(r, BaseException)` : on ne casse pas sur les KeyboardInterrupt
  qui héritent de BaseException et qu'on ne veut PAS swallow. Mais pour un
  batch d'inférence, `Exception` suffirait — on prend BaseException pour
  matcher exactement ce que gather renvoie.
"""
from __future__ import annotations

import asyncio


async def infer(prompt: str) -> int:
    await asyncio.sleep(0)
    if prompt == "":
        raise ValueError("empty prompt")
    return len(prompt)


async def robust_batch(prompts: list[str]) -> list[tuple[str, bool, object]]:
    results = await asyncio.gather(
        *(infer(p) for p in prompts),
        return_exceptions=True,
    )
    out: list[tuple[str, bool, object]] = []
    for prompt, r in zip(prompts, results, strict=True):
        if isinstance(r, BaseException):
            out.append((prompt, False, str(r)))
        else:
            out.append((prompt, True, r))
    return out
