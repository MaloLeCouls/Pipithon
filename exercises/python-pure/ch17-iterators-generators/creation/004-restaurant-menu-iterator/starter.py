"""Un restaurant veut un iterator manuel sur les plats du menu : plein contrôle
sur l'avancement (pour brancher du logging, des filtres dynamiques, etc.).

On écrit le protocole d'itération **sans `yield`** — à la main.

Implémente :
- `Dish(dish_id: str, name: str, price: float)`.
- `Menu(dishes: list[Dish])` :
    * `__iter__(self)` retourne un MenuIterator **frais** sur `dishes`.
    * Le `Menu` est donc **réutilisable** : `iter(menu)` 2× redémarre.
- `MenuIterator(dishes: list[Dish])` :
    * `__iter__(self)` retourne `self` (un iterator est son propre iterable).
    * `__next__(self)` retourne le prochain `Dish`, lève `StopIteration` à la fin.
"""
from __future__ import annotations


class Dish:
    def __init__(self, dish_id: str, name: str, price: float) -> None:
        self.dish_id = dish_id
        self.name = name
        self.price = price


class MenuIterator:
    def __init__(self, dishes: list[Dish]) -> None:
        raise NotImplementedError("À implémenter")

    def __iter__(self) -> "MenuIterator":
        raise NotImplementedError("À implémenter")

    def __next__(self) -> Dish:
        raise NotImplementedError("À implémenter")


class Menu:
    def __init__(self, dishes: list[Dish]) -> None:
        self.dishes = dishes

    def __iter__(self) -> MenuIterator:
        raise NotImplementedError("À implémenter")
