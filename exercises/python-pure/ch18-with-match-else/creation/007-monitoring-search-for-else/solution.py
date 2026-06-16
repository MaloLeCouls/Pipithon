"""Choix de design :
- `for/else` : pythonique pour le pattern « search avec fallback ». Le
  `else` lit *« quand la boucle a terminé sans break »*. C'est contre-
  intuitif (le mot-clé devrait être `nobreak`), mais quand on a digéré la
  sémantique on s'en sert beaucoup pour éviter un drapeau.
- `next((... for ...), default)` est l'équivalent fonctionnel ; ici on
  drille la version impérative qui marche aussi quand le corps de la
  boucle est complexe.
"""
from __future__ import annotations


class Metric:
    def __init__(self, name: str, value: float) -> None:
        self.name = name
        self.value = value


def first_critical(metrics: list[Metric], threshold: float, default: str) -> str:
    for m in metrics:
        if m.value > threshold:
            return m.name
    else:
        return default
