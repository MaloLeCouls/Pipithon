"""Un dispatcher de tickets répartit du travail sur N workers. Chaque worker
maintient sa propre file `pending`.

BUG : quand on appelle `make_workers(3)`, les trois workers semblent partager
le même buffer. Si on enqueue un ticket sur worker[0], il apparaît sur
worker[1] et worker[2].

Corrige `make_workers` (la fonction qui CRÉE les workers).

Indice : regarde comment `Worker.__init__` reçoit `pending`.
"""
from __future__ import annotations


class Worker:
    def __init__(self, worker_id: int, pending: list[str] = []) -> None:  # noqa: B006
        self.worker_id = worker_id
        self.pending = pending

    def enqueue(self, ticket: str) -> None:
        self.pending.append(ticket)


def make_workers(n: int) -> list[Worker]:
    return [Worker(i) for i in range(n)]
