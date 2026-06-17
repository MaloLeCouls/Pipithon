"""Ton serveur d'inférence traite 100 prompts en batch via `gather`.
Si UN seul plante (ex. prompt vide → `ValueError`), gather lève et annule
tout — tu perds 99 résultats valides. Mauvais business.

La parade : `asyncio.gather(*coros, return_exceptions=True)`. Les
exceptions sont retournées comme items normaux ; à toi de les emballer
proprement.

Contrat :

- `async def infer(prompt: str) -> int` est fournie : renvoie `len(prompt)`,
  mais lève `ValueError("empty prompt")` si `prompt == ""`.
- `async def robust_batch(prompts: list[str]) -> list[tuple[str, bool, object]]` :
  lance toutes les infer en parallèle avec `return_exceptions=True`.
  Pour chaque prompt, renvoie `(prompt, ok, value)` où :
    - `(prompt, True, n_tokens)` si l'inférence a réussi.
    - `(prompt, False, str(exc))` si elle a planté.
"""
from __future__ import annotations

import asyncio


async def infer(prompt: str) -> int:
    await asyncio.sleep(0)
    if prompt == "":
        raise ValueError("empty prompt")
    return len(prompt)


async def robust_batch(prompts: list[str]) -> list[tuple[str, bool, object]]:
    raise NotImplementedError("À implémenter")
