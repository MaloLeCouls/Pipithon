"""Un job d'inférence multi-GPU veut **verrouiller N GPUs ensemble** : tous
réservés à l'entrée, tous libérés à la sortie — même si une exception
survient au milieu. Le nombre de GPUs n'est pas connu à l'écriture ;
écrire `with GPULock(g1), GPULock(g2), ...` ne marche pas.

Implémente `allocate_all(gpus)` (un context manager via `@contextmanager`) :
- `gpus` : liste de `GPU`.
- À l'entrée : pose un `GPULock` sur chaque GPU (utilise `ExitStack`).
- Yield la liste des GPUs verrouillés (utilisable via `as`).
- À la sortie : tous les GPUs sont libérés en ordre inverse (LIFO),
  exception ou non.
"""
from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager


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


@contextmanager
def allocate_all(gpus: list[GPU]) -> Iterator[list[GPU]]:
    raise NotImplementedError("À implémenter")
    yield gpus  # pragma: no cover  # garde la signature de generator
