"""Ce code groupe les colis par chauffeur avec le boilerplate classique
`if key not in d`.

Refactor `by_driver` avec collections.defaultdict :
- même résultat (mêmes listes, même ordre),
- plus de test d'existence de clé manuel,
- renvoie un dict ordinaire.
"""


def by_driver(packages: list[dict]) -> dict[str, list[str]]:
    groups = {}
    for pkg in packages:
        d = pkg["driver"]
        if d not in groups:
            groups[d] = []
        groups[d].append(pkg["tracking"])
    return groups
