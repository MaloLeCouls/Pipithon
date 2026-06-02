"""Employee a un salaire et un nom. On veut pouvoir trier par
salaire croissant, puis par nom alphabétique en cas d'égalité.

Aujourd'hui c'est un @dataclass + __lt__ manuel. Refactor :
- Garde @dataclass mais passe order=True pour générer les comparaisons.
- ATTENTION à l'ordre des champs : order=True compare par tuple des
  champs dans l'ordre de déclaration. Range les champs (salary, name)
  pour que sorted(employees) trie comme demandé.
- Supprime le __lt__ manuel.
"""

from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    salary: float

    def __lt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return (self.salary, self.name) < (other.salary, other.name)
