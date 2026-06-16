"""Un restaurant veut un context manager pour réserver une table le temps
d'une commande : flag `reserved = True` à l'entrée, `False` à la sortie.

Implémente `reservation_window(table)` :
- Décorée avec `@contextmanager` (depuis `contextlib`).
- Met `table.reserved = True`.
- `yield table` (ce que l'utilisateur récupère via `as`).
- Au cleanup : `table.reserved = False`.
- Le cleanup doit s'exécuter MÊME si une exception est levée dans le bloc.
"""
from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager


class Table:
    def __init__(self, table_id: str) -> None:
        self.table_id = table_id
        self.reserved: bool = False


@contextmanager
def reservation_window(table: Table) -> Iterator[Table]:
    raise NotImplementedError("À implémenter")
    yield table  # pragma: no cover  # pour que la signature reste un generator
