"""Le module llm-serving veut acquérir N caches d'inférence à la fois, en
respectant LIFO sur le cleanup. Aujourd'hui c'est écrit *récursivement*
avec un `with` imbriqué (ça marche pour 2-3 caches, ça pète au-delà à cause
de la profondeur d'appels — et c'est moche à lire).

Refactor `with_all_caches(caches, work)` :
- Reçoit une liste de `KVCache`-like (objet avec `clear()`).
- Reçoit un callable `work(caches_list)` qui prend la liste des caches
  ouverts.
- À l'entrée : ouvre chaque cache via `cache_scope(cache)` (déjà fourni).
- À la sortie : tous les scopes sont refermés en ordre inverse, exception
  ou pas.

⚠️ Utilise `contextlib.ExitStack` — pas de récursion, pas de `with`
imbriqués manuels."""
from __future__ import annotations

from collections.abc import Callable, Iterator
from contextlib import contextmanager


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
    # Implémentation actuelle : récursive avec des `with` imbriqués via une
    # fonction interne. Pas de problème à 2-3 niveaux, mais ça grimpe vite.
    def _recurse(remaining: list[FakeCache], opened: list[FakeCache]) -> None:
        if not remaining:
            work(opened)
            return
        head, *tail = remaining
        with cache_scope(head) as h:
            _recurse(tail, opened + [h])

    _recurse(caches, [])
