"""Choix de design :
- Generator function : le client consomme caractère par caractère ; on ne
  matérialise jamais la séquence complète. Ttft (time-to-first-token) =
  coût du 1er caractère, pas du dernier.
- `vocab.add(ch)` est appelé à chaque tour : c'est le contrat de
  `Vocabulary` (dédup interne), donc pas besoin de tester l'existence
  avant.
"""
from __future__ import annotations

from collections.abc import Iterator

from pymistral import Token, Vocabulary


def stream_tokens(text: str, vocab: Vocabulary) -> Iterator[Token]:
    for ch in text:
        tid = vocab.add(ch)
        yield Token(id=tid, text=ch)
