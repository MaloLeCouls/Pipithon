"""Choix de design :
- __post_init__ centralise les invariants APRÈS l'__init__ généré : on
  garde la concision de @dataclass tout en refusant un état incohérent
  dès la construction (échouer tôt > corrompre des données plus loin).
"""

from dataclasses import dataclass


@dataclass
class Dish:
    name: str
    price: float

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("name vide")
        if self.price <= 0:
            raise ValueError("price doit être > 0")
