"""Choix de design :
- unicodedata.normalize("NFC", ...) sur les deux opérandes : NFC
  recompose les séquences (e + ́ -> é) en une forme canonique unique.
  Comparer les str brutes donnerait des faux négatifs invisibles à
  l'œil — un bug typique de déduplication de données saisies.
"""

import unicodedata


def same_name(a: str, b: str) -> bool:
    return unicodedata.normalize("NFC", a) == unicodedata.normalize("NFC", b)
