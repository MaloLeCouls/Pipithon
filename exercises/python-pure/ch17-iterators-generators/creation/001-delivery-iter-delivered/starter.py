"""Une compagnie de livraison veut un flux paresseux des colis livrés
(intégration en streaming, sans charger toute la base en RAM).

Implémente `iter_delivered(packages)` :
- `packages` : itérable de `Package` (attributs `tracking_id: str` et
  `status: str`).
- yield le `tracking_id` (str) de chaque colis dont `status == "delivered"`.

C'est un **générateur** (mot-clé `yield`), pas une liste construite à l'avance.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Package:
    def __init__(self, tracking_id: str, status: str) -> None:
        self.tracking_id = tracking_id
        self.status = status


def iter_delivered(packages: Iterable[Package]) -> Iterator[str]:
    raise NotImplementedError("À implémenter")
