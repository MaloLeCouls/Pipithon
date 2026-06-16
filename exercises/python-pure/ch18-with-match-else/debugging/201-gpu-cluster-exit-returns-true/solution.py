"""Choix de design (correctif) :
- `__exit__` retournant `True` veut dire « j'ai géré, n'arrête pas
  l'interpréteur ». C'est un signal *sélectif*, pas un sceau de satisfaction.
- Pour libérer une ressource ET laisser remonter les exceptions : retourne
  None (implicite) ou False.
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
