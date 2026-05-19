"""best_sellers a 2 bugs. Les tests les exposent.
Corrige en chirurgie, sans réécrire from scratch.

Contrat attendu :
- renvoie les `n` produits aux ventes les PLUS élevées, du meilleur au moins bon ;
- ne modifie PAS la liste passée en argument.
"""


def best_sellers(products: list[dict], n: int) -> list[dict]:
    products.sort(key=lambda p: p["sales"])
    return products[:n]
