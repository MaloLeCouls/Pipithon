"""Bug : `Worker.__init__(self, ..., pending=[])` partage UN SEUL `[]` entre
toutes les instances qui n'en fournissent pas explicitement. Le `[i for i in
range(n)]` crée n workers qui pointent tous vers la même liste.

Fix chirurgical : pattern sentinelle dans __init__.

Alternative équivalente : `Worker(i, pending=[])` dans make_workers (force
une liste fraîche par appel). On retient la sentinelle dans __init__ car elle
protège *tous* les appels, pas seulement ceux de make_workers.
"""
from __future__ import annotations


class Worker:
    def __init__(self, worker_id: int, pending: list[str] | None = None) -> None:
        self.worker_id = worker_id
        self.pending = pending if pending is not None else []

    def enqueue(self, ticket: str) -> None:
        self.pending.append(ticket)


def make_workers(n: int) -> list[Worker]:
    return [Worker(i) for i in range(n)]
