"""CHECKPOINT chapitre 5 — si tu fais ça sans réfléchir, les data class
builders sont acquis.

Une bibliothèque décrit ses ressources façon Dublin Core.

Implémente `Resource` avec @dataclass :
- `identifier: str`           (obligatoire)
- `title: str`                (obligatoire)
- `authors: list[str]`        (optionnel, vide par défaut)
- `subjects: list[str]`       (optionnel, vide par défaut)
- `description: str | None`   (optionnel, None par défaut)
- `_normalized: str`          (interne : title.strip().lower(), calculé
                               en __post_init__, EXCLU du repr et de
                               __init__)

Règles :
- authors/subjects via field(default_factory=list) (jamais `= []`).
- __post_init__ : ValueError("identifier requis") si identifier vide ;
  remplit `_normalized`.
- repr ne montre PAS `_normalized`.
"""

from dataclasses import dataclass, field  # noqa: F401


class Resource:
    ...
