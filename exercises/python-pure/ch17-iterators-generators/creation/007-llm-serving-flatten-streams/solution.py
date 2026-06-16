"""Choix de design :
- `yield from stream` : équivalent à `for tok in stream: yield tok` mais
  transmet aussi `send()`, `throw()`, `close()` à la coroutine sous-jacente.
  C'est l'expression chap.17 du « pipeline composable ».
- Un seul passage sur `streams` (boucle simple) : si l'appelant passe un
  générateur, on respecte son usage unique sans le ré-itérer en douce.
- On peut écrire l'équivalent en double boucle ; `yield from` est juste
  plus court et plus puissant.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator

from pymistral import Token


def flatten_streams(streams: Iterable[Iterator[Token]]) -> Iterator[Token]:
    for stream in streams:
        yield from stream
