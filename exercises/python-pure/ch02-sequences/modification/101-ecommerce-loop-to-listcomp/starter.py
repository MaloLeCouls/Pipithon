"""Ce code marche mais accumule à la main.

Refactor `discounted_skus` en UNE list comprehension :
- même résultat exactement,
- pas de boucle for explicite, pas de .append().
"""


def discounted_skus(products: list[dict]) -> list[str]:
    result = []
    for p in products:
        if p["discount"] > 0:
            result.append(p["sku"])
    return result
