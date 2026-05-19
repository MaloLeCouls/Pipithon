"""Choix de design :
- La list comprehension dit l'intention ('les sku en promo') en une
  expression, sans variable d'accumulation ni mutation : moins de surface
  à bugger, et c'est l'idiome attendu en review.
"""


def discounted_skus(products: list[dict]) -> list[str]:
    return [p["sku"] for p in products if p["discount"] > 0]
