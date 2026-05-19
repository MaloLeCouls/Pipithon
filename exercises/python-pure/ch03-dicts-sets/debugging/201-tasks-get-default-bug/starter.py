"""group_by_assignee a 1 bug : le dict renvoyé est toujours vide.
Corrige en chirurgie, sans réécrire from scratch.
"""


def group_by_assignee(tasks: list[dict]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for t in tasks:
        groups.get(t["assignee"], []).append(t["id"])
    return groups
