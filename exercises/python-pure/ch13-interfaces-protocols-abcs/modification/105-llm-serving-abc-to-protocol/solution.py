"""Choix de design :
- `Protocol` (typing) : pas d'héritage requis, juste la forme.
- `GreedyImpl` reste exactement le même code, sans la base class.
- mypy --strict valide que `GreedyImpl` est compatible avec `Sampler`
  parce qu'il a `sample(self, scores: list[float]) -> int` — structurel.
"""
from __future__ import annotations

from typing import Protocol


class Sampler(Protocol):
    def sample(self, scores: list[float]) -> int: ...


class GreedyImpl:
    def sample(self, scores: list[float]) -> int:
        return max(range(len(scores)), key=lambda i: scores[i])


def pick(sampler: Sampler, scores: list[float]) -> int:
    return sampler.sample(scores)
