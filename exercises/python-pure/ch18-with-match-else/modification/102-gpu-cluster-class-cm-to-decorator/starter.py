"""La classe `GPULockCM` marche, mais elle est inutilement verbeuse : 3
dunders pour ce qui tient en 3 lignes avec `@contextmanager`.

Refactor :
- Remplace `GPULockCM` par une fonction `gpu_lock(gpu)` décorée
  `@contextmanager`, équivalente.
- **Supprime entièrement** la classe `GPULockCM`.

Le test attend `gpu_lock(gpu)` utilisable directement dans un `with`."""
from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager


class GPU:
    def __init__(self, gpu_id: str) -> None:
        self.gpu_id = gpu_id
        self.status: str = "free"


class GPULockCM:
    def __init__(self, gpu: GPU) -> None:
        self.gpu = gpu

    def __enter__(self) -> GPU:
        self.gpu.status = "in_use"
        return self.gpu

    def __exit__(self, exc_type, exc, tb) -> None:
        self.gpu.status = "free"


@contextmanager
def gpu_lock(gpu: GPU) -> Iterator[GPU]:
    raise NotImplementedError("À implémenter")
    yield gpu  # pragma: no cover
