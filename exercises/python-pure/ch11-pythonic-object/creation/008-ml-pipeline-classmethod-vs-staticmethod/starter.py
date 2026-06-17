"""Tu mélanges souvent `classmethod` et `staticmethod`. Règle :
- `@classmethod` quand tu utilises `cls` (construction polymorphique).
- `@staticmethod` quand tu rangerais sinon une fn module-level dans la classe.

Contrat — classe `Dataset(samples: list[int])` :

- `@classmethod from_csv(cls, line: str) -> "Dataset"` : parse `"1,2,3"`
  en `[1, 2, 3]` et renvoie `cls([...])`.
- `@staticmethod is_valid_line(line: str) -> bool` : True si `line`
  est non vide ET que chaque token est convertible en int. N'utilise PAS
  `cls`/`self`.

Test : `is_valid_line` peut être appelée sans instance (`Dataset.is_valid_line(...)`).
"""
from __future__ import annotations


class Dataset:
    def __init__(self, samples: list[int]) -> None:
        self.samples = samples

    @classmethod
    def from_csv(cls, line: str) -> "Dataset":
        raise NotImplementedError("À implémenter")

    @staticmethod
    def is_valid_line(line: str) -> bool:
        raise NotImplementedError("À implémenter")
