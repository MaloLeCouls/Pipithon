"""`pymistral.Sampler` est un Protocol `@runtime_checkable` qui exige
juste `__call__(logits, config, rng=None) -> int`. Tu vas en écrire un
qui RETIENT combien de fois il a été appelé — utile pour le monitoring.

Contrat :

- Classe `CountingSampler` :
  - `__init__(self, fallback: int = 0)` : stocke `fallback` (l'id token
    à renvoyer en cas d'absence de logits) et initialise `self.calls = 0`.
  - `__call__(self, logits, config, rng=None) -> int` :
    - incrémente `self.calls`,
    - si `len(logits) == 0`, renvoie `self.fallback`,
    - sinon renvoie `logits.argmax()`.

- Le Sampler doit satisfaire `isinstance(s, Sampler)` (Protocol runtime).
"""
from __future__ import annotations

import random

from pymistral import GenerationConfig, Logits


class CountingSampler:
    def __init__(self, fallback: int = 0) -> None:
        raise NotImplementedError("À implémenter")

    def __call__(
        self,
        logits: Logits,
        config: GenerationConfig,
        rng: random.Random | None = None,
    ) -> int:
        raise NotImplementedError("À implémenter")
