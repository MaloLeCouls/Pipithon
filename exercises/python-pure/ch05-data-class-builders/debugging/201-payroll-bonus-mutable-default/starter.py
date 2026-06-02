"""Le module entier refuse de s'importer : ValueError des la
declaration de la classe. Trouve le defaut interdit, et fournis
le bon mecanisme @dataclass pour une liste vide par defaut.

Contrainte : meme API publique (Payslip(employee_id, base) et
Payslip(employee_id, base, bonuses)).
"""

from dataclasses import dataclass


@dataclass
class Payslip:
    employee_id: str
    base: float
    bonuses: list[float] = []

    def total(self) -> float:
        return self.base + sum(self.bonuses)
