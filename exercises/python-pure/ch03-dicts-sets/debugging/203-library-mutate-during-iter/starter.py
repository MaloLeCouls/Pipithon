"""purge_unavailable doit retirer de l'index les livres dont le nombre
de copies est 0. Il plante en pleine itération.
Corrige en chirurgie, sans changer le contrat (mutation en place du dict
passé, et retour de ce même dict).
"""


def purge_unavailable(stock: dict[str, int]) -> dict[str, int]:
    for isbn, copies in stock.items():
        if copies == 0:
            del stock[isbn]
    return stock
