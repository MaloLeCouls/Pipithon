"""Un junior a écrit un `GPULock` qui ressemble à ce qui marche partout :
`__exit__` libère le GPU, retourne `True` "pour signaler que tout s'est
bien passé". Sauf que… en prod, des `RuntimeError` du bloc disparaissent
silencieusement. Le scheduler croit que tout va bien et continue à
distribuer des jobs sur un GPU qui a crashé.

Trouve le bug et corrige. Contrat :
- `__enter__` met `status='in_use'` et retourne le GPU.
- `__exit__` remet `status='free'` (toujours) MAIS laisse remonter les
  exceptions du bloc."""
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

    def __exit__(self, exc_type, exc, tb) -> bool:
        self.gpu.status = "free"
        # BUG : `return True` indique à Python d'AVALER l'exception du bloc.
        # On voulait juste « libérer le GPU » — mais on a aussi caché tous
        # les bugs.
        return True
