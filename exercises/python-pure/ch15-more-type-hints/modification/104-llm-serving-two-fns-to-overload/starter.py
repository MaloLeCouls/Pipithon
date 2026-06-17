"""Tu as DEUX fonctions `decode_int` et `decode_list` qui font la même
chose au type près. Fusionne-les en UNE seule fn `decode` avec 2
overloads + 1 impl unique.

Vocab : un `Vocabulary` simulé est fourni — `decode(id)` renvoie un
mot.

Contrat solution :
- `@overload def decode(x: int) -> str: ...`
- `@overload def decode(x: list[int]) -> list[str]: ...`
- `def decode(x: int | list[int]) -> str | list[str]:` (impl)
"""
from __future__ import annotations

_VOCAB = ["<pad>", "the", "cat", "sat", "on", "mat"]


def decode_int(token_id: int) -> str:
    return _VOCAB[token_id]


def decode_list(token_ids: list[int]) -> list[str]:
    return [_VOCAB[i] for i in token_ids]
