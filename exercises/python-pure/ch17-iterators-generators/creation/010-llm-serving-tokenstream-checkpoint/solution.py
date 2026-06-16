"""Checkpoint ch.17 — Sentence en 3 formes, version `llm-serving`.

Choix de design :
- Forme 1 (iterator manuel) : montre le protocole nu (`__iter__` retourne
  self, `__next__` avance et lève StopIteration). À usage unique : une fois
  consommé, il faut un NOUVEAU TokenStreamIter pour re-itérer.
- Forme 2 (generator function) : `yield` fait tout le boulot du `__next__`
  + StopIteration automatique. Code 10× plus court, sémantique identique.
- Forme 3 (generator expression) : la plus dense ; idéale quand le « corps »
  tient en une expression. Retourne un iterator paresseux sans `def`.
"""
from __future__ import annotations

from collections.abc import Iterator

from pymistral import Token


class TokenStreamIter:
    def __init__(self, text: str) -> None:
        self.text = text
        self._i = 0

    def __iter__(self) -> "TokenStreamIter":
        return self

    def __next__(self) -> Token:
        if self._i >= len(self.text):
            raise StopIteration
        tok = Token(id=self._i, text=self.text[self._i])
        self._i += 1
        return tok


def tokenstream_gen(text: str) -> Iterator[Token]:
    for i, ch in enumerate(text):
        yield Token(id=i, text=ch)


def tokenstream_genexpr(text: str) -> Iterator[Token]:
    return (Token(id=i, text=ch) for i, ch in enumerate(text))
