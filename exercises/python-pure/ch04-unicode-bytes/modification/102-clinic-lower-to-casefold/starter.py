"""Cette comparaison de noms ignore la casse via .lower(). Ça rate les
plis durs ('Straße' vs 'STRASSE').

Refactor `same_ci` :
- utilise str.casefold() au lieu de str.lower(),
- comportement préservé sur l'ASCII, correct sur les cas durs.
"""


def same_ci(a: str, b: str) -> bool:
    return a.lower() == b.lower()
