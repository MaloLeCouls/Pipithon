"""Choix de design :
- `@contextmanager` rend visible que ce CM est *un setup/cleanup symétrique
  sans état persistant* — pas besoin d'une classe.
- La classe disparaît : moins de code à maintenir, même contrat.
- `try/finally` autour du yield = garantie de cleanup sur exception, exactement
  ce que faisait `__exit__` toujours appelé par le `with`.
"""
from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager


class GPU:
    def __init__(self, gpu_id: str) -> None:
        self.gpu_id = gpu_id
        self.status: str = "free"


@contextmanager
def gpu_lock(gpu: GPU) -> Iterator[GPU]:
    gpu.status = "in_use"
    try:
        yield gpu
    finally:
        gpu.status = "free"
