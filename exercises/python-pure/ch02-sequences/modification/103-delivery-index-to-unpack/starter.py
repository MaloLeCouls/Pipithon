"""Ce code lit un record colis par indices. Illisible.

Le record est (tracking_id, weight_kg, zone, express).

Refactor `routing_label` : déballe le tuple par unpacking nommé, plus
aucun accès rec[i]. Comportement identique.
"""


def routing_label(rec: tuple) -> str:
    if rec[3]:
        return f"{rec[0]} [EXPRESS {rec[2]}] {rec[1]}kg"
    return f"{rec[0]} [{rec[2]}] {rec[1]}kg"
