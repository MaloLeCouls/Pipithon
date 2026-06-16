"""Un dashboard de monitoring veut un flux paresseux des alertes critiques
(potentiellement des millions de métriques — on n'en matérialise aucune liste).

Implémente `critical_alerts(metrics)` :
- `metrics` : itérable de `Metric` (attribut `severity: str` parmi
  `'info', 'warning', 'critical'`).
- retourne un **Iterator** sur les Metrics dont `severity == 'critical'`.

⚠️ Utilise une **generator expression** : `(m for m in metrics if ...)`.
Pas de `yield`, pas de boucle explicite, pas de list comprehension.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Metric:
    def __init__(self, name: str, value: float, severity: str) -> None:
        self.name = name
        self.value = value
        self.severity = severity


def critical_alerts(metrics: Iterable[Metric]) -> Iterator[Metric]:
    raise NotImplementedError("À implémenter")
