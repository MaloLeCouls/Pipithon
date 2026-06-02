"""Choix de design :
- @dataclass régénère __init__/__repr__/__eq__ identiques à la main, en
  3 lignes : moins de surface à bugger, repr/eq toujours synchronisés
  avec les champs. C'est le refactor attendu sur ce boilerplate.
"""

from dataclasses import dataclass


@dataclass
class Product:
    product_id: str
    price: float
