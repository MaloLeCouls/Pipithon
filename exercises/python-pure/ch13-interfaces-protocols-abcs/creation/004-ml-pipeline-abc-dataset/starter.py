"""Une ABC = un contrat NOMINAL (hériter explicitement) — l'autre face
du typage par rapport au Protocol structurel.

Contrat :

- Classe `Dataset(abc.ABC)` :
  - `@abc.abstractmethod def __len__(self) -> int`.
  - `@abc.abstractmethod def __getitem__(self, idx: int) -> int`.
  - méthode CONCRÈTE `summary(self) -> str` qui renvoie
    `f"Dataset(n={len(self)})"` — utilise les méthodes abstraites.

- Sous-classe `RangeDataset(Dataset)` qui implémente les deux :
  - `__init__(self, n: int)` stocke `n`.
  - `__len__` renvoie `n`.
  - `__getitem__(i)` renvoie `i * 2` (juste un placeholder).

Le test vérifie qu'instancier `Dataset()` directement lève TypeError.
"""
from __future__ import annotations

import abc


class Dataset(abc.ABC):
    ...


class RangeDataset(Dataset):
    def __init__(self, n: int) -> None:
        raise NotImplementedError("À implémenter")
