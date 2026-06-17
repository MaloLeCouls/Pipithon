"""Cette routine acquiert un lease GPU, fait du boulot, et release dans
un `try/finally`. Ça marche. Mais c'est verbeux et fragile (oublier le
finally = leak). Refactore en async context manager.

Contrat demandé :

- Crée une classe `GPULease(node: str, events: list[str])` avec :
  - `async __aenter__(self)` : append `f"acquire:{self.node}"` dans events, return self.
  - `async __aexit__(self, exc_type, exc, tb)` : append `f"release:{self.node}"` dans events. Return None.
- Réécris `run_job(node, events, work)` pour utiliser `async with GPULease(...) as lease:`
  au lieu de `try/finally`. Le `work` est une coroutine que tu await dans le bloc.

`run_job` ne doit PLUS contenir de `try`/`finally` au niveau syntaxique.
"""
from __future__ import annotations

from collections.abc import Awaitable


async def _acquire(node: str, events: list[str]) -> None:
    events.append(f"acquire:{node}")


async def _release(node: str, events: list[str]) -> None:
    events.append(f"release:{node}")


async def run_job(node: str, events: list[str], work: Awaitable[None]) -> None:
    # Anti-pattern : acquire/release manuel. Symétrise via __aenter__/__aexit__.
    await _acquire(node, events)
    try:
        await work
    finally:
        await _release(node, events)
