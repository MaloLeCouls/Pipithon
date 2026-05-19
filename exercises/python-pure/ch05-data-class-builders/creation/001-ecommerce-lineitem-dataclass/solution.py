"""Choix de design :
- @dataclass génère __init__/__repr__/__eq__ à partir des champs annotés :
  zéro boilerplate, et le repr/eq restent synchronisés si on ajoute un
  champ. C'est l'idiome moderne pour un simple porteur de données.
"""

from dataclasses import dataclass


@dataclass
class LineItem:
    sku: str
    quantity: int
    unit_price: float
