"""`TokenKey` est utilisée comme clé d'un cache KV (prefix-sharing) :
elle DOIT être hashable, immuable, et économe en mémoire. C'est
exactement le pattern qu'on retrouve dans les codebases vLLM/SGLang.

Contrat :

- `__slots__ = ("_prefix", "_seq_id")`.
- `__init__(self, prefix: tuple[int, ...], seq_id: int)` :
  - stocke `prefix` (déjà immuable car tuple) et `seq_id`,
  - PUIS verrouille : toute future écriture sur `_prefix`/`_seq_id`
    doit lever `AttributeError`. Utilise `object.__setattr__` pour
    la première écriture, et un `__setattr__` custom qui interdit
    les modifications ultérieures.
- `__eq__` : True si même prefix ET même seq_id.
- `__hash__` : `hash((self._prefix, self._seq_id))`.

NB : `prefix` est typé `tuple` (immuable). Si tu acceptais une `list`,
elle pourrait muter et faire dériver le hash — interdit.
"""
from __future__ import annotations


class TokenKey:
    # À implémenter (slots, init, __setattr__, __eq__, __hash__).
    ...
