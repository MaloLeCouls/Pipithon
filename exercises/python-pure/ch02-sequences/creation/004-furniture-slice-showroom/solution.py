"""Choix de design :
- Le slicing exprime l'intention en une expression et renvoie toujours
  une nouvelle liste (pas de mutation), y compris sur l'entrée vide.
- [::2] = un sur deux ; [::-1] = inversion. Pas besoin de range/reversed.
"""


def every_other(catalog: list[str]) -> list[str]:
    return catalog[::2]


def reversed_showroom(catalog: list[str]) -> list[str]:
    return catalog[::-1]
