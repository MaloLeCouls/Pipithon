"""Le cluster GPU veut un context manager qui marque un GPU comme `in_use`
pendant un bloc de code, et le libère à la sortie — **même si une exception
est levée** dans le bloc.

Implémente la classe `GPULock(gpu)` :
- `__enter__` met `gpu.status = "in_use"` et retourne le GPU (utilisable
  via `with GPULock(gpu) as g: ...`).
- `__exit__(exc_type, exc, tb)` remet `gpu.status = "free"`. Toujours.
  Ne retourne **pas** True : on ne veut pas avaler les exceptions du bloc.
"""
from __future__ import annotations


class GPU:
    def __init__(self, gpu_id: str) -> None:
        self.gpu_id = gpu_id
        self.status: str = "free"


class GPULock:
    def __init__(self, gpu: GPU) -> None:
        raise NotImplementedError("À implémenter")

    def __enter__(self) -> GPU:
        raise NotImplementedError("À implémenter")

    def __exit__(self, exc_type, exc, tb) -> None:
        raise NotImplementedError("À implémenter")
