"""Une expo de meubles veut deux vues sur son catalogue (une liste de refs) :

1. `every_other(catalog: list[str]) -> list[str]`
   un meuble sur deux, en partant du premier (indices 0, 2, 4...).

2. `reversed_showroom(catalog: list[str]) -> list[str]`
   le catalogue dans l'ordre inverse.

Utilise le slicing (pas de boucle, pas de reversed()/range()).
Une liste vide -> une liste vide.
"""


def every_other(catalog: list[str]) -> list[str]:
    ...


def reversed_showroom(catalog: list[str]) -> list[str]:
    ...
