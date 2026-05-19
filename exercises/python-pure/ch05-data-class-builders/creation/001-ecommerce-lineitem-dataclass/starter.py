"""Un site e-commerce modélise une ligne de commande.

Implémente `LineItem` avec @dataclass :
- champs : `sku: str`, `quantity: int`, `unit_price: float`,
- __init__, __repr__ et __eq__ doivent être GÉNÉRÉS (ne les écris pas).

Repr attendu (format dataclass standard) :
LineItem(sku='A1', quantity=2, unit_price=9.9)
"""

from dataclasses import dataclass  # noqa: F401


class LineItem:
    ...
