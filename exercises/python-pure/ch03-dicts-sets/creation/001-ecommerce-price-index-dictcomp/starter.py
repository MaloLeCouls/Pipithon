"""Un site e-commerce veut un index rapide prix-par-SKU.

Chaque produit est un dict {"sku": str, "price": float, ...}.

Implémente `price_index(products: list[dict]) -> dict[str, float]` :
- renvoie {sku: price} pour tous les produits,
- via une dict comprehension (pas de boucle for + d[k] = v).
"""


def price_index(products: list[dict]) -> dict[str, float]:
    ...
