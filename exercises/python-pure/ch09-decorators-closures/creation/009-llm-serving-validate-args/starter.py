"""On veut un garde-fou : aucune fonction d'inférence ne doit s'exécuter
avec une GenerationConfig dont temperature < 0.5 (politique métier).

Implémente le décorateur `validate_temperature(fn)` :
- Inspecte la signature de fn pour trouver le paramètre typé GenerationConfig.
- Quand on appelle la fn, récupère la valeur de ce paramètre (positional ou keyword).
- Si config.temperature < 0.5 : lève ValueError("temperature too low: <val>").
- Sinon : exécute fn et renvoie son résultat.

Hint : inspect.signature(fn).parameters te donne les annotations.
"""
from __future__ import annotations

import inspect

from pymistral import GenerationConfig  # noqa: F401


def validate_temperature(fn):
    ...
