"""Logits — vecteur de scores. Chapitre 11 (Pythonic object, analogue Vector2d).

Implémentation Python pure (pas de numpy). Supporte `+`, indexation, slicing,
softmax stable (subtract max), argmax.
"""
from __future__ import annotations

import math
from collections.abc import Iterator, Sequence
from typing import overload


class Logits:
    """Vecteur immuable de scores réels (logits)."""

    __slots__ = ("_scores",)

    def __init__(self, scores: Sequence[float]) -> None:
        self._scores: tuple[float, ...] = tuple(scores)

    @property
    def scores(self) -> tuple[float, ...]:
        return self._scores

    def __len__(self) -> int:
        return len(self._scores)

    def __iter__(self) -> Iterator[float]:
        return iter(self._scores)

    @overload
    def __getitem__(self, index: int) -> float: ...
    @overload
    def __getitem__(self, index: slice) -> Logits: ...
    def __getitem__(self, index: int | slice) -> float | Logits:
        if isinstance(index, slice):
            return Logits(self._scores[index])
        return self._scores[index]

    def __add__(self, other: Logits) -> Logits:
        if len(self) != len(other):
            raise ValueError(
                f"Logits dimensions mismatch: {len(self)} vs {len(other)}"
            )
        return Logits(tuple(a + b for a, b in zip(self._scores, other._scores)))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Logits):
            return NotImplemented
        return self._scores == other._scores

    def __hash__(self) -> int:
        return hash(self._scores)

    def __repr__(self) -> str:
        return f"Logits(n={len(self)})"

    def argmax(self) -> int:
        if not self._scores:
            raise ValueError("argmax of empty Logits")
        best_idx = 0
        best_val = self._scores[0]
        for i, v in enumerate(self._scores[1:], start=1):
            if v > best_val:
                best_val = v
                best_idx = i
        return best_idx

    def softmax(self, temperature: float = 1.0) -> list[float]:
        """Softmax numériquement stable. `temperature > 0`."""
        if temperature <= 0:
            raise ValueError(f"temperature must be > 0, got {temperature}")
        if not self._scores:
            return []
        scaled = [s / temperature for s in self._scores]
        m = max(scaled)
        exps = [math.exp(s - m) for s in scaled]
        total = sum(exps)
        return [e / total for e in exps]
