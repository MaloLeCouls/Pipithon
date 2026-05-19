"""Choix de design :
- {v: k for k, v in catalog.items()} : itère sur les paires plutôt que
  sur les clés puis re-lookup ; lisible, une passe, sans mutation.
- Si deux livres ont le même titre, le dernier isbn gagne (sémantique dict).
"""


def invert(catalog: dict[str, str]) -> dict[str, str]:
    return {title: isbn for isbn, title in catalog.items()}
