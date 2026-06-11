"""Choix de design (le canonique Fluent Python ch.6) :
- HauntedBus illustre le bug : le `[]` par défaut est évalué UNE FOIS à la
  définition de la fonction et est partagé par toutes les instances qui
  acceptent ce défaut.
- Bus utilise le None-guard : default à None, instanciation d'une liste fraîche
  dans le corps de __init__.
- make_fleet retourne (copy.copy, copy.deepcopy) du prototype :
  * copy.copy crée une nouvelle instance mais réutilise les attributs ;
    si on a *aussi* fait une copie superficielle de la liste manuellement, on
    aurait isolé — mais ici on appelle juste copy.copy : la liste reste partagée.
  * copy.deepcopy descend récursivement : la liste est isolée.
"""
from __future__ import annotations

import copy


class HauntedBus:
    def __init__(self, passengers: list[str] = []) -> None:  # noqa: B006 — le bug est volontaire
        self.passengers = passengers

    def pick(self, name: str) -> None:
        self.passengers.append(name)

    def drop(self, name: str) -> None:
        self.passengers.remove(name)


class Bus:
    def __init__(self, passengers: list[str] | None = None) -> None:
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name: str) -> None:
        self.passengers.append(name)

    def drop(self, name: str) -> None:
        self.passengers.remove(name)


def make_fleet(prototype: Bus) -> tuple[Bus, Bus]:
    return copy.copy(prototype), copy.deepcopy(prototype)
