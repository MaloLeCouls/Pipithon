"""Choix de design :
- `match/case` rend explicite que c'est *un* dispatch sur valeur (pas une
  série indépendante de tests). Plus lisible, plus facile à étendre sans
  oublier le défaut.
- On peut grouper plusieurs valeurs en un seul case avec `|` (`case
  "todo" | "doing":`) ; ici on garde un case par libellé pour que le
  mapping reste 1-à-1 et grep-friendly.
"""
from __future__ import annotations


def status_label(status: str) -> str:
    match status:
        case "todo":
            return "À faire"
        case "doing":
            return "En cours"
        case "review":
            return "En revue"
        case "done":
            return "Terminé"
        case "blocked":
            return "Bloqué"
        case _:
            return "Inconnu"
