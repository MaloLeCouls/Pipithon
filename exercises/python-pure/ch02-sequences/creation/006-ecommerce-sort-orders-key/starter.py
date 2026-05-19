"""Un site e-commerce veut trier ses commandes pour traitement.

Chaque commande est un dict : {"id": str, "priority": int, "total": float}
(priority : 0 = urgent, 1 = normal, 2 = basse).

Implémente `triage(orders: list[dict]) -> list[dict]` :
- trié par priority croissante (0 d'abord),
- à priority égale, par total DÉCROISSANT (les gros paniers d'abord),
- renvoie une NOUVELLE liste (l'entrée ne doit pas être modifiée).

Piège signalé : `orders.sort()` mute l'entrée et renvoie None — ce n'est
PAS ce qu'on veut ici.
"""


def triage(orders: list[dict]) -> list[dict]:
    ...
