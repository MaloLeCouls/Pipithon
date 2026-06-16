"""`inference_window(session)` est un context manager qui marque la session
comme `active` à l'entrée, et `idle` à la sortie. Tests verts en local,
mais en intégration on observe des sessions coincées en `active` après
une erreur de génération — le scheduler refuse alors de nouvelles
requêtes pour ces sessions.

Trouve la cause et corrige."""
from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager


class Session:
    def __init__(self, session_id: str) -> None:
        self.session_id = session_id
        self.state: str = "idle"


@contextmanager
def inference_window(session: Session) -> Iterator[Session]:
    session.state = "active"
    yield session
    # BUG : cette ligne n'est PAS exécutée si le bloc `with` lève une
    # exception (elle est injectée au point du yield, et fait remonter
    # sans toucher au reste du générateur).
    session.state = "idle"
