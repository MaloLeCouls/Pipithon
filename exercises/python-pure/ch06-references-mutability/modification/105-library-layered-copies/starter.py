"""Catalogue d'une bibliothèque : {author -> [book_dict]} avec book_dict
= {"title": str, "reviews": list[str]} (les `reviews` sont mutables).

Le clone actuel utilise copy.copy : il copie le dict racine, mais les listes
de livres et les dicts internes restent partagés.

Refactor : `deepcopy` est la réponse robuste. Justifie en commentaire pourquoi
une copie plus subtile (3 niveaux à la main) serait fragile face à un
contributeur qui rajoute un quatrième niveau plus tard.
"""
from __future__ import annotations

import copy


def clone_catalog(catalog: dict[str, list[dict]]) -> dict[str, list[dict]]:
    return copy.copy(catalog)
