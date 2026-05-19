"""Une bibliothèque a un index {isbn: title} et veut l'inverse
{title: isbn} pour chercher par titre.

Implémente `invert(catalog: dict[str, str]) -> dict[str, str]` :
- renvoie {title: isbn},
- via une dict comprehension sur catalog.items(),
- sans modifier `catalog`.
"""


def invert(catalog: dict[str, str]) -> dict[str, str]:
    ...
