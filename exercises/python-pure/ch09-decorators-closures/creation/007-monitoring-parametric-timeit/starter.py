"""Une plateforme de monitoring veut tagger ses fonctions avec un label,
puis tracer chaque exécution sous ce label.

Implémente :
- `TIMINGS: list[tuple[str, object]]` (label, result).
- un décorateur PARAMÉTRÉ `timed(label: str)` :
    * usage : @timed("hot_path") def f(...): ...
    * append (label, result) à TIMINGS à chaque appel de f.
    * préserve la valeur de retour.

C'est le pattern 3-niveaux : timed -> wrapper_factory -> wrapper.
"""
from __future__ import annotations

TIMINGS: list[tuple[str, object]] = []


def timed(label: str):
    ...
