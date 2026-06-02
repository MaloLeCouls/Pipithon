"""Correction :
- Bug : `bonuses: list[float] = []` -> @dataclass leve ValueError
  ("mutable default ... is not allowed: use default_factory") parce
  qu'une seule liste serait partagee entre toutes les instances.
- Fix : field(default_factory=list) construit une liste FRESH a
  chaque instance, jamais partagee.
"""

from dataclasses import dataclass, field


@dataclass
class Payslip:
    employee_id: str
    base: float
    bonuses: list[float] = field(default_factory=list)

    def total(self) -> float:
        return self.base + sum(self.bonuses)
