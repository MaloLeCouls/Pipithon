"""Choix de design :
- `@contextmanager` : la forme idiomatique pour ce pattern (state simple,
  setup/cleanup symétriques).
- `try/finally` autour du yield : c'est LA garantie que le cleanup tourne
  même si la génération crashe (vital pour ne pas leaker des tokens entre
  requêtes successives).
- On `yield cache` pour permettre `with inference_context(cache) as c: ...`
  (et taper directement sur `c`).
"""
from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager

from pymistral import KVCache


@contextmanager
def inference_context(cache: KVCache) -> Iterator[KVCache]:
    cache.clear()
    try:
        yield cache
    finally:
        cache.clear()
