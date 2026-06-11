"""Une API REST de gestion de tâches crée des tickets. Le piège classique :
`def create_task(title, tags=[])` partage la liste `tags` entre TOUS les
appels qui ne fournissent pas explicitement de tags.

Implémente `create_task(title: str, tags: list[str] | None = None) -> dict`
en utilisant le **pattern sentinelle** None pour éviter le bug.

Le dict renvoyé doit contenir au moins les clés 'title' et 'tags'.
"""
from __future__ import annotations


def create_task(title: str, tags: list[str] | None = None) -> dict:
    ...
