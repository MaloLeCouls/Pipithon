"""Choix de design :
- `__aenter__` fait l'acquire et renvoie le lease (pratique pour
  l'appelant qui peut accéder à `lease.node`).
- `__aexit__` fait le release — Python garantit son appel même sur
  exception, on n'a plus besoin du `try/finally`.
- `__aexit__` renvoie None (= False) : on laisse remonter les exceptions.
"""
from __future__ import annotations

from collections.abc import Awaitable


class GPULease:
    def __init__(self, node: str, events: list[str]) -> None:
        self.node = node
        self.events = events

    async def __aenter__(self) -> "GPULease":
        self.events.append(f"acquire:{self.node}")
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        self.events.append(f"release:{self.node}")
        return None


async def run_job(node: str, events: list[str], work: Awaitable[None]) -> None:
    async with GPULease(node, events):
        await work
