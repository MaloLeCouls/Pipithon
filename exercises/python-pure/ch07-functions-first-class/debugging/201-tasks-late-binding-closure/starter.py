"""On veut construire N « tâches préfabriquées » : chacune est une fonction
sans argument qui renvoie son numéro.

BUG : toutes les fonctions renvoient le MÊME numéro (le dernier).

Corrige `make_task_factories`. Une ligne suffit (presque).
"""
from __future__ import annotations

from collections.abc import Callable


def make_task_factories(n: int) -> list[Callable[[], int]]:
    return [lambda: i for i in range(n)]
