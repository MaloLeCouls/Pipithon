"""Choix de design :
- order=True génère __lt__/__le__/__gt__/__ge__ par tuple des
  champs dans l'ordre de déclaration. Pour trier d'abord par salary
  puis par name, on déclare salary AVANT name.
- Le constructeur reste positionnel (Employee(salary, name)), ce
  qui est documenté par l'ordre des champs.
"""

from dataclasses import dataclass


@dataclass(order=True)
class Employee:
    salary: float
    name: str
