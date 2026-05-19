"""Choix de design :
- set(a) & set(b) et set(a) - set(b) expriment l'intention en O(n+m),
  sans boucle imbriquée O(n*m) ni gestion manuelle de doublons.
- On renvoie des set : la déduplication est intrinsèque au domaine
  (un allergène est présent ou non, pas 'deux fois').
"""


def common_allergens(a: list[str], b: list[str]) -> set[str]:
    return set(a) & set(b)


def only_in_first(a: list[str], b: list[str]) -> set[str]:
    return set(a) - set(b)
