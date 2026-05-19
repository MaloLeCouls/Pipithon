"""Un cabinet médical fusionne des dossiers patients venant de systèmes
différents. Le même nom "Zoé" peut être saisi avec un 'é' précomposé
(U+00E9) dans l'un et 'e' + accent combinant (U+0301) dans l'autre :
visuellement identiques, mais `a == b` renvoie False.

Implémente `same_name(a: str, b: str) -> bool` :
- True si les deux noms sont canoniquement équivalents,
- via une normalisation NFC avant comparaison.
"""


def same_name(a: str, b: str) -> bool:
    ...
