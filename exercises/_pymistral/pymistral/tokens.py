"""Token — unité atomique de texte. Introduit au chapitre 1 (data model).

`Token` est *frozen* (immutable) et hashable : utilisable comme clé de dict ou
membre de set. Le `__repr__` est sans ambiguïté, conforme au protocole Fluent
Python ch.1.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Token:
    """Une unité de texte avec son identifiant dans un vocabulaire.

    Attributs:
        id: index dans le `Vocabulary` (entier positif).
        text: forme imprimable du token (peut être un caractère, une pièce BPE).
    """

    id: int
    text: str

    def __repr__(self) -> str:
        return f"Token(id={self.id}, text={self.text!r})"
