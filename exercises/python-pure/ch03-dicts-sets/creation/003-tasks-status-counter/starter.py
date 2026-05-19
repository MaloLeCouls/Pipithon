"""Un board de tâches veut le nombre de tickets par statut.

Implémente `count_status(tasks: list[dict]) -> collections.Counter` :
- chaque tâche est un dict {"id": str, "status": str},
- renvoie un Counter {status: nombre},
- utilise collections.Counter (pas de dict rempli à la main).
"""

import collections  # noqa: F401


def count_status(tasks: list[dict]) -> "collections.Counter":
    ...
