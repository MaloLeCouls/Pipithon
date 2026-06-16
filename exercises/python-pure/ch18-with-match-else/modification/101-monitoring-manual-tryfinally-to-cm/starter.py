"""Le module monitoring a un `traced_run(probe, work)` qui active la sonde
avant `work()`, et la désactive ensuite — y compris si `work` plante.
Aujourd'hui c'est un try/finally inline. Le chapitre 18 dit : extrais-le
en *context manager* réutilisable.

Refactor :
1. Crée `tracing_window(probe)` (fonction décorée `@contextmanager`) qui
   active la sonde à l'entrée et la désactive à la sortie (toujours).
2. Réécris `traced_run(probe, work)` pour qu'il **utilise** `tracing_window`
   via un `with` — plus aucun `try`/`finally` visible dans `traced_run`.

Le comportement (`probe.active` True pendant `work`, False après) doit
rester identique."""
from __future__ import annotations

from collections.abc import Callable, Iterator
from contextlib import contextmanager


class Probe:
    def __init__(self) -> None:
        self.active: bool = False


def traced_run(probe: Probe, work: Callable[[], None]) -> None:
    probe.active = True
    try:
        work()
    finally:
        probe.active = False


@contextmanager
def tracing_window(probe: Probe) -> Iterator[Probe]:
    raise NotImplementedError("À implémenter")
    yield probe  # pragma: no cover
