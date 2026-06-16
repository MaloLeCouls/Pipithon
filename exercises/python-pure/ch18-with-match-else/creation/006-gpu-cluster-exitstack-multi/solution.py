"""Choix de design :
- `ExitStack` : LE pattern pour empiler dynamiquement N context managers
  dont le nombre est connu au runtime (impossible avec `with a, b, c:`).
- `stack.enter_context(cm)` appelle `cm.__enter__()` immédiatement et
  enregistre `cm.__exit__` pour qu'il soit appelé à la sortie de l'ExitStack.
- Ordre LIFO garanti : si on a posé 5 verrous, ils sont relâchés du 5e
  vers le 1er — même si une exception remonte du bloc.
"""
from __future__ import annotations

from collections.abc import Iterator
from contextlib import ExitStack, contextmanager


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
    with ExitStack() as stack:
        locked = [stack.enter_context(GPULock(g)) for g in gpus]
        yield locked
