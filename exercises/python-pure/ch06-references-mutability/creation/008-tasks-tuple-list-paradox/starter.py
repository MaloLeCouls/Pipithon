"""Un ticket de tâche est un tuple `(id: int, tags: list[str])` : on aime
le tuple pour signaler que la structure est immuable... sauf que la liste
interne, elle, ne l'est pas. `ticket[1] += new_tags` est un piège :
ça mute la liste ET ça lève TypeError.

Implémente `add_tags_safely(ticket: tuple[int, list[str]], new_tags: list[str])
-> tuple[int, list[str]]` qui renvoie un NOUVEAU tuple avec une NOUVELLE liste
de tags concaténés. Le ticket d'origine est inchangé.

PIÈGE SIGNALÉ : ne fais pas `ticket[1].extend(new_tags)` ni
`ticket[1] += new_tags`.
"""
from __future__ import annotations


def add_tags_safely(
    ticket: tuple[int, list[str]], new_tags: list[str]
) -> tuple[int, list[str]]:
    ...
