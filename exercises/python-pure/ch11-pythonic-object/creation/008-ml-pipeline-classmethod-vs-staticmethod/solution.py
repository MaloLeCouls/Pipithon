"""Choix de design :
- `from_csv` : a besoin de `cls` pour la construction polymorphique
  (sous-classe → instance de sous-classe).
- `is_valid_line` : pure validation textuelle, aucune référence à la
  classe — donc `staticmethod`. Si demain on déplace cette fn au niveau
  module, le code reste correct.
- C'est précisément le critère que Fluent Python pose : « la fn
  utilise-t-elle `cls` ? Si non, `staticmethod`. »
"""
from __future__ import annotations


class Dataset:
    def __init__(self, samples: list[int]) -> None:
        self.samples = samples

    @classmethod
    def from_csv(cls, line: str) -> "Dataset":
        return cls([int(x) for x in line.split(",")])

    @staticmethod
    def is_valid_line(line: str) -> bool:
        if not line:
            return False
        try:
            for token in line.split(","):
                int(token)
        except ValueError:
            return False
        return True
