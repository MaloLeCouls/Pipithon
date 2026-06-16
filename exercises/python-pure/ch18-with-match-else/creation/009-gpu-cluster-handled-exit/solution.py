"""Choix de design :
- `__exit__` retourne `True` UNIQUEMENT pour `OutOfMemoryError` — c'est le
  signal Python pour « j'ai géré, n'arrête pas l'interpréteur ».
- Pour tout autre type d'exception, on remet `free` et on retourne None
  (implicite) : l'exception remonte normalement.
- Le cas « pas d'exception » est traité d'abord pour la lisibilité.
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
        self.gpu = gpu

    def __enter__(self) -> GPU:
        self.gpu.status = "in_use"
        return self.gpu

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            self.gpu.status = "free"
            return None
        if issubclass(exc_type, OutOfMemoryError):
            self.gpu.status = "failed"
            return True  # avale l'exception
        self.gpu.status = "free"
        return None  # laisse remonter
