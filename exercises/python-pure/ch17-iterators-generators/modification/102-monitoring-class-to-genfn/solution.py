"""Choix de design :
- Generator function : tout l'état (index implicite, sortie de boucle, leak
  de StopIteration) est géré par Python. Plus rien à maintenir à la main.
- On accepte directement `Iterable[Metric]` (plus besoin de matérialiser une
  liste comme le faisait MetricStream).
- La classe MetricStream est supprimée — c'est l'objet du refactor.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Metric:
    def __init__(self, name: str, severity: str) -> None:
        self.name = name
        self.severity = severity


def metric_stream(metrics: Iterable[Metric], severity: str) -> Iterator[Metric]:
    for m in metrics:
        if m.severity == severity:
            yield m
