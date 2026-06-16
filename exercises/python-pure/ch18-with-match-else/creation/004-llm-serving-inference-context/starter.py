"""Une session d'inférence doit (1) partir d'un KV cache propre, (2)
garantir qu'on n'oublie pas de le vider à la sortie — *même* si le modèle
plante au milieu d'une génération. Pattern parfait pour un context manager.

Implémente `inference_context(cache)` :
- Décoré avec `@contextmanager`.
- Avant yield : vide le cache (`cache.clear()`).
- yield le cache pour qu'il soit utilisable via `as`.
- Après yield (en finally) : re-vide le cache.
- Le cleanup doit s'exécuter même en cas d'exception dans le bloc.
"""
from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager

from pymistral import KVCache


@contextmanager
def inference_context(cache: KVCache) -> Iterator[KVCache]:
    raise NotImplementedError("À implémenter")
    yield cache  # pragma: no cover  # garde la signature de generator
