"""Module legacy de routing. Le comportement est correct mais zéro annotation.

Refactor :
1. Annote TOUTES les signatures (params + retours).
2. Le module doit passer `mypy --strict` (le validateur le vérifie).

Garde la sémantique. Ne change pas les noms de fonctions ni de paramètres.
"""


def total_distance(stops):
    return sum(s["km"] for s in stops)


def average_per_stop(stops):
    if not stops:
        return 0.0
    return total_distance(stops) / len(stops)
