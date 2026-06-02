"""Choix de design :
- field(default_factory=list) remplace le None-guard : @dataclass
  appelle list() à chaque instance, jamais de liste partagée.
- total() reste une méthode normale, @dataclass ne gère que les
  champs (annotations).
"""

from dataclasses import dataclass, field


@dataclass
class Payslip:
    employee_id: str
    base: float
    bonuses: list[float] = field(default_factory=list)

    def total(self) -> float:
        return self.base + sum(self.bonuses)
