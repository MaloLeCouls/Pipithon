"""Checkpoint chapitre 21 — Reproduire `blogdom`/`flags_asyncio2.py` de
Fluent Python, en version `llm-serving`.

Tu écris un mini-scheduler d'inférence qui :

1. Est un **async context manager** (`async with LLMScheduler(k) as sched:`).
2. Régule la concurrence via un `asyncio.Semaphore(max_concurrent)` interne.
3. Expose deux méthodes :
   - `await sched.infer_many(prompts)` : renvoie la liste des nb-tokens dans
     l'**ordre des prompts** (utilise `gather`).
   - `sched.as_they_complete(prompts)` : **async generator** qui yield des
     tuples `(index, n_tokens)` dans l'**ordre de fin** (utilise
     `as_completed` + `create_task`).

Contrat détaillé :

- Classe `LLMScheduler(max_concurrent: int)` :
  - attribut `self._sem = asyncio.Semaphore(max_concurrent)`.
  - `async __aenter__(self) -> "LLMScheduler"` : renvoie self.
  - `async __aexit__(self, exc_type, exc, tb) -> None` : renvoie None.
  - `async def infer_one(self, prompt: str) -> int` :
    `async with self._sem: await asyncio.sleep(0); return len(prompt)`.
  - `async def infer_many(self, prompts: list[str]) -> list[int]` :
    gather sur `self.infer_one(p)` pour chaque p, retour en list dans l'ordre.
  - `async def as_they_complete(self, prompts: list[str])` (async generator) :
    crée une Task par prompt qui renvoie `(index, n_tokens)`, itère via
    `asyncio.as_completed(tasks)`, yield chaque `(index, n_tokens)`.

Toutes les opérations passent par le sem (donc respectent `max_concurrent`).
"""
from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator


class LLMScheduler:
    def __init__(self, max_concurrent: int) -> None:
        self._sem = asyncio.Semaphore(max_concurrent)

    async def __aenter__(self) -> "LLMScheduler":
        raise NotImplementedError("À implémenter")

    async def __aexit__(self, exc_type, exc, tb) -> None:
        raise NotImplementedError("À implémenter")

    async def infer_one(self, prompt: str) -> int:
        raise NotImplementedError("À implémenter")

    async def infer_many(self, prompts: list[str]) -> list[int]:
        raise NotImplementedError("À implémenter")

    async def as_they_complete(self, prompts: list[str]) -> AsyncIterator[tuple[int, int]]:
        raise NotImplementedError("À implémenter")
