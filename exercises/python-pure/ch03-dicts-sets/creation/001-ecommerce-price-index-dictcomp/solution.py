"""Choix de design :
- Dict comprehension : l'intention ('indexer le prix par sku') tient en
  une expression, sans dict mutable intermédiaire ni boucle explicite.
- En cas de SKU dupliqué, la dernière valeur gagne (sémantique dict
  naturelle) — cohérent avec un index.
"""


def price_index(products: list[dict]) -> dict[str, float]:
    return {p["sku"]: p["price"] for p in products}
