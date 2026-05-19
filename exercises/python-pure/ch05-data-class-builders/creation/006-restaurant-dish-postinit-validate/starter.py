"""Un restaurant modélise un plat. Un plat invalide ne doit pas exister.

Implémente `Dish` avec @dataclass :
- champs : `name: str`, `price: float`,
- `__post_init__` : lève ValueError("name vide") si name est vide
  (ou seulement des espaces), et ValueError("price doit être > 0")
  si price <= 0.
- un plat valide se construit sans erreur.
"""

from dataclasses import dataclass  # noqa: F401


class Dish:
    ...
