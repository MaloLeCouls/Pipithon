"""Cette ABC `Sampler` n'apporte AUCUNE impl partagée — juste deux
`@abstractmethod`. C'est exactement le cas où un `typing.Protocol` est
préférable : ça désaccouple le code, et n'importe quelle classe avec la
bonne forme (duck typing) marche.

Refactore :
1. `Sampler` doit être un `Protocol` (pas une `ABC`).
2. `GreedyImpl` ne doit PLUS hériter de `Sampler`.
3. `pick(sampler: Sampler, ...)` reste typé `Sampler` — c'est l'annotation
   qui assure la cohérence.

Comportement runtime identique. Garanties mypy renforcées (typage structurel).
"""
from __future__ import annotations

import abc


class Sampler(abc.ABC):
    @abc.abstractmethod
    def sample(self, scores: list[float]) -> int: ...


class GreedyImpl(Sampler):
    def sample(self, scores: list[float]) -> int:
        return max(range(len(scores)), key=lambda i: scores[i])


def pick(sampler: Sampler, scores: list[float]) -> int:
    return sampler.sample(scores)
