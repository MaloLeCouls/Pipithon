"""Checkpoint ch.18 — LookingGlass, en classe ET en @contextmanager.

Choix de design :
- Monkey-patching de `sys.stdout.write` : on sauve l'original, on installe
  un wrapper, on restore dans __exit__/finally. C'est exactement le pattern
  enseigné par Fluent Python — minimal, vérifie qu'on a compris la
  symétrie enter/exit.
- Avalement sélectif de `ZeroDivisionError` : `__exit__` retourne True
  *uniquement* pour ce type, sinon None implicite (laisse remonter).
- Forme `@contextmanager` : try/except sur ZeroDivisionError + finally
  pour le restore. C'est strictement équivalent à la classe ; on choisit
  selon le style/lisibilité.
"""
from __future__ import annotations

import sys
from collections.abc import Iterator
from contextlib import contextmanager


class LogMirror:
    def __enter__(self) -> str:
        self._original_write = sys.stdout.write

        def reversed_write(text: str) -> int:
            return self._original_write(text[::-1])

        sys.stdout.write = reversed_write  # type: ignore[method-assign]
        return "MIRROR"

    def __exit__(self, exc_type, exc, tb):
        sys.stdout.write = self._original_write  # type: ignore[method-assign]
        if exc_type is not None and issubclass(exc_type, ZeroDivisionError):
            self._original_write("RECOVERED")
            return True
        return None


@contextmanager
def log_mirror() -> Iterator[str]:
    original_write = sys.stdout.write

    def reversed_write(text: str) -> int:
        return original_write(text[::-1])

    sys.stdout.write = reversed_write  # type: ignore[method-assign]
    try:
        yield "MIRROR"
    except ZeroDivisionError:
        original_write("RECOVERED")
    finally:
        sys.stdout.write = original_write  # type: ignore[method-assign]
