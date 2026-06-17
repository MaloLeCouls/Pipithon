"""Choix de design :
- `UNIT` au niveau classe : un seul stockage partagé par défaut. Override
  par instance = nouvel attribut d'instance, ne touche pas le class attr.
- `__count` (mangling) : impossible d'y accéder via `m.__count` depuis
  l'extérieur. Devient `_Metric__count` — c'est volontaire, pas un bug.
- `@classmethod reset_unit` : modifie le class attr via `cls.UNIT = ...`
  — affecte toutes les instances qui n'ont pas overridé.
"""
from __future__ import annotations


class Metric:
    UNIT: str = "ms"

    def __init__(self, name: str, value: float) -> None:
        self.name = name
        self.value = value
        self.__count = 0  # name mangled -> _Metric__count

    def bump(self) -> int:
        self.__count += 1
        return self.__count

    @classmethod
    def reset_unit(cls, new_unit: str) -> None:
        cls.UNIT = new_unit
