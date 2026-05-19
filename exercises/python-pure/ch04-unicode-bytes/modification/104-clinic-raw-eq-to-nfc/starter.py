"""Ce rapprochement de dossiers patients compare les noms brut à brut.
Il rate les noms identiques à l'œil mais encodés différemment.

Refactor `is_match` :
- compare les noms après normalisation NFC,
- comportement préservé quand les deux formes sont déjà identiques.
"""


def is_match(name_a: str, name_b: str) -> bool:
    return name_a == name_b
