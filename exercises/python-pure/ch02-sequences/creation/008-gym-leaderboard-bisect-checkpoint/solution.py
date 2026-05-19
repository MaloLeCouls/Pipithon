"""Choix de design (l'idée du chapitre 2) :
- grade : une table de seuils + bisect_right remplace 6 if/elif. Ajouter
  un palier = éditer deux listes, pas réécrire la logique. C'est l'exemple
  canonique 'bisect comme lookup table'.
- Leaderboard.add : bisect.insort garde l'invariant trié en O(n) d'insert
  mais O(log n) de recherche, sans jamais re-trier toute la liste.
- top_count : len - bisect_right(scores, score) = nb d'éléments
  strictement supérieurs, en O(log n), zéro boucle.
- scores() renvoie une copie : l'invariant trié ne peut pas être cassé
  de l'extérieur.
"""

import bisect

_BREAKPOINTS = [60, 70, 80, 90, 100]
_LETTERS = "FEDCBA"


def grade(score: int) -> str:
    return _LETTERS[bisect.bisect_right(_BREAKPOINTS, score)]


class Leaderboard:
    def __init__(self) -> None:
        self._scores: list[int] = []

    def add(self, score: int) -> None:
        bisect.insort(self._scores, score)

    def scores(self) -> list[int]:
        return list(self._scores)

    def top_count(self, score: int) -> int:
        return len(self._scores) - bisect.bisect_right(self._scores, score)
