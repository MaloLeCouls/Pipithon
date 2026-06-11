"""Choix de design :
- Callable[[Logits, GenerationConfig], int] précise la signature attendue
  (mypy strict refuse Callable nu sans args).
- Iterable[Logits] en entrée : le code n'a besoin que d'itérer.
- list[int] en retour : précis.
"""
from __future__ import annotations

from collections.abc import Callable, Iterable

from pymistral import GenerationConfig, Logits


def top_token_per_batch(
    batch: Iterable[Logits],
    scorer: Callable[[Logits, GenerationConfig], int],
) -> list[int]:
    cfg = GenerationConfig()
    return [scorer(logits, cfg) for logits in batch]
