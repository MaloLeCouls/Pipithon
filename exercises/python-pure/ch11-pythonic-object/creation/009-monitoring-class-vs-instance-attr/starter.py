"""Le ch.11 distingue clairement :
- **class attribute** : défini AU NIVEAU CLASSE, partagé par défaut entre
  instances. Override par instance possible (mais ça crée alors un
  attribut d'instance distinct, le class attr reste intact).
- **name mangling** : un attribut commençant par `__` (double underscore,
  PAS dunder) devient `_ClassName__attr` — protection forte contre
  override accidentel par sous-classes.

Contrat — classe `Metric(name: str, value: float)` :

- Class attribute `UNIT: str = "ms"` (défaut, partagé).
- `__init__` stocke `name`, `value`, et un compteur PRIVÉ
  `self.__count = 0` (name mangled).
- Méthode `bump(self) -> int` : incrémente `__count` et le renvoie.
- Méthode CLASSE `reset_unit(cls, new_unit: str)` : remplace `UNIT` au
  niveau classe (`cls.UNIT = new_unit`).

Tests :
- `Metric.UNIT` est `"ms"` à l'init.
- `m.UNIT = "ns"` change seulement `m`, pas `Metric.UNIT`.
- `m.__count` lève AttributeError (mangling actif).
- Mais `m._Metric__count` existe.
"""
from __future__ import annotations


class Metric:
    # À implémenter (UNIT, __init__, bump, reset_unit).
    ...
