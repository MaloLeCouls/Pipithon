"""Un site e-commerce modélise un panier.

Implémente `Cart` avec @dataclass :
- `customer_id: str`,
- `items: list[str]` qui démarre VIDE par défaut,
  via field(default_factory=list) (un `= []` lèverait une erreur de
  dataclass, et partagerait l'état entre instances).
- une méthode `add(self, sku: str) -> None` qui ajoute au panier.

Deux Cart créés sans items doivent avoir des listes indépendantes.
"""

from dataclasses import dataclass, field  # noqa: F401


class Cart:
    ...
