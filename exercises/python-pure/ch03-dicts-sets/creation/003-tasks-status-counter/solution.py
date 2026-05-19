"""Choix de design :
- Counter sur une generator expression des statuts : une ligne, pas de
  if 'k in d' / d[k]=0 à la main. Counter renvoie 0 pour une clé absente
  (pas de KeyError), ce qui simplifie le code appelant.
"""

from collections import Counter


def count_status(tasks: list[dict]) -> Counter:
    return Counter(t["status"] for t in tasks)
