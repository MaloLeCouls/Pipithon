"""Un outil de gestion de tâches organise le travail en `lanes` (voies),
une par jour.

Implémente :

1. `new_board(lanes: int) -> list[list[str]]`
   renvoie une liste de `lanes` voies, chacune une liste de tâches vide.

2. `assign(board: list[list[str]], lane: int, task: str) -> None`
   ajoute `task` à la voie d'indice `lane` (modifie le board en place).

Exemple : sur un board à 3 voies, assigner "deploy" à la voie 0 ne doit
apparaître QUE dans la voie 0.
"""


def new_board(lanes: int) -> list[list[str]]:
    ...


def assign(board: list[list[str]], lane: int, task: str) -> None:
    ...
