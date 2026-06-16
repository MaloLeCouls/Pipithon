"""Choix de design :
- `ExitStack` remplace la récursion : on empile les context managers dans
  une boucle, et ils sont tous fermés (LIFO) à la sortie du with externe.
- Plus de profondeur d'appel proportionnelle à N. Plus lisible : un seul
  niveau d'indentation pour le `work`.
"""
from __future__ import annotations

from collections.abc import Callable, Iterator
from contextlib import ExitStack, contextmanager


class FakeCache:
    def __init__(self, name: str) -> None:
        self.name = name
        self.open: bool = False


@contextmanager
def cache_scope(cache: FakeCache) -> Iterator[FakeCache]:
    cache.open = True
    try:
        yield cache
    finally:
        cache.open = False


def with_all_caches(caches: list[FakeCache], work: Callable[[list[FakeCache]], None]) -> None:
    with ExitStack() as stack:
        opened = [stack.enter_context(cache_scope(c)) for c in caches]
        work(opened)
