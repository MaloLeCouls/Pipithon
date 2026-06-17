"""Ce `BaseTokenizer` est une « pseudo-ABC » : il déclare des méthodes
vides qui lèvent `NotImplementedError`. Conséquence : on découvre qu'une
sous-classe incomplète est buguée seulement quand on APPELLE la méthode
manquante — souvent en prod, jamais en CI.

Refactore en vraie ABC : `abc.ABC` + `@abc.abstractmethod`. Le checker
de contrat se déclenchera dès l'instanciation, beaucoup plus tôt.

Le test sur le starter :
- `IncompleteTokenizer()` se construit (pas idéal),
- mais `IncompleteTokenizer().encode("x")` lève NotImplementedError.

Le test sur la solution :
- `IncompleteTokenizer()` lève TypeError — la sous-classe incomplète
  refuse d'être instanciée. C'est le bon comportement.
"""
from __future__ import annotations


class BaseTokenizer:
    def encode(self, text: str) -> list[int]:
        raise NotImplementedError

    def decode(self, ids: list[int]) -> str:
        raise NotImplementedError


class CompleteTokenizer(BaseTokenizer):
    def encode(self, text: str) -> list[int]:
        return [ord(c) for c in text]

    def decode(self, ids: list[int]) -> str:
        return "".join(chr(i) for i in ids)


class IncompleteTokenizer(BaseTokenizer):
    # Oublie d'implémenter `encode`.
    def decode(self, ids: list[int]) -> str:
        return "x" * len(ids)
