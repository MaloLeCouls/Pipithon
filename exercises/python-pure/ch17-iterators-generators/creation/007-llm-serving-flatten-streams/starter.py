"""Plusieurs workers d'inférence produisent chacun un flux paresseux de tokens.
Tu veux **concaténer** ces flux en un seul, un worker à la fois, dans l'ordre,
sans matérialiser aucun batch en RAM.

Implémente `flatten_streams(streams) -> Iterator[Token]` :
- `streams` : itérable de générateurs / iterators de `Token` (pymistral).
- yield les Tokens dans l'ordre des streams, puis dans l'ordre interne.

⚠️ Piège du chapitre — *signalé* :
   un générateur est à **usage unique**. Si tu itères `streams` deux fois
   (par exemple pour pré-compter), la 2e itération est vide. Garde **un
   seul passage** sur `streams`.

Mot-clé attendu : `yield from`. (Une double boucle marche aussi, mais
`yield from` est l'expression idiomatique du chapitre.)
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator

from pymistral import Token


def flatten_streams(streams: Iterable[Iterator[Token]]) -> Iterator[Token]:
    raise NotImplementedError("À implémenter")
