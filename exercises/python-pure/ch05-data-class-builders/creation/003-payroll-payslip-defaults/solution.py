"""Choix de design :
- Défauts immuables (str, float) déclarés directement : sûr (pas de
  partage d'état entre instances, contrairement à une liste/dict).
- Champs obligatoires d'abord, puis ceux à défaut : contrainte du
  modèle dataclass (sinon TypeError à la définition de la classe).
"""

from dataclasses import dataclass


@dataclass
class Payslip:
    employee_id: str
    gross: float
    currency: str = "EUR"
    tax_rate: float = 0.2
