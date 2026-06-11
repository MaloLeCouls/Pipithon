"""Une plateforme de livraison a une fonction générique de calcul de route :

    route_from(depot: str, destination: str) -> str

mais en pratique chaque flotte de camions part TOUJOURS du même dépôt.
On veut produire, pour un dépôt donné, une fonction spécialisée qui n'attend
plus que la destination.

Implémente `make_router(depot: str) -> Callable[[str], str]` qui renvoie une
fonction `f(destination)` équivalente à `route_from(depot, destination)`.

Utilise `functools.partial`. Pas de def imbriqué, pas de lambda.
"""
from __future__ import annotations

from collections.abc import Callable


def route_from(depot: str, destination: str) -> str:
    return f"{depot} -> {destination}"


def make_router(depot: str) -> Callable[[str], str]:
    ...
