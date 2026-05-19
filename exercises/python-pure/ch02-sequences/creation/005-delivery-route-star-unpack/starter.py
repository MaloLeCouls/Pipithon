"""Une route de livraison est une liste d'arrêts (str), du dépôt au dernier
client.

Implémente `split_route(route: list[str]) -> tuple[str, list[str], str]` :
- renvoie (premier_arret, arrets_du_milieu, dernier_arret),
- `arrets_du_milieu` est une list (vide s'il n'y a que 2 arrêts),
- utilise le star unpacking (first, *middle, last = ...).

Si la route a moins de 2 arrêts, lève ValueError("route trop courte").
"""


def split_route(route: list[str]) -> tuple[str, list[str], str]:
    ...
