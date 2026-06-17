"""Choix de design :
- `abc.ABC` + `@abc.abstractmethod` : Python refuse l'instanciation tant
  qu'une méthode abstraite n'est pas overridden.
- `summary` est CONCRÈTE et s'appuie sur les abstraites — pattern « template
  method ». L'enfant n'a qu'à fournir le mince contrat des abstractmethods.
- `RangeDataset` ferme le contrat → instanciable.
"""
from __future__ import annotations

import abc


class Dataset(abc.ABC):
    @abc.abstractmethod
    def __len__(self) -> int: ...

    @abc.abstractmethod
    def __getitem__(self, idx: int) -> int: ...

    def summary(self) -> str:
        return f"Dataset(n={len(self)})"


class RangeDataset(Dataset):
    def __init__(self, n: int) -> None:
        self.n = n

    def __len__(self) -> int:
        return self.n

    def __getitem__(self, idx: int) -> int:
        return idx * 2
