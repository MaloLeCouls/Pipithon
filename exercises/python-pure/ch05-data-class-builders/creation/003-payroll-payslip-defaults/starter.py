"""Un service paie modélise un bulletin.

Implémente `Payslip` avec @dataclass :
- `employee_id: str` (obligatoire),
- `gross: float` (obligatoire),
- `currency: str` avec défaut "EUR",
- `tax_rate: float` avec défaut 0.2.

Construire Payslip("E1", 3000.0) doit marcher (défauts appliqués).
"""

from dataclasses import dataclass  # noqa: F401


class Payslip:
    ...
