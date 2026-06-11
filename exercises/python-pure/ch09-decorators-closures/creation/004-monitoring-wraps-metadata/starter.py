"""Un décorateur d'instrumentation : compte les appels via un attribut
`__calls__` sur la fonction décorée.

Implémente `instrument(fn)` :
- définit un wrapper interne qui appelle fn et incrémente un compteur,
- utilise `@functools.wraps(fn)` pour préserver les métadonnées,
- attache `wrapper.__calls__ = 0` initialement,
- renvoie wrapper.

Les tests vérifient que __name__, __doc__ de la fn d'origine sont préservés.
"""
from __future__ import annotations


def instrument(fn):
    ...
