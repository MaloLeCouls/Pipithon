"""Choix de design :
- Distinction stricte iterable / iterator : `Menu` est l'iterable réutilisable
  (à chaque `iter()` il rend un nouveau iterator) ; `MenuIterator` est
  l'iterator à usage unique (avance, ne se remet pas à zéro).
- `MenuIterator.__iter__` retourne `self` — c'est la règle qui fait fonctionner
  les boucles `for` sur les iterators (et qu'on oubliera à la fin du chapitre
  pour mesurer la nuance).
"""
from __future__ import annotations


class Dish:
    def __init__(self, dish_id: str, name: str, price: float) -> None:
        self.dish_id = dish_id
        self.name = name
        self.price = price


class MenuIterator:
    def __init__(self, dishes: list[Dish]) -> None:
        self._dishes = dishes
        self._i = 0

    def __iter__(self) -> "MenuIterator":
        return self

    def __next__(self) -> Dish:
        if self._i >= len(self._dishes):
            raise StopIteration
        dish = self._dishes[self._i]
        self._i += 1
        return dish


class Menu:
    def __init__(self, dishes: list[Dish]) -> None:
        self.dishes = dishes

    def __iter__(self) -> MenuIterator:
        return MenuIterator(self.dishes)
