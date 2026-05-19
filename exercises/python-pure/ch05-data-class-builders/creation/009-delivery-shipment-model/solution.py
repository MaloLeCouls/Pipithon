"""Choix de design :
- parcels = field(default_factory=list) : pas d'état partagé entre
  envois (le piège du défaut mutable, non signalé ici).
- total_weight = field(init=False) : dérivé, recalculé en __post_init__
  (cohérent même si parcels est fourni au constructeur) et maintenu par add().
- Normalisation de zone dans __post_init__ : l'invariant 'zone canonique'
  est garanti dès la construction, quel que soit l'appelant.
"""

from dataclasses import dataclass, field


@dataclass
class Shipment:
    zone: str
    parcels: list[float] = field(default_factory=list)
    total_weight: float = field(init=False, default=0.0)

    def __post_init__(self) -> None:
        self.zone = self.zone.strip().upper()
        self.total_weight = sum(self.parcels)

    def add(self, weight: float) -> None:
        self.parcels.append(weight)
        self.total_weight += weight
