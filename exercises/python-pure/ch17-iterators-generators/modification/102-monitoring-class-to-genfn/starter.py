"""Le module monitoring contient un `MetricStream` écrit avec
`__iter__`/`__next__` à la main (héritage d'une vieille codebase). C'est
verbeux pour rien : un générateur fait pareil en 3 lignes.

Refactor :
- Conserve la fonction `metric_stream(metrics, severity) -> Iterator[Metric]`.
- Réécris son corps avec `yield` (mot-clé du chapitre).
- **Supprime entièrement** la classe `MetricStream` (plus utilisée).
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Metric:
    def __init__(self, name: str, severity: str) -> None:
        self.name = name
        self.severity = severity


class MetricStream:
    def __init__(self, metrics: list[Metric], severity: str) -> None:
        self._metrics = metrics
        self._severity = severity
        self._i = 0

    def __iter__(self) -> "MetricStream":
        return self

    def __next__(self) -> Metric:
        while self._i < len(self._metrics):
            m = self._metrics[self._i]
            self._i += 1
            if m.severity == self._severity:
                return m
        raise StopIteration


def metric_stream(metrics: Iterable[Metric], severity: str) -> Iterator[Metric]:
    return MetricStream(list(metrics), severity)
