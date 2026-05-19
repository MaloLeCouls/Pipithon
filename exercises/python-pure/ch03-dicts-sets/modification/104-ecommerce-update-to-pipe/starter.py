"""Ce code fusionne deux grilles tarifaires en trois lignes.

Refactor `merge_pricing` avec l'opérateur | :
- même résultat (extra écrase base sur clé commune),
- ne mute toujours pas base,
- une seule expression.
"""


def merge_pricing(
    base: dict[str, float], extra: dict[str, float]
) -> dict[str, float]:
    merged = base.copy()
    merged.update(extra)
    return merged
