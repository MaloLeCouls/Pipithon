"""Corrections (chirurgie) :
- Bug 1 : products.sort(...) mutait la liste de l'appelant. -> sorted()
  produit une nouvelle liste, l'entrée reste intacte.
- Bug 2 : tri ascendant + [:n] renvoyait les PIRES ventes. -> reverse=True
  (ou key négative) pour avoir les meilleures d'abord.
"""


def best_sellers(products: list[dict], n: int) -> list[dict]:
    ranked = sorted(products, key=lambda p: p["sales"], reverse=True)
    return ranked[:n]
