"""Un gestionnaire de tâches limite les titres : il faut savoir combien
de caractères ET combien d'octets UTF-8 pèse un titre.

Implémente `sizes(title: str) -> tuple[int, int]` :
- renvoie (nombre_de_caractères, nombre_d_octets_utf8).
"""


def sizes(title: str) -> tuple[int, int]:
    ...
