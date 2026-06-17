"""Ton serveur d'inférence accepte N requêtes utilisateurs en parallèle,
mais ton GPU ne peut en traiter que `max_concurrent` à la fois. Si tu
laisses `gather` lancer les 100 requêtes d'un coup, l'OOM te punit.
La solution canonique : `asyncio.Semaphore(max_concurrent)`.

Contrat :

- `async def infer(prompt: str, sem: asyncio.Semaphore, tracker: list) -> int` :
  prend le sem avec `async with sem:` ; pendant qu'elle le tient, elle
  s'enregistre dans `tracker` (append/pop) pour qu'on puisse mesurer le pic
  de concurrence ; renvoie `len(prompt)` (fake token count).
- `async def serve(prompts: list[str], max_concurrent: int) -> list[int]` :
  lance toutes les inférences en parallèle via gather, mais régule avec
  un `Semaphore(max_concurrent)`. Renvoie les résultats dans l'ordre des
  prompts. Crée `tracker` localement et utilise-le pour les tests.

Le tracker est interne à `serve` ; il n'est pas renvoyé. Le test va
plutôt observer le pic via un Semaphore espion (cf. tests).
"""
from __future__ import annotations

import asyncio


async def infer(prompt: str, sem: asyncio.Semaphore, tracker: list[int]) -> int:
    raise NotImplementedError("À implémenter")


async def serve(prompts: list[str], max_concurrent: int) -> list[int]:
    raise NotImplementedError("À implémenter")
