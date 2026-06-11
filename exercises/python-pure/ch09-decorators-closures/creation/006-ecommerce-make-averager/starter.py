"""Une plateforme e-commerce veut une moyenne CONTINUE des prix de commande
(pas la moyenne d'une liste figée).

Implémente `make_averager()` qui renvoie une fonction `(new_price: float) -> float`.
Chaque appel ajoute new_price à l'historique interne et renvoie la moyenne
courante.

Pas de liste exposée : seulement deux variables (total, count) en closure +
nonlocal.

Exemple :
    avg = make_averager()
    avg(10) -> 10.0
    avg(20) -> 15.0
    avg(30) -> 20.0
"""
from __future__ import annotations

from collections.abc import Callable


def make_averager() -> Callable[[float], float]:
    ...
