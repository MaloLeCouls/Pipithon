"""Choix de design :
- __post_init__ exécute la validation à chaque construction : le
  caller ne peut plus l'oublier, l'invariant "price > 0" est porté
  par la classe elle-même (pas par un appelant discipliné).
- L'erreur reste un ValueError au même moment logique (à la
  construction), donc l'API d'erreur ne régresse pas.
"""

from dataclasses import dataclass


@dataclass
class Dish:
    name: str
    price: float

    def __post_init__(self) -> None:
        if self.price <= 0:
            raise ValueError("price must be > 0")
