"""Choix de design :
- field(default_factory=list) : la fabrique est appelée à CHAQUE
  instanciation -> chaque Cart a sa propre liste. `items: list = []`
  est refusé par dataclass précisément pour empêcher l'état partagé
  (le piège du défaut mutable, classique en entretien).
"""

from dataclasses import dataclass, field


@dataclass
class Cart:
    customer_id: str
    items: list[str] = field(default_factory=list)

    def add(self, sku: str) -> None:
        self.items.append(sku)
