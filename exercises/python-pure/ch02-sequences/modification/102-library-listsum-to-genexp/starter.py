"""Ce code matérialise une liste juste pour la sommer.

Refactor `late_fees_total` : passe une generator expression à sum()
(pas de list comprehension intermédiaire). Résultat identique.
"""


def late_fees_total(loans: list[dict]) -> float:
    return sum([loan["fine"] for loan in loans if loan["late"]])
