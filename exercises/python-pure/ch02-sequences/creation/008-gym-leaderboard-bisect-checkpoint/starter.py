"""CHECKPOINT chapitre 2 — si tu fais ça sans réfléchir, les séquences et
bisect sont acquis.

Une salle de sport tient un classement de scores au challenge mensuel.

1. `grade(score: int) -> str`
   Convertit un score en lettre via une TABLE de seuils + bisect
   (PAS une cascade de if/elif) :
     score  < 60        -> "F"
     60  <= score < 70  -> "E"
     70  <= score < 80  -> "D"
     80  <= score < 90  -> "C"
     90  <= score < 100 -> "B"
     score >= 100        -> "A"

2. Classe `Leaderboard`
   - `__init__`            : classement vide.
   - `add(self, score: int)`: insère en gardant la liste triée croissante
                              (bisect.insort, pas de re-tri global).
   - `scores(self) -> list[int]` : la liste triée (copie défensive).
   - `top_count(self, score: int) -> int` : combien de scores enregistrés
     sont strictement SUPÉRIEURS à `score` (via bisect, pas de boucle).
"""

import bisect  # noqa: F401  (à utiliser)


def grade(score: int) -> str:
    ...


class Leaderboard:
    def __init__(self) -> None:
        ...

    def add(self, score: int) -> None:
        ...

    def scores(self) -> list[int]:
        ...

    def top_count(self, score: int) -> int:
        ...
