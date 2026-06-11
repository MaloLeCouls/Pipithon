"""Le décorateur `tag` veut prendre un label et tagger les sorties d'un
sampler. Mais il n'a que 2 niveaux : c'est cassé.

Refactor pour qu'il s'utilise comme :
    @tag("greedy")
    def my_sampler(logits, config, rng=None):
        return logits.argmax()

et qu'au retour, le wrapper append (label, result) à TAGGED.

Hint : il faut UNE fonction de plus.
"""
from __future__ import annotations

TAGGED: list[tuple[str, object]] = []


def tag(fn, label):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        TAGGED.append((label, result))
        return result
    return wrapper
