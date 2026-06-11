"""Le catalogue d'un fabricant de meubles est un dict `{section: [refs]}`
(deux niveaux : sections, et listes mutables de références).

Implémente `clone_catalog(cat: dict[str, list[str]]) -> dict[str, list[str]]`
qui renvoie une copie *profonde*. Muter une section du clone ne doit jamais
toucher l'original.

PIÈGE SIGNALÉ : `copy.copy` ne suffit pas — il copie le dict mais les listes
internes restent les mêmes objets.
"""
from __future__ import annotations


def clone_catalog(cat: dict[str, list[str]]) -> dict[str, list[str]]:
    ...
