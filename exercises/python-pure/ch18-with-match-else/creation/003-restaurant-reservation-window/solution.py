"""Choix de design :
- `@contextmanager` transforme un générateur (1 seul `yield`) en context
  manager. Setup avant le yield, cleanup après. Forme la plus concise
  quand le state à gérer est simple.
- Le `try/finally` autour du yield garantit le cleanup même si une
  exception remonte du bloc `with`. Sans lui, le cleanup ne tournerait
  pas et `table.reserved` resterait à True.
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
    table.reserved = True
    try:
        yield table
    finally:
        table.reserved = False
