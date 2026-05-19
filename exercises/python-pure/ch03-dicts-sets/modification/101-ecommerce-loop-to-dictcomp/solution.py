"""Choix de design :
- Dict comprehension : intention déclarative, pas de dict mutable
  intermédiaire ni boucle. Idiome attendu en review.
"""


def stock_index(products: list[dict]) -> dict[str, int]:
    return {p["sku"]: p["stock"] for p in products}
