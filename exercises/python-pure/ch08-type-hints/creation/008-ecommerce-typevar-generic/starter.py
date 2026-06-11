"""Une plateforme e-commerce a besoin d'une fonction utilitaire générique :
prendre le premier élément d'un itérable, ou renvoyer une valeur par défaut.

Implémente `first_or_default(items, default)` :
- accepte n'importe quel itérable d'un type T,
- accepte une `default` du même type T,
- renvoie le premier item ou `default` si l'itérable est vide.

Utilise `TypeVar` pour signaler que entrée et sortie partagent le même type.
"""
from __future__ import annotations


def first_or_default(items, default):
    ...
