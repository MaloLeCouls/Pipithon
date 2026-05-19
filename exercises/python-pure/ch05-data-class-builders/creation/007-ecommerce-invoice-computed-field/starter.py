"""Une facture agrège des lignes (quantité, prix unitaire) et expose un
total CALCULÉ (pas fourni au constructeur).

Implémente `Invoice` avec @dataclass :
- `invoice_id: str`,
- `lines: list[tuple[int, float]]`  # (quantité, prix_unitaire)
- `total: float` dérivé : champ field(init=False), rempli par
  __post_init__ = somme des quantité * prix_unitaire.

Piège signalé : `total` ne doit PAS être un paramètre du constructeur
(field(init=False)) ; sinon on pourrait passer un total incohérent.
"""

from dataclasses import dataclass, field  # noqa: F401


class Invoice:
    ...
