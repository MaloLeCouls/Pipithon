"""Choix de design :
- __getitem__ + __len__ délégués à la liste : on hérite gratuitement de
  l'index négatif, de l'IndexError, et surtout du protocole séquence
  ancien -> `for`, `in`, `reversed` marchent sans __iter__.
- get()/nb() disparaissent : l'API devient celle que tout Python connaît.
"""


class Menu:
    def __init__(self, dishes: list[str]) -> None:
        self.dishes = list(dishes)

    def __len__(self) -> int:
        return len(self.dishes)

    def __getitem__(self, index: int) -> str:
        return self.dishes[index]
