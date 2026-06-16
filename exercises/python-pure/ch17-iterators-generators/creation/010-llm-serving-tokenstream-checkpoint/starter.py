"""Checkpoint chapitre 17 — Reproduire l'exemple canonique `Sentence` de
Fluent Python, en l'adaptant au domaine `llm-serving` : itérer sur les
caractères d'un texte et les **tokeniser** en stream.

Tu dois écrire **trois versions strictement équivalentes** :

1. `TokenStreamIter(text)` — *iterator écrit à la main* :
   - `__init__` stocke le texte et un index interne.
   - `__iter__` retourne `self`.
   - `__next__` produit le prochain `Token` (id = position du caractère
     dans le texte ; text = le caractère). Lève `StopIteration` à la fin.

2. `tokenstream_gen(text) -> Iterator[Token]` — *generator function* :
   - une seule `def` avec `yield`.

3. `tokenstream_genexpr(text) -> Iterator[Token]` — *generator expression* :
   - une seule `return` sur `(Token(...) for ...)`.

Toutes trois doivent produire la **même séquence** : pour `text = "ab"`,
`[Token(id=0, text='a'), Token(id=1, text='b')]`. Toutes sont paresseuses
(retournent un Iterator, pas une list).
"""
from __future__ import annotations

from collections.abc import Iterator

from pymistral import Token


class TokenStreamIter:
    def __init__(self, text: str) -> None:
        raise NotImplementedError("À implémenter")

    def __iter__(self) -> "TokenStreamIter":
        raise NotImplementedError("À implémenter")

    def __next__(self) -> Token:
        raise NotImplementedError("À implémenter")


def tokenstream_gen(text: str) -> Iterator[Token]:
    raise NotImplementedError("À implémenter")


def tokenstream_genexpr(text: str) -> Iterator[Token]:
    raise NotImplementedError("À implémenter")
