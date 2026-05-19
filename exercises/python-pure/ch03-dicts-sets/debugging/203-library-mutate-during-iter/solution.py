"""Correction :
- Bug : `del stock[isbn]` pendant `for ... in stock.items()` change la
  taille du dict en cours d'itération -> RuntimeError.
- Fix : on itère sur un instantané `list(stock.items())` ; on peut alors
  muter `stock` en toute sécurité. Le contrat (mutation en place + retour
  du même objet) est préservé.
"""


def purge_unavailable(stock: dict[str, int]) -> dict[str, int]:
    for isbn, copies in list(stock.items()):
        if copies == 0:
            del stock[isbn]
    return stock
