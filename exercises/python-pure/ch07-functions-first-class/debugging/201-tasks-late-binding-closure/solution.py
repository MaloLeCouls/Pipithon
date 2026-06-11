"""Bug : `lambda: i` capture la variable `i`, pas sa valeur au moment de la
construction. Quand la comprehension est terminée, i vaut n-1 — toutes les
lambdas pointent vers le même i.

Fix idiomatique : `lambda i=i: i` — la valeur courante est figée dans le
default argument, évalué AU MOMENT DE LA DÉFINITION du lambda.
"""
from __future__ import annotations

from collections.abc import Callable


def make_task_factories(n: int) -> list[Callable[[], int]]:
    return [lambda i=i: i for i in range(n)]
