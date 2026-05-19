"""Un restaurant veut accéder à ses plats par position : `menu[0]`, `menu[-1]`.

Implémente la classe `Menu` :
- `__init__(self, dishes: list[str])` stocke les plats.
- `__getitem__(self, index: int)` renvoie le plat à cette position.
  L'indexation négative doit fonctionner. Un index hors plage doit lever
  IndexError (comportement naturel d'une liste).
"""


class Menu:
    def __init__(self, dishes: list[str]) -> None:
        ...

    def __getitem__(self, index: int) -> str:
        ...
