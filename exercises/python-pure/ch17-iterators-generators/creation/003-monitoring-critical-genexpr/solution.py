"""Choix de design :
- Generator expression : la forme la plus concise quand le filtrage tient
  en une expression. Pas de `yield` => la fonction n'est PAS une generator
  function : elle renvoie directement l'iterator produit par la genexpr.
- Mémoire O(1), évaluation à la demande — parfait pour un dashboard qui
  affiche les alertes au fil de l'eau.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Metric:
    def __init__(self, name: str, value: float, severity: str) -> None:
        self.name = name
        self.value = value
        self.severity = severity


def critical_alerts(metrics: Iterable[Metric]) -> Iterator[Metric]:
    return (m for m in metrics if m.severity == "critical")
