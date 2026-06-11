"""Choix de design :
- Default = None (immutable) plutôt qu'une liste : impossible à partager.
- À l'intérieur, on crée une liste neuve si l'appelant n'en a pas fourni.
- On peut accepter la liste de l'appelant telle quelle OU en faire une copie
  défensive ; ici on copie pour éviter qu'une mutation externe affecte la tâche.
"""
from __future__ import annotations


def create_task(title: str, tags: list[str] | None = None) -> dict:
    if tags is None:
        tags = []
    return {"title": title, "tags": list(tags)}
