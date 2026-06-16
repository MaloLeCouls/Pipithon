"""Un job qui crashe avec `OutOfMemoryError` ne doit pas faire tomber tout
le scheduler : on veut juste marquer le GPU comme `failed`, *avaler*
l'exception, et continuer. En revanche, toute autre exception (bug, kill
manuel, etc.) doit remonter normalement pour que le superviseur la voie.

Implémente `TryAllocate(gpu)` :
- `gpu` a `status: str` ('free', 'in_use', 'failed').
- `__enter__` met `status='in_use'` et retourne le GPU.
- `__exit__(exc_type, exc, tb)` :
    * Si aucune exception (exc_type is None) -> remet `status='free'`,
      retourne None.
    * Si exception est `OutOfMemoryError` -> met `status='failed'`,
      retourne True (avale l'exception).
    * Sinon -> remet `status='free'`, retourne None / False
      (laisse remonter).
"""
from __future__ import annotations


class OutOfMemoryError(Exception):
    """Spécifique GPU — distinct de `MemoryError` du builtin."""


class GPU:
    def __init__(self, gpu_id: str) -> None:
        self.gpu_id = gpu_id
        self.status: str = "free"


class TryAllocate:
    def __init__(self, gpu: GPU) -> None:
        raise NotImplementedError("À implémenter")

    def __enter__(self) -> GPU:
        raise NotImplementedError("À implémenter")

    def __exit__(self, exc_type, exc, tb):
        raise NotImplementedError("À implémenter")
