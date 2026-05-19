"""Choix de design :
- Counter sur un générateur aplati des tags : une ligne remplace la
  double boucle + if/else. Counter == dict pour la comparaison, et
  renvoie 0 (pas KeyError) pour un tag absent côté appelant.
"""

from collections import Counter


def tag_counts(tasks: list[dict]) -> Counter:
    return Counter(tag for t in tasks for tag in t["tags"])
