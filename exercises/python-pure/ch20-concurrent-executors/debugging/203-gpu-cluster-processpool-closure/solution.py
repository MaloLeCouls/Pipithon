"""Fix : promouvoir la closure en top-level fn `hash_with_factor`.
Cette fn est picklable (référencée par son nom de module).

Pour passer `factor` à chaque appel via `ex.map` : `ex.map(fn, iter1,
iter2)` appelle `fn(item1, item2)` — on broadcast factor en répétant.

Alternative équivalente : `functools.partial(hash_with_factor, factor=factor)`
puis `ex.map(partial_fn, payloads)`. Les partial DE fns top-level sont
picklables.
"""
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor


def hash_with_factor(payload: str, factor: int) -> int:
    h = 0
    for c in payload:
        h = (h * 31 + ord(c) + factor) & 0xFFFFFFFF
    return h


def batch_hashes(payloads: list[str], factor: int) -> list[int]:
    with ProcessPoolExecutor(max_workers=2) as ex:
        return list(ex.map(hash_with_factor, payloads, [factor] * len(payloads)))
