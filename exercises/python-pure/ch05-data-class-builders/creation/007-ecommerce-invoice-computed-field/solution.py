"""Choix de design :
- total = field(init=False) : il est DÉRIVÉ, pas saisi. L'exclure de
  __init__ rend impossible un total incohérent passé par l'appelant ;
  __post_init__ le calcule une fois à partir des lignes.
- default=0.0 pour que la dataclass ait une valeur avant __post_init__.
"""

from dataclasses import dataclass, field


@dataclass
class Invoice:
    invoice_id: str
    lines: list[tuple[int, float]]
    total: float = field(init=False, default=0.0)

    def __post_init__(self) -> None:
        self.total = sum(qty * price for qty, price in self.lines)
