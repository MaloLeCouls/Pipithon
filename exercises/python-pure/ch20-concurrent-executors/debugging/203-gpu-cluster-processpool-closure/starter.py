"""Bug observé : `batch_hashes(payloads, factor=3)` lève
`PicklingError: Can't pickle <function <local>>`.

Indices :
- `ProcessPoolExecutor` envoie la fn au worker via `pickle`.
- Les CLOSURES (fns locales qui capturent une variable) ne sont PAS
  picklables.
- Fix : top-level fn `hash_with_factor(payload: str, factor: int)`
  utilisée via `ex.map(hash_with_factor, payloads, [factor]*len(payloads))`
  (broadcast manuel du factor), ou via `functools.partial`.

Pour cet exo, on choisit la version la plus simple : top-level fn +
broadcast du factor.
"""
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor


def batch_hashes(payloads: list[str], factor: int) -> list[int]:
    # BUG : closure non picklable.
    def with_factor(payload: str) -> int:
        h = 0
        for c in payload:
            h = (h * 31 + ord(c) + factor) & 0xFFFFFFFF
        return h

    with ProcessPoolExecutor(max_workers=2) as ex:
        return list(ex.map(with_factor, payloads))
