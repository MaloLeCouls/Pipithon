"""Choix de design :
- Callable[[Sample], None] précise : un Sample en entrée, rien en sortie.
- mypy strict est satisfait ; le compilateur peut vérifier les callbacks.
"""
from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass


@dataclass
class Sample:
    feature: float


def process(samples: Iterable[Sample], callback: Callable[[Sample], None]) -> None:
    for s in samples:
        callback(s)
