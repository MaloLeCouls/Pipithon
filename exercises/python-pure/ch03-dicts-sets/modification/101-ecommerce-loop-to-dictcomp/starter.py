"""Ce code remplit un dict à la main.

Refactor `stock_index` en UNE dict comprehension :
- même résultat exactement,
- pas de boucle for explicite.
"""


def stock_index(products: list[dict]) -> dict[str, int]:
    d = {}
    for p in products:
        d[p["sku"]] = p["stock"]
    return d
