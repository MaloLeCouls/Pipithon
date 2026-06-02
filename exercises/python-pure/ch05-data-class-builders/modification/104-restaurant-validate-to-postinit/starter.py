"""Dish a un prix : il doit être > 0. Aujourd'hui un caller distrait
peut construire un Dish à prix nul/négatif sans rien voir, puis
appeler validate_dish() en bout de chaine (ou l'oublier).

Refactor :
- Garde @dataclass et les mêmes champs (name: str, price: float).
- Déplace la validation dans __post_init__ pour qu'elle soit
  systématique : impossible de construire un Dish invalide.
- Supprime validate_dish (le test importe seulement Dish).
"""

from dataclasses import dataclass


@dataclass
class Dish:
    name: str
    price: float


def validate_dish(d: Dish) -> None:
    if d.price <= 0:
        raise ValueError("price must be > 0")
