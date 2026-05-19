"""Choix de design :
- order=True génère les 4 comparateurs à partir d'un tuple des champs
  COMPARABLES, dans l'ordre de déclaration. On met `salary` en premier
  et on sort `name` de la comparaison via field(compare=False) : le tri
  est donc strictement par salaire, sans départage parasite par le nom.
"""

from dataclasses import dataclass, field


@dataclass(order=True)
class Employee:
    salary: int
    name: str = field(compare=False)
