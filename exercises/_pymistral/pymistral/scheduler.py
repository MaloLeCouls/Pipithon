"""Scheduler — FIFO trivial. Chapitres 12 (sequences) & 19-21 (concurrence).

Une file de Requests en attente, `next_batch` pop le préfixe. Pas de priorité,
pas de continuous batching « pour de vrai » — l'exo continuous-batching du
ch19+ enrichira ça.
"""
from __future__ import annotations

from collections import deque
from collections.abc import Iterable

from pymistral.batching import BatchedRequests, Request


class Scheduler:
    """File FIFO de Requests, batch poppé par `next_batch`."""

    def __init__(self, initial: Iterable[Request] | None = None) -> None:
        self._queue: deque[Request] = deque(initial or [])

    def submit(self, request: Request) -> None:
        self._queue.append(request)

    def pending(self) -> int:
        return len(self._queue)

    def next_batch(self, max_batch_size: int = 8) -> BatchedRequests:
        if max_batch_size <= 0:
            raise ValueError(f"max_batch_size must be > 0, got {max_batch_size}")
        taken: list[Request] = []
        for _ in range(min(max_batch_size, len(self._queue))):
            taken.append(self._queue.popleft())
        return BatchedRequests(taken)

    def __len__(self) -> int:
        return len(self._queue)

    def __repr__(self) -> str:
        return f"Scheduler(pending={len(self)})"
