"""Choix de design :
- `__call__` permet à la classe d'être utilisée comme une fn ; c'est ce
  qui la rend conforme au Protocol `Sampler`.
- État interne `calls` : la classe-callable est utile précisément quand
  on a besoin de cet état (vs une fn pure).
- Aucun héritage : `Sampler` est un Protocol, donc duck typing statique.
"""
from __future__ import annotations

import random

from pymistral import GenerationConfig, Logits


class CountingSampler:
    def __init__(self, fallback: int = 0) -> None:
        self.fallback = fallback
        self.calls = 0

    def __call__(
        self,
        logits: Logits,
        config: GenerationConfig,
        rng: random.Random | None = None,
    ) -> int:
        self.calls += 1
        if len(logits) == 0:
            return self.fallback
        return logits.argmax()
