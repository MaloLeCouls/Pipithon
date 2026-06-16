"""Tu cherches la première métrique au-dessus d'un seuil critique. Si tu la
trouves, tu retournes son nom. Sinon, tu retournes une valeur par défaut.

Le pattern classique en Python : `for ... else` — le `else` s'exécute
seulement si la boucle ne `break` pas.

Implémente `first_critical(metrics, threshold, default)` :
- `metrics` : liste de `Metric` (`name: str`, `value: float`).
- `threshold` : seuil.
- `default` : valeur à retourner si aucune métrique ne dépasse `threshold`.
- Retourne le `name` de la première métrique dont `value > threshold`,
  ou `default` si la boucle se termine sans avoir trouvé.

⚠️ Utilise **`for ... else`** (pas de drapeau `found = False`)."""
from __future__ import annotations


class Metric:
    def __init__(self, name: str, value: float) -> None:
        self.name = name
        self.value = value


def first_critical(metrics: list[Metric], threshold: float, default: str) -> str:
    raise NotImplementedError("À implémenter")
