"""Choix de design :
- `__enter__` retourne le GPU lui-même : permet `with GPULock(gpu) as g:` et
  utilisation de `g` dans le bloc (équivalent à `gpu` mais explicite).
- `__exit__` remet `free` *avant* d'éventuellement re-raiser. On ne retourne
  rien (None implicite) : Python re-raise toute exception du bloc.
"""
from __future__ import annotations


class GPU:
    def __init__(self, gpu_id: str) -> None:
        self.gpu_id = gpu_id
        self.status: str = "free"


class GPULock:
    def __init__(self, gpu: GPU) -> None:
        self.gpu = gpu

    def __enter__(self) -> GPU:
        self.gpu.status = "in_use"
        return self.gpu

    def __exit__(self, exc_type, exc, tb) -> None:
        self.gpu.status = "free"
