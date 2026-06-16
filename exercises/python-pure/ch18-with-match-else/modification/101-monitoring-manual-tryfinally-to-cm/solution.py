"""Choix de design :
- L'extraction en context manager rend `traced_run` trivial à lire (un
  `with`, un appel) et `tracing_window` réutilisable ailleurs (pas juste
  pour `work`).
- `@contextmanager` est la forme la plus concise pour un pattern à un
  seul aller-retour setup/cleanup.
- `try/finally` reste DANS `tracing_window` — c'est son rôle de garantir
  le cleanup même sur exception du bloc.
"""
from __future__ import annotations

from collections.abc import Callable, Iterator
from contextlib import contextmanager


class Probe:
    def __init__(self) -> None:
        self.active: bool = False


@contextmanager
def tracing_window(probe: Probe) -> Iterator[Probe]:
    probe.active = True
    try:
        yield probe
    finally:
        probe.active = False


def traced_run(probe: Probe, work: Callable[[], None]) -> None:
    with tracing_window(probe):
        work()
