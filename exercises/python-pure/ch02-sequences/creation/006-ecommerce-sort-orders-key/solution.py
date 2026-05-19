"""Choix de design :
- sorted() (pas list.sort()) : on veut une nouvelle liste sans toucher
  l'entrée — sort() muterait l'argument et renverrait None.
- key composite (priority, -total) : tri lexicographique du tuple ->
  priority croissante puis total décroissant, en une seule passe stable.
"""


def triage(orders: list[dict]) -> list[dict]:
    return sorted(orders, key=lambda o: (o["priority"], -o["total"]))
