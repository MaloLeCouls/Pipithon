"""Un envoi regroupe des colis pour une zone donnée.

Implémente `Shipment` avec @dataclass :
- `zone: str` (obligatoire),
- `parcels: list[float] ` : poids des colis, liste VIDE par défaut,
- `total_weight: float` : DÉRIVÉ (pas saisi), = somme des poids,
- à la construction, `zone` est normalisée : espaces retirés et mise
  en MAJUSCULES (ex. "  eu-west " -> "EU-WEST").

Méthode `add(self, weight: float) -> None` : ajoute un colis ET met à
jour total_weight.
"""

from dataclasses import dataclass, field  # noqa: F401


class Shipment:
    ...
