"""Correction :
- Bug : groups.get(k, []) renvoie une NOUVELLE liste éphémère quand k
  est absent ; on append dessus puis elle est jetée -> rien n'est stocké.
- Fix : setdefault(k, []) insère ET renvoie la liste DANS le dict, donc
  l'append persiste. (defaultdict(list) serait aussi valable.)
"""


def group_by_assignee(tasks: list[dict]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for t in tasks:
        groups.setdefault(t["assignee"], []).append(t["id"])
    return groups
