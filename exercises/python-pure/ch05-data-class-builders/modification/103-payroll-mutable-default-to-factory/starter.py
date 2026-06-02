"""Payslip stocke des bonus (liste). Le code suivant marche, mais
le None-guard manuel + __init__ écrit à la main est la version
artisanale d'un pattern dataclass.

Refactor en @dataclass :
- mêmes champs (employee_id: str, base: float, bonuses: list[float]),
- bonuses par défaut = liste vide PROPRE à chaque instance,
- plus de None-guard, plus de __init__ manuel.
"""


class Payslip:
    def __init__(self, employee_id, base, bonuses=None):
        if bonuses is None:
            bonuses = []
        self.employee_id = employee_id
        self.base = base
        self.bonuses = bonuses

    def total(self):
        return self.base + sum(self.bonuses)
