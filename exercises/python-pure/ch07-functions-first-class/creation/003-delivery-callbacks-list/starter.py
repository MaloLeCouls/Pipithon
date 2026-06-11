"""Une plateforme de livraison enregistre des callbacks à appeler quand un
colis change de statut (audit, notification client, log...).

Implémente `notify_all(callbacks, package_id)` :
- Pour chaque callback dans `callbacks`, appelle-la avec `package_id`.
- Accumule les retours dans une liste.
- Renvoie la liste dans l'ordre d'appel.
"""
from __future__ import annotations

from collections.abc import Callable


def notify_all(
    callbacks: list[Callable[[str], str]], package_id: str
) -> list[str]:
    ...
