"""Correction :
- Bug : set(names) sur des str non normalisées garde "Zoé" (U+00E9)
  ET "Zoé" (e + U+0301) comme deux éléments distincts -> surcompte.
- Fix : normaliser chaque nom en NFC avant de le mettre dans le set.
  Les formes canoniquement équivalentes fusionnent alors.
"""

import unicodedata


def count_unique(names: list[str]) -> int:
    return len({unicodedata.normalize("NFC", n) for n in names})
